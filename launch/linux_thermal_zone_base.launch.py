from launch_ros.actions import Node

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import TextSubstitution


def generate_launch_description():

    # args that can be set from the command line or a default will be used
    base_ns_launch_arg = DeclareLaunchArgument(
        "base_ns",
        default_value=TextSubstitution(text="base"),
        description="Set the namespace of the base node",
    )

    # start a in a namespace
    base_node = Node(
        package="linux_thermal_zone_base",
        namespace="base_ns",
        executable="linux_thermal_zone_base",
        name="ltz_base",
    )

    return LaunchDescription(
        [
            base_ns_launch_arg,
            base_node,
        ]
    )
