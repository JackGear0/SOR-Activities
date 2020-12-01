def loops(item, QTDE, QTDS, Saldo, Preço, Subtotal):
    print("|{: ^23}|{: ^14}|{: ^12}|{: ^15}|{: ^16}|{: ^10}|".format(item, QTDE, QTDS, Saldo , Preço, Subtotal))

item=['Azeite de Oliva', 'Castanha do Pará', 'Flocos de Aveia', 'Paçoca de Amendoim', 'Panetone sem Gluten', 'Pão Sirio Integral', 'Polpa de Açai Natural', 'Queijo Vegano']
qtde=['100', '100', '200', '100', '100', '100', '100', '100',]
qtds=['40', '5', '800', '8', '60', '70', '1', '30']
Saldo=['60', '95', '10', '92', '40', '30', '99', '70']
preço=['21,90', '6,00', '90', '1,50', '17,30', '5,90', '7,10', '25,00']
subtotal=['1.314,0', '300,00', '872,00', '30,00', '692,00', '177,00', '639,00', '1.750,00' ]
print("◸{}|{}|{}|{}|{}|{}◹".format("—" * 23, "—" * 14, "—" * 12, "—" * 15,"—" * 16, "—" * 9))
print("| Lista de Produtos     | QTD Entradas | QTD Saidas | Saldo Estoque | Preço Unitário | SubTotal |")
x=0
while x < 8:
    print("|{}|{}|{}|{}|{}|{}|".format("—" * 23, "—" * 14, "—" * 12, "—" * 15,"—" * 16, "—" * 10))
    loops(item[x], qtde[x], qtds[x], Saldo[x], preço[x], subtotal[x])
    x+=1
print("|{}|\n|{:>95}|\n◺{}◿".format("—" * 95, "TOTAL: 5.774,00 ", "—" * 94)) 