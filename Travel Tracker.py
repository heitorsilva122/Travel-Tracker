total_gasto_iene = 0
total_gasto_dolar = 0
total_gasto_real = 0
cotação_iene_dolar = 0.00620644
cotação_iene_real = 0.032206
total_para_importar = 1000
rodando = True
lista_importação_item = []
lista_importação_preço_iene = []
lista_importação_preço_dolar = []
lista_importação_preço_real = []
lista_consumo_item = []
lista_consumo_preço_iene = []
lista_consumo_preço_real = []

while(rodando):
    add = 1
    print("Bem vindo ao Travel Tracker, escolha umas das opções abaixo")
    print("1 - Vou levar um item para o Brasil (lembrancinhas, etc)")
    print("2 - vou consumir no Japão (comida, hospedagem, etc)")
    print("3 - Listar itens")
    print("4 - verificar saldo de importação para o Brasil")
    print("5 - cotação atual")
    print("6 - Sair")

    opção = int(input("Escolha uma opção: "))

    if opção == 1:
        while add == 1:
            #adicionando o item na lista
            item = input("Qual foi o item comprado: ")
            item = item.lower()
            lista_importação_item.append(item)

            #adicionando os preços em dolar, iene e real na lista
            preço_iene = float(input("Qual o preço desse item: "))
            lista_importação_preço_iene.append(preço_iene)
            total_gasto_iene += preço_iene

            preço_dolar =  preço_iene * cotação_iene_dolar
            lista_importação_preço_dolar.append(preço_dolar)
            total_gasto_dolar += preço_dolar
            total_para_importar -= preço_dolar

            preço_real = preço_iene * cotação_iene_real
            lista_importação_preço_real.append(preço_real)
            total_gasto_real += preço_real

            add = int(input("Deseja adicionar mais um item? Digite 1 para sim ou 0 para não: "))

        print("Você comprou um total de", len(lista_importação_item), "item(s)")
        print("Sendo eles", lista_importação_item)
        print(f"Você gastou um total de {sum(lista_importação_preço_iene)} ienes")
        print(f"Você gastou um total de {sum(lista_importação_preço_dolar):.2f} dolares")
        print(f"Você gastou um total de {sum(lista_importação_preço_real):.2f} reais")
        print(f"Você ainda pode gastar {total_para_importar:.2f} dolares")

        opção = int(input("Digite 0 para voltar ao menu: "))

    elif opção == 2:
        while add == 1:
            #adicionando o item na lista
            item = input("Oque você consumiu: ")
            item = item.lower()
            lista_consumo_item.append(item)

            #adicionando os preço em iene e real
            preço_iene = float(input("qual foi o preço: "))
            lista_consumo_preço_iene.append(preço_iene)
            total_gasto_iene += preço_iene

            preço_real = preço_iene * cotação_iene_real
            lista_consumo_preço_real.append(preço_real)
            total_gasto_real += preço_real

            add = int(input("Deseja adicionar mais um item? Digite 1 para sim ou 0 para não: "))
        
        print("Você consumiu um total de", len(lista_consumo_item), "coisas")
        print("Sendo elas", lista_consumo_item)
        print(f"Você gastou um total de {sum(lista_consumo_preço_iene)} ienes")
        print(f"Você gastou um total de {sum(lista_consumo_preço_real):.2f} reais")
        opção = int(input("Digite 0 para voltar ao menu: "))
    elif opção == 3:
        for i in range(len(lista_importação_item)):
            print(f"Você comprou {lista_importação_item[i]}, e custou:")
            print(f"{lista_importação_preço_iene[i]} ienes")
            print(f"{lista_importação_preço_real[i]:.2f} reais")
            print(F"{lista_importação_preço_dolar[i]:.2f} dolares")
        for j in range(len(lista_consumo_item)):
            print(f"Você consumiu {lista_consumo_item[j]}, e custou:")
            print(f"{lista_consumo_preço_iene[j]} ienes")
            print(f"{lista_consumo_preço_real[j]:.2f} reais")
        opção = int(input("Digite 0 para voltar ao menu: "))
    elif opção == 4:
        print(f"Você ainda pode gastar {total_para_importar:.2f} dolares")
        opção = int(input("Digite 0 para voltar ao menu: "))
    elif opção == 5:
        print("A cotação atual de ieen para dolar é de", cotação_iene_dolar)
        print(f"100 iene é igual a {cotação_iene_dolar * 100:.2f} dolares")
        print(f"Você pode gaster até aproximadamente {1000 / cotação_iene_dolar:.2f} ienes em produtos para levar para o Brasil")
        print("A cotação atual de iene para real é de", cotação_iene_real)
        print(f"100 iene é igual a {cotação_iene_real * 100:.2f} reais")
        opção = int(input("Digite 0 para voltar para o menu: "))
    elif opção == 6:
        rodando = False