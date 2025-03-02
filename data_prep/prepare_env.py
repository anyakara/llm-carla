"""
Define the following for PythonAPI level implementation:
CarlaInterface: Connects to the simulator
VehicleManager: Handles vehicle spawning
Sensor (base class): Abstract class for all sensors (sensor) // might or might not use its
    .. bc each sensor is so different in its acquisition process
Derived Sensor Classes (CameraSensor, LidarSensor, etc.): implements specific Sensor behaviors
SensorManager: manges sensor lifecyle and data processing
DataProcessor: saves and processes sensor data
"""

import carla
import time
import numpy as np
import cv2
import os
import json
from queue import Queue
from threading import Thread

def data_deposit_config(self, dir_name:str):
    """ Configure data deposit. """
    data_dumps = "./{dir_name}"
    if not os.path.exists(data_dumps):
        os.makedirs(data_dumps)
    print(f"Created {dir_name} in provided repository.")
    return data_dumps

class CarlaClientInterface:
    def __init__(self, host_port:int, timeout:float):
        self.client = carla.Client('localhost', 2000)
        self.client.set_timeout(10.0)
        self.world = self.client.get_world()

class Vehicle:
    def __init__(self, inf_client: CarlaClientInterface):
        self.spawn_points = self.world.get_map().get_spawn_points()
        self.spawn_point = self.spawn_points[0]
        self.vehicle = self.world.spawn_actor(self.world.get_blueprint_library().find('vehicle.tesla.model3'), \
                                              self.spawn_point)

class Sensor:
    def __init__(self):
        pass


class CameraSensor(Sensor):
    def __init__(self):
        super().__init__()

    @staticmethod
    def save_image(dir_name, img, fname) -> None:
        img.save_to_disk(f"{dir_name}/{fname}.png")
    
    def process_camera_img(img, queue):
        pass







__namespace__ = [data_deposit_config, CarlaClientInterface, Vehicle, Sensor, CameraSensor]