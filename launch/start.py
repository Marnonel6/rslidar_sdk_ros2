from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch.conditions import IfCondition
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument(
            name='use_rviz',
            default_value='true',
            choices=['true','false'],
            description='Open RVIZ for visualization'
        ),
        Node(
            namespace='rslidar_sdk',
            package='rslidar_sdk',
            executable='rslidar_sdk_node',
            output='screen'
        ),
        Node(
            namespace='rviz2',
            package='rviz2',
            executable='rviz2',
            arguments=[
                '-d',
                PathJoinSubstitution([
                    FindPackageShare('rslidar_sdk'),
                    'rviz',
                    'rviz2.rviz'
                ])
            ],
            condition=IfCondition(LaunchConfiguration('use_rviz'))
        ),
    ])
