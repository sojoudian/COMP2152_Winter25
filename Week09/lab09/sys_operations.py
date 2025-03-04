import platform
import socket
import os
import sys

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

print("Current Process ID")
print(os.getpid())
print ("-------------------------------\n")

file_name = "fdpractice.txt"
# Print the PID of the process before forking
print(f"[Before Fork] Process ID: {os.getpid()}")

# Open the file using os.open (low-level file handling)
file_handle = os.open(file_name, os.O_RDWR | os.O_CREAT)
print(f"\n[Process ID {os.getpid()} opened file_handle: {file_handle}]")

# Convert the file handle into a file object for writing
file_object_TextIO = os.fdopen(file_handle, "w+")

# Write text to the file
file_object_TextIO.write("Lab Tue 10 to 12")
file_object_TextIO.flush() # Ensure content is written immediately

print(f"[Before Fork] Process ID: {os.getpid()}")

#######
pid = os.fork()

if pid == 0:
    # Child process
    print(f"\n[Child Process] PID: {os.getpid()}, Parent PID {os.getppid()}")
    
    # Move the cursor to the beginning of the file before reading
    os.lseek(file_handle, 0, 0)

    # Read and print the file contents
    print(f"[Child process {os.getpid()} File Content: {os.read(file_handle, 100).decode()}]")

    # Close only in the child process
    os.close(file_handle)
    sys.exit(0) # Exit child process safely

else:
    # Parent Process
    print(f"\n[Parent Process] PID: {os.getpid()}, Child PID {pid}")

    print("Wait for the Child Process")
    os.wait
    print("The Child Process is finished it's operations")

    file_object_TextIO.close()

print(f"\n[Parent {os.getpid()}], File Closed. Exiting now")
sys.exit(0)