import socket

host = ''        # Symbolic name meaning all available interfaces
port = 12345     # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))

print ("Listening")
s.listen(1)
conn, addr = s.accept()
print('Connected by', addr)
while True:

    try:
        data = conn.recv(1024)

        if not data: break

        print ("Client Request received: ", data.decode('utf-8'))
        conn.sendall(bytes("Hi I am Server", 'utf-8'))

    except socket.error:
        print ("Error Occured.")
        break

conn.close()