from socket import *
import sys

if len(sys.argv) < 2:
    print("Error: U didnt provide the server IP address")
    print("Usage: python TCPTimeClient.py <server_ip>")
    sys.exit()

serverName = sys.argv[1]
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)

try:
    clientSocket.connect((serverName, serverPort))
except Exception as e:
    print("Error connecting to server: ", e)
    sys.exit()

print("options: date, day, month, year, hour")
parameter = input("Enter a parameter: ")

clientSocket.send(parameter.encode())
response = clientSocket.recv(1024).decode()

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Server response: ", response)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

clientSocket.close()