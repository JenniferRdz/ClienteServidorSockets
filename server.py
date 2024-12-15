import socket

# Configuración del servidor
HOST = '127.0.0.1'  # Dirección IP del servidor (localhost)
PORT = 65432        # Puerto de escucha

# Crear socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print("Esperando conexión del cliente...")

# Aceptar conexión del cliente
conn, addr = server_socket.accept()
print(f"Conectado con {addr}")

# Manejar mensajes
while True:
    data = conn.recv(1024)  # Recibir mensaje
    if not data:
        break
    print(f"Mensaje recibido: {data.decode()}")
    conn.sendall(b"Mensaje recibido")  # Responder al cliente

conn.close()
