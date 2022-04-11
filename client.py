import socket

server_ip = '192.168.1.112'
print("Connecting to Server: ", server_ip)
port = 12345                   # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((server_ip, port))
s.sendall(bytes('Hello I am client !', 'utf-8'))
data = s.recv(1024)
s.close()
print('Server Response received:', data.decode('utf-8'))