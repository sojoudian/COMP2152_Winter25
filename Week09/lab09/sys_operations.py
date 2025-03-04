# Lab 9 - import the libraries os, sys, platform, and socket
import os
import sys
import platform
import socket

# Lab 9 - Practicing System Operations
print("Current machine type")
print(platform.machine())
print("--")
print("Current processor type")
print(platform.architecture())
print("--")

print("Set timeout time of socket in seconds")
print(socket.setdefaulttimeout(50))
print("--")
print("Get the default timeout of socket")
print(socket.getdefaulttimeout())
print("--")
print("Operating system type")
print(os.name)
print("--")
print("Operating system name")
print(platform.system())
print("--")
print("Current process ID (different for every run of the program)")
print(os.getpid())
print("--")

file_name = "fdpractice.txt"

# Print the PID of the process before forking
print(f"\n[Before Fork] Process PID: {os.getpid()}")

# Open the file using os.open (low-level file handling)
file_handle = os.open(file_name, os.O_RDWR | os.O_CREAT)
print(f"\n[Process {os.getpid()}] Opened file_handle: {file_handle}")

# Convert the file handle into a file object for writing
file_object_TextIO = os.fdopen(file_handle, "w+")

# Write text to the file
file_object_TextIO.write("Some string to write to the file")
file_object_TextIO.flush()  # Ensure content is written immediately

# Print PID before forking
print(f"\n[Process {os.getpid()}] Forking now...")

# Fork a new process
pid = os.fork()

if pid == 0:
    # Child Process
    print(f"\n[Child Process] PID: {os.getpid()}, Parent PID: {os.getppid()}")

    # Move the cursor to the beginning of the file before reading
    os.lseek(file_handle, 0, 0)

    # Read and print the file contents
    print(f"[Child Process {os.getpid()}] File Content: {os.read(file_handle, 100).decode()}")

    # Close only in the child process
    os.close(file_handle) # May not be necessary on your system
    sys.exit(0)  # Exit child process safely

else:
    # Parent Process
    print(f"\n[Parent Process] PID: {os.getpid()}, Child PID: {pid}")

    # Wait for the child process to finish
    print("Wait for child")
    os.wait()
    print("Child finished")

    # Close the file descriptor only in the parent
    file_object_TextIO.close()

print(f"\n[Process {os.getpid()}] File closed. Exiting now.")
sys.exit(0)

