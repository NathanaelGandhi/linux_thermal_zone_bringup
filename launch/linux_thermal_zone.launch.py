import os

from ament_index_python import get_package_share_directory
from launch_ros.actions import PushRosNamespace

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import GroupAction
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch.substitutions import TextSubstitution


def generate_launch_description():

    ltz_ns = LaunchConfiguration("ltz_ns")

    # args that can be set from the command line or a default will be used
    ltz_ns_launch_arg = DeclareLaunchArgument(
        "ltz_ns", default_value=TextSubstitution(text="ltz")
    )

    # include a Python launch file in the namespace
    launch_py_include_with_namespace = GroupAction(
        actions=[
            # push_ros_namespace to set namespace of included nodes
            PushRosNamespace(ltz_ns),
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(
                    os.path.join(
                        get_package_share_directory("linux_thermal_zone_bringup"),
                        "launch/ltz_base.launch.py",
                    )
                )
            ),
        ]
    )

    return LaunchDescription(
        [
            ltz_ns_launch_arg,
            launch_py_include_with_namespace,
        ]
    )
