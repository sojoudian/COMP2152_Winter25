import platform
import socket
import os

print("Current Machine Type")
print(platform.machine()) 
print("===============================")

print("Current Processor Type")
print(platform.architecture())
print("===============================")

print("Set Socket Timeout to 50 Seconds")
print(socket.setdefaulttimeout(50))
print("Get the current Socket Timeout")
print(socket.getdefaulttimeout())

print("===============================")
print("Get the current Operating System Type")
print(os.name)
print("Get the current Operating System Name")
print(platform.system())

print("===============================")
print("Current Process ID")
print(os.getpid())

file_name = "fdpractice.txt"
print(f"\n[Before Fork] Process {os.getpid()}")

file_handle = os.open(file_name, os.O_RDWR | os.O_CREAT)
print(f"\n[Process {os.getpid()}] Opened file_handle: {file_handle}")

file_object_TextIO = os.fdopen(file_handle, "w+")

file_object_TextIO.write("Some string to write to the file")
file_object_TextIO.flush()