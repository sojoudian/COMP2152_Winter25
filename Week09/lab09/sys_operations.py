import platform
import socket
import os
import sys

print(f"\nMachine Type: {platform.machine()}")
print(f"\nProcessor Type: {platform.architecture()}")

socket.setdefaulttimeout(50)
print(f"\nDefault Timeout for Socket: {socket.getdefaulttimeout()}")

print(f"\nOS Type: {os.name}")
print(f"\nOS Name: {platform.system()}")
print(f"\nCurrent PID: {os.getpid()}")

file_name = "fdpractice.txt"
file_handle = os.open(file_name, os.O_RDWR | os.O_CREAT)
file_object_TextIO = os.fdopen(file_handle, "w+")
file_object_TextIO.write("Some string to write to this file")
file_object_TextIO.flush()

# windows
# pid = 0
pid = os.fork()
if pid == 0:
    print(f"\n[Child PID: {os.getpid()}], [Parent PID: {os.getppid()}]")
    os.lseek(file_handle, 0, 0)
    print(f"\n[Child PID: {os.getpid()}] File Content: {os.read(file_handle, 100).decode()}")
    os.close(file_handle)
    sys.exit(0)
else:
    print(f"\n[Parent PID: {os.getpid()}], [Child PID: {pid}]")    
    print("Wait for child")
    os.waitpid(pid, 0)
    print("child finished")
    file_object_TextIO.close()
sys.exit(0)    