import ssl
import socket

def create_client():
    context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    context.load_verify_locations('../certs/cert.pem')

    with socket.create_connection(('localhost', 8443)) as sock:
        with context.wrap_socket(sock, server_hostname='localhost') as ssock:
            print(f"Client: Sending secure data")
            ssock.send(b"Training/inference data")
            data = ssock.recv(1024)
            print(f"Client: Received {data}")

if __name__ == "__main__":
    create_client()
