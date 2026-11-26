import socket

# Create DNS server socket
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind server to localhost and port 5053
server.bind(("127.0.0.1", 5053))

print("================================")
print("       DNS EXPLORER SERVER")
print("================================")
print("Server started successfully!")
print("Listening on UDP Port 5053")
print("Waiting for client query...\n")

while True:
    # Receive request from client
    data, client_address = server.recvfrom(1024)

    # Convert received data into domain name
    domain = data.decode().strip()

    print("--------------------------------")
    print(f"DNS Query Received: {domain}")
    print(f"Client Address: {client_address}")

    # Resolve domain name into IP address
    try:
        ip_address = socket.gethostbyname(domain)
        response = f"SUCCESS: {domain} = {ip_address}"

    except socket.gaierror:
        response = f"ERROR: Domain '{domain}' not found"

    # Send response back to client
    server.sendto(response.encode(), client_address)

    print(f"Response: {response}")
    print("Response sent to client")
    print("Waiting for next query...\n")