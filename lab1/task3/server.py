import socket

host = 'localhost'
port = 4000

def get_response_html():
    try:
        with open("index.html", "r") as file:
            html_content = file.read()
    except FileNotFoundError:
        html_content = "<html><body><h1>File index.html isn't found</h1></body></html>"

    response = f"HTTP/1.1 200 OK\r\nContent-Length: {len(html_content)}\r\n\r\n{html_content}"
    return response


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)

    print("Server listening on port", port)

    while True:
        client, addr = s.accept()
        print(f"Connection from {addr}")

        request = client.recv(1024).decode('utf-8')

        if request:
            response = get_response_html()
            client.send(response.encode('utf-8'))

        client.close()


if __name__ == "__main__":
    main()