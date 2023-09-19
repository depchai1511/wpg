import socket

host = 'localhost'
port = 4000



def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    try:
        while True:
            type = input('Do you want to send message to server ?(y/n)')
            type.lower()
            if(type=='n'):
                break
            a = input("Enter the larger base of the trapezoid: ")
            b = input("Enter the smaller base of the trapezoid: ")
            h = input("Enter the height of the trapezoid: ")
            # a='1'
            # b='2'
            # h= '3'
            message = a + "," + b + "," + h

            s.send(message.encode("utf-8"))
            reply_message = s.recv(1024).decode("utf-8")
            print(f"Area is : {reply_message}")
                
    except KeyboardInterrupt:
        pass

    except Exception as e:
        # Xử lý các ngoại lệ khác
        print("An error occurred:", str(e))

    finally:
        s.close()



if __name__ == "__main__":
    main()