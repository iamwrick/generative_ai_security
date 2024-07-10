import ssl
import socket

def create_server():
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile="../certs/cert.pem", keyfile="../certs/key.pem")

    bindsocket = socket.socket()
    bindsocket.bind(('localhost', 8443))
    bindsocket.listen(5)
    print("Server listening on port 8443")

    while True:
        newsocket, fromaddr = bindsocket.accept()
        conn = context.wrap_socket(newsocket, server_side=True)
        try:
            data = conn.recv(1024)
            print(f"Received: {data}")
            conn.send(b"Data received securely")
        finally:
            conn.shutdown(socket.SHUT_RDWR)
            conn.close()

if __name__ == "__main__":
    create_server()
