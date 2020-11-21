import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
"""
Por que puso 0.0.0.0 en vez de ver la ipconfig?
Para escuchar por cualquier interfaz de red (hardware de red)
Solo escuchar por este puerto (1337)
"""
# eschuchar peticiones
s.bind(("0.0.0.0", 1337))
s.listen(1)
# acpetar coneccion. Regresa coneccion y direccion del cliente
conn, addr = s.accept()

with conn:
    dataFromClient = conn.recv(1024)
    print(dataFromClient)
    # enviar a la informacion el mensaje precedido de b por que son bytes
    conn.send(b"OK")
