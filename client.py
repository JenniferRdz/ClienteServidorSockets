import socket

# Configuración del cliente
HOST = '127.0.0.1'  # Dirección IP del servidor
PORT = 65432        # Puerto del servidor

# Crear socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# Enviar mensaje
mensaje = "Hola, servidor!"
client_socket.sendall(mensaje.encode())

# Recibir respuesta
respuesta = client_socket.recv(1024)
print(f"Respuesta del servidor: {respuesta.decode()}")

client_socket.close()
