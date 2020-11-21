import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # sock.SOCK_DGRAM
# direccion y puerto
s.connect(("192.168.1.70", 1337))
# declaras string binario b"" y el mandas la informacion
# \n ->  new line
# \r ->  retorno de carro para decir nueva linea igual
# es el equivalente de http a dar 2 enters. por que \r\n\r\n
s.send(b'GET / HTTP/1.1\r\n\r\n')
# recebir los datos recibe 1024 bytes
data = s.recv(1024)
print(data)
s.close()
