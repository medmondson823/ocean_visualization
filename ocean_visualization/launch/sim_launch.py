from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare

import os

def generate_launch_description():
    pkg_share = FindPackageShare(package='ocean_visualization').find('ocean_visualization')
    gz_pkg_share = FindPackageShare(package='ros_gz_sim').find('ros_gz_sim')
    world_path = os.path.join(pkg_share, 'worlds', 'ocean_world.sdf')
    gazebo_path = os.path.join(gz_pkg_share, 'launch', 'gz_sim.launch.py')

    gazebo_sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([gazebo_path]),
        launch_arguments={'gz_args': f"-r -v 4 {world_path}"}.items()
    )

    return LaunchDescription([gazebo_sim])
