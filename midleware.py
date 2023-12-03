import socket
import threading
from datetime import datetime, date, time, timezone

IP_MAQ_1 = "192.168.40.128"
IP_MAQ_2 = "127.0.0.1"
IP_MAQ_3 = "192.168.40.136"
IP_MAQ_4 = "192.168.40.137"

ip_propio = "192.168.40.142" #Infosec2
SERVER = socket.gethostbyname(socket.gethostname())
PORT = 9999
ADDR = (SERVER, PORT)

def handle_client(client_socket):
    request = client_socket.recv(1024)
    print(f"Recibido: {request.decode('utf-8')}")
    client_socket.send(b"Recibido")
    client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0",PORT))
    server.listen(5)
    print("Servidor en espera en el puerto 9999")

    while True:
        client_socket, addr = server.accept()
        print(f"Accepted connection from {addr[0]}:{addr[1]}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

def send_message(message,SERVER):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1",9999))
    client.send(message.encode('utf-8'))
    response = client.recv(1024)
    print(f"Server response: {response.decode('utf-8')}")
    client.close()

if _name_ == "_main_":
    # Start the server in a separate thread
    				
	server_thread = threading.Thread(target=start_server)
	server_thread.start()

	while True: 
		# Simulate client behavior in the main thread
		opcion = input("A que maquina te quieres conectar: ")
		match opcion:
			case "1":
				SERVER = IP_MAQ_1
			case "2":
				SERVER = IP_MAQ_2
			case "3":
				SERVER = IP_MAQ_3
			case "4":	
				SERVER = IP_MAQ_4
			case _:
				SERVER = socket.gethostbyname(socket.gethostname())
		message = input("Agrega el mensaje: ")
		send_message(SERVER,message)

	# Wait for the server thread to finish before exiting
	server_thread.join()