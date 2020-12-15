# server.py
import socket
from converter import converter

# create a socket object
c= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = "127.0.0.1"
port = 5000
print("\033[1;32mESPERANDO CLIENTE\033[0;0m")
# bind to the port
c.bind((host, port))

# starts listening requests
c.listen()
while True:
    # establish a connection
    clientsocket,addr = c.accept()
    print("\033[;1m{}\nGot a connection from".format('_' * 41), str(addr), "\nCONECTADO")
    clientsocket.send("BEM VINDO AO CONVERSOR".encode('ascii'))
    while True:
        #primeira opçao receive
        a = (clientsocket.recv(1024)).decode('ascii')
        m = int(a)
        if m == 1:
            print("Opção: Dinheiro ",m)
            # segunda opçao receive
            a = (clientsocket.recv(1024)).decode('ascii')
            OP = int(a)
            if OP == 1:
                print("Real para Dolar")
                r = str(clientsocket.recv(1024).decode('ascii'))
                f = converter(OP, float(r))
                result = "R${:.2f} Em Dólar é: {:.2f} US$".format(float(r), float(f.coin()))
                clientsocket.send(result.encode())
                print("CONVERSÃO CONCLUIDA")
                print("—" * 21)

            elif OP == 2:
                print("Real para Iene")
                r = str(clientsocket.recv(1024).decode('ascii'))
                f = converter(OP, float(r))
                result = "R${:.2f} Em Iene é: {:.2f} ¥".format(float(r), float(f.coin()))
                clientsocket.send(result.encode())
                print("CONVERSÃO CONCLUIDA")
                print("—" * 21)

            elif OP == 3:
                print("Real para Peso Argentino")
                r = str(clientsocket.recv(1024).decode('ascii'))
                f = converter(OP, float(r))
                result = "R${:.2f} Em Peso Argentino é: ARS{:.2f}".format(float(r), float(f.coin()))
                clientsocket.send(result.encode())
                print("CONVERSÃO CONCLUIDA")
                print("—" * 21)

            elif OP == 4:
                clientsocket.send("OBRIGADO POR USAR".encode())
                print("CONVERSÃO CONCLUIDA")
                print("—" * 21)

        if m == 2:
            print("Opção: Velocidade ",m)
            a = (clientsocket.recv(1024)).decode('ascii')
            OP = int(a)
            print(OP)
            if OP == 1:
                print("Metros por Segundo -> Quilometro por hora")
                r = str(clientsocket.recv(1024).decode('ascii'))
                f = converter(OP, float(r))
                result = "{:.2f}ms é {:.2f} Km/h".format(float(r), float(f.speed()))
                clientsocket.send(result.encode())
                print("CONVERSÃO CONCLUIDA")
                print("—" * 21)

            elif OP == 2:
                print("Quilometro por hora -> Metros por Segundo")
                r = str(clientsocket.recv(1024).decode('ascii'))
                f = converter(OP, float(r))
                result = "{:.2f}Km/h é {:.2f} m/s".format(float(r), float(f.speed()))
                clientsocket.send(result.encode())
                print("CONVERSÃO CONCLUIDA")
                print("—" * 21)

            elif OP == 3:
                print("Quilometro por hora -> Milhas por hora")
                r = str(clientsocket.recv(1024).decode('ascii'))
                f = converter(OP, float(r))
                result = "{:.2f}Km/h é {:.2f}mph".format(float(r), float(f.speed()))
                clientsocket.send(result.encode())
                print("CONVERSÃO CONCLUIDA")
                print("—" * 21)

            elif OP == 4:
                clientsocket.send("OBRIGADO POR USAR".encode('ascii'))
                print("CONVERSÃO CONCLUIDA")
                print("—" * 21)

        if m == 3:
            print("Opção: Tempo ",m)
            a = (clientsocket.recv(1024)).decode('ascii')
            OP = int(a)
            if OP == 1:
                print("Hora -> Minuto")
                r = str(clientsocket.recv(1024).decode('ascii'))
                f = converter(OP, float(r))
                result = "{:.2f} Hora é {:.2f} Minuto(s)".format(float(r), float(f.time()))
                clientsocket.send(result.encode())
                print("CONVERSÃO CONCLUIDA")
                print("—" * 21)

            elif OP == 2:
                print("Minuto -> Hora")
                r = str(clientsocket.recv(1024).decode('ascii'))
                f = converter(OP, float(r))
                result = "{:.2f} Minuto(s) é {:.2f} Hora(s)".format(float(r), float(f.time()))
                clientsocket.send(result.encode())
                print("CONVERSÃO CONCLUIDA")
                print("—" * 21)

            elif OP == 3:
                print("Segundo -> Minuto")
                r = str(clientsocket.recv(1024).decode('ascii'))
                f = converter(OP, float(r))
                result = "{:.2f} Segundo(s) é {:.2f} Minuto(s)".format(float(r), float(f.time()))
                clientsocket.send(result.encode())
                print("CONVERSÃO CONCLUIDA")
                print("—" * 21)

            elif OP == 4:
                clientsocket.send("OBRIGADO POR USAR".encode('ascii'))
                print("CONVERSÃO CONCLUIDA")
                print("—" * 21)

        if m == 4:
            print("SAIDA")
            clientsocket.send("OBRIGADO POR USAR".encode('ascii'))
            print("CONEXÃO CONCLUIDA\n")
            print("—" * 21)
            print("\t   \033[1;31m꧁\033[1;34m꧂    \n\033[0;0m")
            clientsocket.close()
            print("\033[1;32mESPERANDO PROXIMO CLIENTE\033[0;0m")
            break