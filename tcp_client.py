import socket

def tcp_client():
    target_host = input("Please Enter the domain name/ host name of the server")
    target_port = input("Please Enter the port of the socket")

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target_host, target_port))

    client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

    respone = client.recv(4096)

    print(respone.decode())
    client.close()

if __name__ == "__main__":
    tcp_client()