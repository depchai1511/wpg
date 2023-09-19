import socket

host = 'localhost'
port = 4000

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.connect((host,port))

        request = "GET / HTTP/1.1\r\nHost: localhost\r\n\r\n"
        s.send(request.encode('utf-8'))

        response = s.recv(1024).decode('utf-8')
        print(response)

    except KeyboardInterrupt:
        # Ngắt chương trình khi nhận được tín hiệu Ctrl+C
        pass

    except Exception as e:
        # Xử lý các ngoại lệ khác
        print("An error occurred:", str(e))


if __name__ == "__main__":
    main()