import platform
import socket
import os

print("Current machine type")
print(platform.machine()) # Apple M1, M2, M3, M4, Raspberry Pi : arm64; for intel/AMD: x86
print ("-------------------------------\n")

print("Current Processor Type:")
print(platform.architecture())
print ("-------------------------------\n")

print("Set timeout of socket in seconds")
socket.setdefaulttimeout(50)
print ("-------------------------------\n")

print("Get timeout of socket in seconds")
print(socket.getdefaulttimeout())
print ("-------------------------------\n")

print("Operating System type")
print(os.name)
print ("-------------------------------\n")

print("Operating System name")
print(platform.system())
print ("-------------------------------\n")