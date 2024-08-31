import socket

# Get the hostname of the machine
hostname = socket.gethostname()

# Get the IP address of the hostname
IPAddr = socket.gethostbyname(hostname)

# Print the IP address
print("The IP address of the Computer:", IPAddr)

