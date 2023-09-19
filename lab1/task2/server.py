import socket 

host = 'localhost'
port = 4000

def calc(a,b,h) :
    return (a+b)//2 *h

def main() :
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)
    print("Server listening on port", port)

    try:
        while True:
            client,_ = s.accept()
            # print(client)
            # mess, addr = s.recvfrom(1024)
            mess = client.recv(1024).decode("utf-8")
            clientMsg = "Message from Client: {}".format(mess)
            
            a,b,h = map(int,mess.split(','))
            print(clientMsg)
            area = calc(a,b,h)
            client.send(str(area).encode("utf-8"))

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
    # print(calc(1,2,3))


