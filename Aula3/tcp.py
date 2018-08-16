#!/usr/bin/python
import socket
conexao=socket.socket(socket.AF_INET,
socket.SOCK_STREAM)
host=''
port=15000

msg = "Teste de Socket"

conexao.bind((host, port))
conexao.listen(10)

while True:
    con, cliente = conexao.accept()
    print("Conectado por", cliente)
    con.send(msg.encode('ascii'))
    con.close()