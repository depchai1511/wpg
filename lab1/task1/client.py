import socket

host = 'localhost'
port = 4000


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((host, port))

    try:
        while True:
            type = input('Do you want to send message to server ?(y/n)')
            type.lower()
            if(type=='n'):
                break
            
            s.send(b"Hello, server")
            reply_message = s.recv(1024).decode("utf-8")
            print(f"Server reply: {reply_message}")
                
    except KeyboardInterrupt:
        pass

    except Exception as e:
        # Xử lý các ngoại lệ khác
        print("An error occurred:", str(e))

    finally:
        s.close()



if __name__ == "__main__":
    main()