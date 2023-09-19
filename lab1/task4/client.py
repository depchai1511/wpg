import socket
import threading
import sys

host = 'localhost'
port = 4000

# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

def receive_messages():
    """Receive messages from the server"""
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
        except:
            # An error occurred, close the connection
            print('An error occurred while receiving messages.')
            client_socket.close()

def send_messages():
    """Send messages to the server"""
    while True:
        try:
            message = input()
            client_socket.send(message.encode('utf-8'))
        except KeyboardInterrupt:
            # client_socket.close()
            client_socket.close()
            
           
        


def main() :
    # Create two threads for receiving and sending messages
    receive_thread = threading.Thread(target=receive_messages)
    receive_thread.start()

    send_thread = threading.Thread(target=send_messages)
    send_thread.start()

if __name__ == "__main__":
    main()

