from collections.abc import MutableMapping
import sys
if sys.version_info.major == 3 and sys.version_info.minor >= 10:
 import collections
 setattr(collections,"MutableMapping",collections.abc.MutableMapping)
from dronekit import connect , VehicleMode , LocationGlobalRelative , APIException
import time
import socket
#import exceptions
import math
import argparse



def connectMyCopter ():
    parser  =  argparse.ArgumentParser(description="commands")
    parser.add_argument('--connect')
    args = parser.parse_args()

    connection_string  = args.connect
    baud_rate  =  57600

    vehicle = connect(connection_string , wait_ready=True, timeout=30)
    print("connected")
    return vehicle

def arm(aTargetAltitude):
    while vehicle.is_armable==False:
        print("Waiting for vehicle to become armable ..")
        time.sleep(1)

    print("Vehicle is now armed")
    print("OMG Props are spinning look out")

    vehicle.mode    = VehicleMode("GUIDED")
    vehicle.armed = True
    #return None

    while not vehicle.armed:
        print(" Waiting for arming...")
        time.sleep(1)

    print("Taking off!")
    vehicle.simple_takeoff(aTargetAltitude) # Take off to target altitude

    # Wait until the vehicle reaches a safe height before processing the goto (otherwise the command
    #  after Vehicle.simple_takeoff will execute immediately).
    while True:
        print (" Altitude: ", vehicle.location.global_relative_frame.alt)
        #Break and return from function just below target altitude.
        if vehicle.location.global_relative_frame.alt>=aTargetAltitude*0.95:
            print("Reached target altitude")
            break
        time.sleep(1)



    time.sleep(10)
    vehicle.mode = VehicleMode("LAND")
    vehicle.armed = False
    return None

vehicle = connectMyCopter()
arm(1)
print("End of script")
