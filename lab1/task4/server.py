import socket 
import threading 

host = 'localhost'
port = 4000
clients = []
client_names = []

def broadcast(message, sender):
    """Send message to all clients (except sender)"""
    
    for client in clients:
        if client != sender:
            client.send(message)


def handle_client(client):
    """Handle connections from a client"""
    while True:
        try:
            message = client.recv(1024)
            if not message :
                raise Exception
            else :
                broadcast(message, client)

        except:
            # A connection error occurred, close the connection and remove the client from the list
            index = clients.index(client)
            clients.remove(client)
            client.close()
            name = client_names[index]
            client_names.remove(name)
            
            broadcast(f'{name} has left the chat.\n'.encode('utf-8'), None)
            break
        


def main() :
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(10)
    print("Server listening on port", port)

    try:
        """Start listening for connections from clients"""
        while True:
            client,addr = s.accept()
            # mess, addr = s.recvfrom(1024)
            clientMsg = "New Client address: {}".format(addr)
            print(clientMsg)
            client.send('NAME'.encode('utf-8'))
            name = client.recv(1024).decode('utf-8')
            client_names.append(name)
            clients.append(client)

            print(f'New client name: {name}')
            broadcast(f'{name} has join the chat.\n'.encode('utf-8'), None)
            client.send('Connection successful! You have joined the chat.'.encode('utf-8'))

            thread = threading.Thread(target=handle_client, args=(client,))
            thread.start()

    except KeyboardInterrupt:
        # Ctrl+C
        pass

    except Exception as e:
        
        print("An error occurred:", str(e))

    finally:
        s.close()


if __name__ == "__main__":
    main()
  


