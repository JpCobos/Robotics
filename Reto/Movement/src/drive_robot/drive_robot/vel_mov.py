import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class RobotControlNode(Node):
    def __init__(self):
        super().__init__('robot_control_node')

        # Publishers for left and right motor velocities
        self.left_motor_pub = self.create_publisher(Float32, '/leftMotorSpeed', 10)
        self.right_motor_pub = self.create_publisher(Float32, '/rightMotorSpeed', 10)

        # Subscribers for robot position (using Float32 for x and y position)
        self.position_sub_x = self.create_subscription(Float32, '/x_position', self.position_callback_x, 10)
        self.position_sub_y = self.create_subscription(Float32, '/y_position', self.position_callback_y, 10)

        # Timer for publishing velocities
        self.timer = self.create_timer(0.1, self.publish_velocities)  # 0.1 seconds (10 Hz)
        
        # Default velocity to publish
        self.velocity = 2.0  
        self.publish_duration = 2.0  # Duration to move forward in seconds
        self.start_time = self.get_clock().now()  # Save start time as ROS2 time object

        # Variables to store current position
        self.current_x = 0.0
        self.current_y = 0.0
        self.robot_moving = True  # Flag to indicate if the robot should still move

    def position_callback_x(self, msg):
        # Update the x position from the Float32 message
        self.current_x = msg.data
        self.get_logger().info(f"Current x position: {self.current_x}")

    def position_callback_y(self, msg):
        # Update the y position from the Float32 message
        self.current_y = msg.data
        self.get_logger().info(f"Current y position: {self.current_y}")

    def publish_velocities(self):
        # Calculate elapsed time since the start of movement
        current_time = self.get_clock().now()
        elapsed_time = (current_time - self.start_time).nanoseconds / 1e9  # Convert to seconds

        if elapsed_time < self.publish_duration:
            # Publish velocity to both motors to move forward
            if self.robot_moving:
                self.get_logger().info(f'Publishing velocity: {self.velocity}')
                left_msg = Float32(data=self.velocity)
                right_msg = Float32(data=self.velocity)
                self.left_motor_pub.publish(left_msg)
                self.right_motor_pub.publish(right_msg)
        else:
            # Stop the robot after the duration
            if self.robot_moving:
                self.get_logger().info('Stopping robot after 2 seconds')
                self.left_motor_pub.publish(Float32(data=0.0))
                self.right_motor_pub.publish(Float32(data=0.0))
                self.robot_moving = False  # Flag to stop publishing velocities
                self.timer.cancel()  # Stop the timer
                self.get_logger().info(f'Final Position: x={self.current_x}, y={self.current_y}')


def main(args=None):
    rclpy.init(args=args)
    node = RobotControlNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Shutting down robot control node')
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
