import socket 

host = 'localhost'
port = 4000

def main() :
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))
    print("Server listening on port", port)

    try:
        while True:
            
            mess, addr = s.recvfrom(1024)
            mess = mess.decode("utf-8")
            clientMsg = "Message from Client: {}".format(mess)
            clientIP = "Client IP Address: {}".format(addr)

            print(clientMsg)
            print(clientIP)
            s.sendto(b'Hello client!', addr)

    except KeyboardInterrupt:
        # Ngắt chương trình khi nhận được tín hiệu Ctrl+C
        pass

    except Exception as e:
        # Xử lý các ngoại lệ khác
        print("An error occurred:", str(e))

    finally:
        s.close()


if __name__ == "__main__":
    main()

