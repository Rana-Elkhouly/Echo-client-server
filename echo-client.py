import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    message = input()
    message = bytes(message, encoding='utf8')
    #s.sendall(b"hello, "+ message +b"!")
    s.sendall(message)
    data = s.recv(1024)

print("Received", repr(data))
