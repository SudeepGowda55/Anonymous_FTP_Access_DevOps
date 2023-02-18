import socket

def udp_client():
    target_host = input("Please Enter the domain name/ host name of the server")
    target_port = input("Please Enter the port of the socket")

    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.sendto(b"Hello", (target_host, target_port))

    data, addr = client.recvfrom(4096)

    print(data.decode())
    client.close()

if __name__=="__main__":
    udp_client()