from socket import *
import threading
from datetime import datetime

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(2)
print("The server is ready to receive")
print("Listening on port", serverPort, "- waiting for a client... (press Ctrl+C to stop)")

def handle_client(connectionSocket, addr):
    print("client connected from: ", addr)

    try:
        request = connectionSocket.recv(1024).decode()
        print("client request: ", request)
        now = datetime.now()
        response = ""

        if request == "date":
            response = now.strftime("%Y-%m-%d")
        
        elif request == "day":
            response = now.strftime("%d")

        elif request == "month":
            response = now.strftime("%m")

        elif request == "year":
            response = now.strftime("%Y")
        
        elif request == "hour":
            response = now.strftime("%H:%M:%S")
        
        else:
            response = "Invalid request"

        connectionSocket.send(response.encode())

    except Exception as e:
        print("Error handling client request: ", e)

    finally:
        connectionSocket.close()
        print("client disconnected from: ", addr)

while True:
        clientSocket, addr = serverSocket.accept()
        clientThread = threading.Thread(target=handle_client, args=(clientSocket, addr))
        clientThread.start()
