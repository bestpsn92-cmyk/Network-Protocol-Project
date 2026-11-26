import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ("127.0.0.1", 5053)

domain = input("Enter domain name: ")

client.sendto(domain.encode(), server_address)

data, address = client.recvfrom(1024)

print("\nDNS Server Response:")
print(data.decode())

client.close()