import platform
import socket

print(f"\nMachine Type: {platform.machine()}")
print(f"\nProcessor Type: {platform.architecture()}")

socket.setdefaulttimeout(50)
print(f"\nDefault Timeout for Socket: {socket.getdefaulttimeout()}")