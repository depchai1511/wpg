# Задание 1

Реализовать клиентскую и серверную часть приложения. Клиент
отсылает серверу сообщение «Hello, server». Сообщение должно
отразиться на стороне сервера. Сервер в ответ отсылает клиенту
сообщение «Hello, client». Сообщение должно отобразиться у клиента.
Обязательно использовать библиотеку socket. Реализовать с помощью
протокола UDP.

## Выполнение

### Реализация сервера

```python

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
```

### Реализация клиента

```python
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
```

## Пример работы
![Пример задания 1](images/task_1.png)