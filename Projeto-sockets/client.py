# client.py
import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port = 5000

# connection to hostname on the port.
s.connect((host, port))
print("\033[1;95m", end='')
print(s.recv(1024).decode('ascii'))



while True:
    try:
        print("\033[0;0m{}\n✿ Escolha uma opção:\n✿ 1 ⇛ Dinheiro\n✿ 2 ⇛ Velocidade\n✿ 3 ⇛ Tempo\n✿ 4 ⇛ SAIR".format("—" * 21))
        x = input("✿ Opção:")
        #primeira opçao send
        s.send(x.encode('ascii'))
        print("—" * 22)
        if x == '1':
            #Opção monetaria
            print("Conversão Monetária\n✿ Escolha uma opção:\n✿ 1 - Real -> Dolar\n✿ 2 - Real -> Iene\n✿ 3 - Real -> Peso argentino\n✿ 4 - SAIR")
            n = (input("✿ Opção: ").encode('ascii'))
            s.send(n)
            o = int(n.decode('ascii'))
            if 0 < o < 4:
                r = (input("Digite o valor em R$: ").encode('ascii'))
                s.send(r)
                msg = (s.recv(1024).decode())
                print(msg)
            elif o == 4:
                msg = (s.recv(1024).decode('ascii'))
                print("\n", msg)
            else:
                # em caso valores diferentes de 1 a 4
                print("\nColoque um valor valido")

        elif x == '2':
            # Opção De Velocidade
            print("Conversão de Velocidade\n✿ 1 - Metros por Segundo -> Quilometro por hora\n✿ 2 - Quilometro por hora -> Metros por Segundo\n✿ 3 - Quilometro por hora -> Milhas por hora\n✿ 4 - SAIR")
            n = input("✿ Opção: ").encode('ascii')
            s.send(n)
            o = int(n.decode('ascii'))
            if 0 < o < 4:
                b = int(n.decode('ascii'))
                l=['Metros por Segundo', 'Quilometro por hora', 'Quilometro por hora']
                print("Digite o valor em ", l[b-1], end='')
                r = (input(":").encode('ascii'))
                s.send(r)
                msg = (s.recv(1024).decode())
                print(msg)
            elif o == 4:
                msg = (s.recv(1024).decode('ascii'))
                print("\n", msg)
            else:
                # em caso valores diferentes de 1 a 4
                print("\nColoque um valor valido")
        elif x == '3':
            # Opção de tempo
            print("✿ Escolha uma opção:\n✿ 1 - Hora -> Minuto\n✿ 2 - Minuto -> Hora\n✿ 3 - Segundo -> Minuto\n✿ 4 - SAIR")
            n = input("✿Opção: ").encode('ascii')
            s.send(n)
            o = int(n.decode('ascii'))
            if 0 < o < 4:
                b = int(n.decode('ascii'))
                l = ['Hora', 'Minuto', 'Segundo']
                print("Digite o valor em ", l[b - 1], end='')
                r = (input(":").encode('ascii'))
                s.send(r)
                msg = (s.recv(1024).decode())
                print(msg)
            elif o == 4:
                msg = (s.recv(1024).decode('ascii'))
                print("\n", msg)
            else:
                # em caso valores diferentes de 1 a 4
                print("\nColoque um valor valido")
        elif x == '4':
            # SAIDA
            print("Saindo")
            s.send(x.encode('ascii'))
            f = (s.recv(1024).decode('ascii'))
            s.close()
            print(f)
            print("—" * 22)
            break
        else:
            #em caso de erro
            print("\nColoque um valor valido")
    except:
        print("Algum erro ocorreu, retornando")

from tkinter import *

OPTIONS = ["⭐","⭐⭐","⭐⭐⭐","⭐⭐⭐⭐","⭐⭐⭐⭐⭐"]
master = Tk()
text = Label(master,text="Como voce avaliaria esse programa??")
text["font"] = ("Arial", "10")
variable = StringVar(master)
variable.set(OPTIONS[0]) # default value
w = OptionMenu(master, variable, *OPTIONS)
text.pack()
master.geometry("250x80")
w.pack()

def ok():
    print ("Sua avaliação foi:\033[1;32m" + variable.get())
    print("\033[0;0m")

button = Button(master, text="OK", command=lambda:[ok(),master.quit()])
button.pack()

mainloop()
print("\t    \033[1;31m꧁\033[1;34m꧂    \n\n\n\033[0;0m")