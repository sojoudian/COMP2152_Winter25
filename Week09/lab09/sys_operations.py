import platform
import socket
import os
import sys

print(f"\nMachine Type: {platform.machine()}")
print(f"\nProcessor Type: {platform.architecture()}")

socket.setdefaulttimeout(50)
print(f"\nDefault Timeout for Socket: {socket.getdefaulttimeout()}")

print(f"\nOS Type: {os.name()}")
print(f"\nOS Name: {platform.system()}")