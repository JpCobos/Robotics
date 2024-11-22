import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
from std_msgs.msg import Bool


class MotorControlNode(Node):
    def __init__(self):
        super().__init__('motor_control_node')
        
        # Subscriptions to motor speed topics
        self.left_motor_sub = self.create_subscription(
            Float32,
            'leftMotorSpeed',
            self.left_motor_callback,
            10)
        self.right_motor_sub = self.create_subscription(
            Float32,
            'rightMotorSpeed',
            self.right_motor_callback,
            10)
        
        # Publisher for sensor trigger
        self.sensor_pub = self.create_publisher(
            Bool,
            'sensorTrigger',
            10)

    def left_motor_callback(self, msg):
        # Set the left motor speed in the simulation
        self.get_logger().info(f"Setting left motor speed to {msg.data}")
        # Send motor speed to the simulator (you'll need to call the appropriate sim function in the bridge)

    def right_motor_callback(self, msg):
        # Set the right motor speed in the simulation
        self.get_logger().info(f"Setting right motor speed to {msg.data}")
        # Send motor speed to the simulator (you'll need to call the appropriate sim function in the bridge)

    def sensor_publish(self, sensor_value):
        # Publish sensor data (True/False) to ROS2
        msg = Bool()
        msg.data = sensor_value
        self.sensor_pub.publish(msg)
        self.get_logger().info(f"Publishing sensor trigger: {sensor_value}")

def main(args=None):
    rclpy.init(args=args)
    motor_control_node = MotorControlNode()
    rclpy.spin(motor_control_node)
    motor_control_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
