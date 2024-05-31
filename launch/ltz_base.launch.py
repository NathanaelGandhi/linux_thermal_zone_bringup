import os

from ament_index_python import get_package_share_directory
from launch_ros.actions import Node

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch.substitutions import TextSubstitution


def generate_launch_description():

    base_ns = LaunchConfiguration("base_ns")

    # args that can be set from the command line or a default will be used
    base_ns_launch_arg = DeclareLaunchArgument(
        "base_ns",
        default_value=TextSubstitution(text="base"),
        description="Set the namespace of the base node",
    )

    # load parameters from YAML file
    params_file = os.path.join(
        get_package_share_directory("linux_thermal_zone_bringup"),
        "params",
        "ltz_base.params.yaml",
    )

    # start a in a namespace
    base_node = Node(
        package="linux_thermal_zone_base",
        namespace=base_ns,
        executable="linux_thermal_zone_base",
        name="ltz_base",
        parameters=[params_file],
    )

    return LaunchDescription(
        [
            base_ns_launch_arg,
            base_node,
        ]
    )
