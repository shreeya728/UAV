from collections.abc import MutableMapping
import collections 
import sys
if sys.version_info.major == 3 and sys.version_info.minor >= 10:
 import collections
 setattr(collections,"MutableMapping",collections.abc.MutableMapping)

from dronekit import connect, VehicleMode, LocationGlobalRelative
import time
import math

vehicle = connect('127.0.0.1:14550', wait_ready=True)

def arm_and_takeoff(aTargetAltitude):
    """
    Arms vehicle and fly to aTargetAltitude.
    """

    print("Basic pre-arm checks")
    # Don't try to arm until autopilot is ready
    while not vehicle.is_armable:
        print(" Waiting for vehicle to initialise...")
        time.sleep(1)

    print("Arming motors")
    # Copter should arm in GUIDED mode
    vehicle.mode    = VehicleMode("GUIDED")
    vehicle.armed   = True

    # Confirm vehicle armed before attempting to take off
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

arm_and_takeoff(20)

print("Set default/target airspeed to 3")
vehicle.airspeed = 3

print("Going towards first point for 30 seconds ...")
point1 = LocationGlobalRelative(-35.361354, 149.165218, 20)
vehicle.simple_goto(point1)

# sleep so we can see the change in map
time.sleep(30)

print("Send coordinates from master to 2 slaves")

# Central point coordinates
lat_c = -35.361354
lon_c = 149.165218
alt_c = 20

# Distance between central point and other points (assuming equal sides for equilateral triangle)
distance = 0.0091  # Adjust this value as needed

# Angle between each point (for an equilateral triangle, each angle is 120 degrees)
angle = 120  # in degrees

# Convert angle to radians
angle_rad = math.radians(angle)

# Calculate coordinates of the other two points
lat_1 = lat_c + distance * math.cos(angle_rad)
lon_1 = lon_c + distance * math.sin(angle_rad)

# Adjusting angle for the second point
angle_rad += 2 * math.pi / 3  # Adding 2 * pi / 3 to get the next point

lat_2 = lat_c + distance * math.cos(angle_rad)
lon_2 = lon_c + distance * math.sin(angle_rad)

# Output coordinates
print("Point 1:", lat_1, lon_1)
print("Point 2:", lat_2, lon_2)


print("Going towards second point for 30 seconds ...")
point2 = LocationGlobalRelative(lat_1, lon_1, 20)
vehicle.simple_goto(point2)

# sleep so we can see the change in map
time.sleep(30)

print("Going towards third point for 30 seconds ...")
point2 = LocationGlobalRelative(lat_2, lon_2, 20)
vehicle.simple_goto(point2)

# sleep so we can see the change in map
time.sleep(30)

print("Returning to Launch")
vehicle.mode = VehicleMode("RTL")

# Close vehicle object before exiting script
print("Close vehicle object")
vehicle.close()