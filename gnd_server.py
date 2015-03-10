import socket

HOST = ''  # Symbolic name meaning all available interfaces
PORT = 50007  # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
socket.setdefaulttimeout(1.0)
s.listen(1)  # Listen for incoming connections


while True:
    # Wait for connection
    conn, addr = s.accept()

    try:
        print 'Connected by', addr

        while True:
        # Print all the data received

            data = conn.recv(1024)
            print 'Received:', data

            if not data: 
                print 'no more data'
                break

    finally:
        conn.close()
