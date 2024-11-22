import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from time import sleep

class MoveRobot(Node):
    def __init__(self):
        super().__init__('move_robot')

        # Create a publisher for the cmd_vel topic
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)

        # Create a Twist message to specify linear and angular velocities
        self.vel_msg = Twist()
        self.vel_msg.linear.x = 0.2  # Move forward at 0.2 m/s along the X-axis

        # Start the movement
        self.move_robot()

    def move_robot(self):
        # Publish velocity for 3 seconds
        self.get_logger().info('Moving forward for 3 seconds...')
        start_time = self.get_clock().now().to_msg().sec
        while (self.get_clock().now().to_msg().sec - start_time) < 3:
            self.publisher_.publish(self.vel_msg)
            sleep(0.1)  # Small delay to allow for smooth movement

        # Stop the robot after 3 seconds
        self.vel_msg.linear.x = 0.0
        self.publisher_.publish(self.vel_msg)
        self.get_logger().info('Robot stopped.')

def main(args=None):
    rclpy.init(args=args)
    move_robot_node = MoveRobot()
    rclpy.spin(move_robot_node)
    move_robot_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
