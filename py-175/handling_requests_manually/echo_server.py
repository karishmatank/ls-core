import socket
import random

# Create a TCP server
# AF_INET specifies the address family (IPv4)
# SOCK_STREAM indicates we are using a TCP socket, designed for continuous streams of data
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Tell our server where to listen for incoming requests. We'll use 'localhost' and port 3003
server_socket.bind(('localhost', 3003))
server_socket.listen()

print('Server is running on localhost:3003')

# Run an infinite loop, constantly listening for new connections and accepting incoming connections
while True:
    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr}")

    # Read the incoming data. 1024 is the buffer size (tells recv to read 1024 bytes at a time). 
    # We use decode() to convert bytes into a string, as network data is transmitted in bytes
    request = client_socket.recv(1024).decode()

    # Skip any requests from browsers that request a favicon or that are empty requests
    if (not request) or ('favicon.ico' in request):
        client_socket.close()
        continue

    # Grab the first line of the request, construct an HTTP response, and send to the client
    request_line = request.splitlines()[0]

    # Parse request line into several variables, namely method, path, params
    http_method, path_params, _ = request_line.split()
    path, params_str = path_params.split("?")
    params = {}
    for param in params_str.split("&"):
        key, value = param.split("=")
        params[key] = value

    # Adding in a random number generator to simulate rolling dice
    # Roll as many dice as specified in the params, with the value of each die specified by the sides parameter
    response_body = ("<html>"
                     "<head>"
                     "<title>Dice Rolls</title>"
                     "</head>"
                     "<body>"
                     "<h1>Request Details</h1>"
                     f"<p>Request Line: {request_line}</p>"
                     f"<p>HTTP Method: {http_method}</p>"
                     f"<p>Path: {path}</p>"
                     f"<p>Parameters: {params}</p>"
                     "<h1>Rolls</h1>"
                     "<ul>")
    
    for _ in range(int(params['rolls'])):
        roll = random.randint(1, int(params['sides']))
        response_body += f"<li>Roll: {roll}</li>"

    response_body += "</ul></body></html>"
    
    response = ("HTTP/1.1 200 OK\r\n"
                "Content-Type: text/html\r\n"
                f"Content-Length: {len(response_body)}\r\n"
                "\r\n"
                f"{response_body}\n")
    
    client_socket.sendall(response.encode())
    client_socket.close()