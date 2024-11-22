import cv2
import numpy as np

# Inicialización: configuración del filtro de Kalman y captura de video
def initialize_kalman_filter():
    kalman = cv2.KalmanFilter(4, 2)  # 4 estados, 2 medidas (x, y)
    kalman.measurementMatrix = np.array([[1, 0, 0, 0],
                                         [0, 1, 0, 0]], np.float32)
    kalman.transitionMatrix = np.array([[1, 0, 1, 0],
                                        [0, 1, 0, 1],
                                        [0, 0, 1, 0],
                                        [0, 0, 0, 1]], np.float32)
    kalman.processNoiseCov = np.eye(4, dtype=np.float32) * 0.03  # Ruido del proceso
    return kalman

# Cargar el detector de rostros de Haar Cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Detección: detección de color rojo en el video
def detect_red_object(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Definir el rango de color rojo en HSV
    lower_red1 = np.array([0, 120, 70])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([160, 120, 70])
    upper_red2 = np.array([180, 255, 255])

    # Crear máscara de color rojo
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = cv2.bitwise_or(mask1, mask2)

    # Detectar rostros en la imagen
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    # Enmascarar las áreas de los rostros detectados
    for (x, y, w, h) in faces:
        mask[y:y + h, x:x + w] = 0  # Descartar las áreas del rostro de la máscara

    # Operaciones morfológicas para limpiar la máscara
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    
    # Imprimir el número de píxeles detectados en la máscara
    red_pixels = cv2.countNonZero(mask)
    print(f"Píxeles detectados en la máscara: {red_pixels}")

    # Encontrar contornos
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    if contours:
        # Filtrar contornos por tamaño
        min_area = 100  # Ajusta este valor según las dimensiones del objeto real
        filtered_contours = [contour for contour in contours if cv2.contourArea(contour) > min_area]
        
        if filtered_contours:
            # Encontrar el contorno más grande que cumpla con el área mínima
            largest_contour = max(filtered_contours, key=cv2.contourArea)
            (x, y, w, h) = cv2.boundingRect(largest_contour)
            center = np.array([x + w / 2, y + h / 2], np.float32)
            print(f"Centro detectado: {center}")
            return center, mask  # Devolver el centro y la máscara
    
    print("No se encontró ningún objeto rojo.")
    return None, mask

# Filtrado: aplicación del filtro de Kalman
def apply_kalman_filter(kalman, measurement):
    # Predecir la posición con el filtro de Kalman
    prediction = kalman.predict()
    
    # Si tenemos una nueva medición, corregimos la predicción
    if measurement is not None:
        kalman.correct(measurement)
    return prediction

# Loop principal: procesamiento de cada frame
def process_video(video_path, enable_filter=True):
    cap = cv2.VideoCapture(video_path)
    kalman = initialize_kalman_filter()
    
    last_measurement = None  # Variable para almacenar la última medición válida
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # Detección del objeto rojo
        measurement, mask = detect_red_object(frame)
        
        # Si no se detecta nada, usar la última medición válida
        if measurement is None:
            measurement = last_measurement
        
        # Filtrado con Kalman (si está habilitado)
        if enable_filter:
            prediction = apply_kalman_filter(kalman, measurement)
        else:
            prediction = measurement
        
        # Solo dibujar círculos si measurement y prediction no son None
        if measurement is not None:
            # Dibujar la medición en azul (círculo más pequeño)
            cv2.circle(frame, (int(measurement[0]), int(measurement[1])), 5, (255, 0, 0), -1)  # Azul
            
            # Almacenar la última medición válida
            last_measurement = measurement

        if prediction is not None:
            # Dibujar la predicción de Kalman en verde (círculo más pequeño)
            cv2.circle(frame, (int(prediction[0]), int(prediction[1])), 5, (0, 255, 0), -1)  # Verde
            
        # Mostrar la máscara en una ventana separada
        cv2.imshow("Mask", mask)
        
        # Mostrar el frame con los círculos
        cv2.imshow("Kalman Filter vs Medición", frame)
        
        # Salir si se presiona la tecla ESC
        if cv2.waitKey(30) & 0xFF == 27:  
            break
    
    cap.release()
    cv2.destroyAllWindows()

# Ejecutar la detección y filtrado en el video
video_path = 'video.mp4'
process_video(video_path, enable_filter=True)
