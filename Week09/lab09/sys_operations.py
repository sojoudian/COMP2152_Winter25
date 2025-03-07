import platform
import socket

print("Current Machine Type")
print(platform.machine()) 
print("===============================")

print("Current Processor Type")
print(platform.architecture())
print("===============================")

print("")
print(socket.setdefaulttimeout(50))
print("===============================")
