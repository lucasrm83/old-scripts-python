import socket
def Servidor():
    name2 = ("Cliente: ")
    host = "127.0.0.1"
    port = 5000
     
    mySocket = socket.socket()
    mySocket.bind((host,port))
     
    mySocket.listen(1)
    conn, addr = mySocket.accept()
    print ("Conexão de: " + str(addr))
    while True:
            data = conn.recv(1024).decode()
            if data == "usr":
                data = conn.recv(1024).decode()
                name2 = data+": "
            print (name2 + str(data))
            msg = input("Mensagem: ")
            msg = str(msg)
            conn.send(msg.encode())
            if msg == ("usr"):
                    username = input("Novo nome: ")
                    conn.send(username.encode())
             
    conn.close()
import socket
 
def Cliente():
        name = ("Servidor: ")
        host = '127.0.0.1'
        port = 5000
         
        mySocket = socket.socket()
        mySocket.connect((host,port))
         
        message = ''
         
        while message != 'q':
                message = input("Digite a msg: ")
                mySocket.send(message.encode())
                if message == ("usr"):
                    username = input("Novo nome: ")
                    mySocket.send(username.encode())  
                data = mySocket.recv(1024).decode()
                if data == "usr":
                    data = mySocket.recv(1024).decode()
                    name = data+": "
                print (name + data)   
                    
        mySocket.close()
        
 



while True:
    print("[1] cliente")
    print("[2] servidor")
    op = input("opção: ")
    if op == '1':
        Cliente()
    if op == '2':
        Servidor()
    else:
        break
        