import platform
import socket
import os

print(f"Machine Type: {platform.machine()}\n")
print(f"CPU Architecture: {platform.architecture()}\n")

socket.setdefaulttimeout(50)
print(f"Current default Socket time out: {socket.getdefaulttimeout()}\n")

print(f"OS Type: {os.name}\n")
print(f"OS name: {platform.system()}\n")