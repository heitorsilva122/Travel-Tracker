cotacao_iene_dolar = 0.00620644
cotacao_iene_real = 0.032206
total_para_importar = 1000
rodando = True
lista_importacao_item = []
lista_importacao_preco_iene = []
lista_importacao_preco_dolar = []
lista_importacao_preco_real = []
lista_consumo_item = []
lista_consumo_preco_iene = []
lista_consumo_preco_real = []


def menu():
    print("=" * 50)
    print("             Bem vindo ao Travel Tracker!\n            Escolha uma das opções abaixo")
    print("=" * 50)
    print()
    print("1 - Vou levar um item para o Brasil (lembrancinhas, etc)")
    print("2 - vou consumir no Japão (comida, hospedagem, etc)")
    print("3 - Pesquisar item")
    print("4 - Remover item")
    print("5 - Editar item")
    print("6 - Listar itens")
    print("7 - verificar saldo de importação para o Brasil")
    print("8 - cotação atual")
    print("9 - Sair\n")

    opcao = int(input("Escolha uma opção: "))
    print()
    return opcao


def adicionar_importacao(total_para_importar):
    add = 1
    total_gasto_iene = 0
    total_gasto_real = 0
    total_gasto_dolar = 0
    while add == 1:
        # adicionando o item na lista
        item = input("Qual foi o item comprado: ")
        item = item.lower()
        lista_importacao_item.append(item)

        # adicionando os preços em dolar, iene e real na lista
        preco_iene = float(input("Qual o preço desse item: "))
        lista_importacao_preco_iene.append(preco_iene)
        total_gasto_iene += preco_iene

        preco_dolar = preco_iene * cotacao_iene_dolar
        lista_importacao_preco_dolar.append(preco_dolar)
        total_gasto_dolar += preco_dolar
        total_para_importar -= preco_dolar

        preco_real = preco_iene * cotacao_iene_real
        lista_importacao_preco_real.append(preco_real)
        total_gasto_real += preco_real

        add = int(
            input("Deseja adicionar mais um item? Digite 1 para sim ou 0 para não: "))

    print("\nVocê comprou um total de", len(lista_importacao_item), "item(s)")
    print("Sendo eles", lista_importacao_item)
    print()
    print("Nessas compras você gastou um total de:")
    print(f"¥{sum(lista_importacao_preco_iene)}")
    print("Ou")
    print(f"US${sum(lista_importacao_preco_dolar):.2f}")
    print("Ou")
    print(f"R${sum(lista_importacao_preco_real):.2f}\n")
    print(f"Você ainda pode gastar US${total_para_importar:.2f}")
    print()
    input("Aperte ENTER para voltar ao menu: ")
    return total_para_importar


def adicionar_consumo():
    add = 1
    total_gasto_iene = 0
    total_gasto_real = 0
    while add == 1:
        # adicionando o item na lista
        item = input("O que você consumiu: ")
        item = item.lower()
        lista_consumo_item.append(item)

        # adicionando os preço em iene e real
        preco_iene = float(input("qual foi o preço: "))
        lista_consumo_preco_iene.append(preco_iene)
        total_gasto_iene += preco_iene

        preco_real = preco_iene * cotacao_iene_real
        lista_consumo_preco_real.append(preco_real)
        total_gasto_real += preco_real

        add = int(
            input("Deseja adicionar mais um item? Digite 1 para sim ou 0 para não: "))

    print("\nVocê consumiu um total de", len(lista_consumo_item), "coisas")
    print("Sendo elas", lista_consumo_item)
    print()
    print("Nessas compras você gastou um total de:")
    print(f"¥{total_gasto_iene}")
    print("Ou")
    print(f"R${total_gasto_real:.2f}")
    print()
    opcao = input("Aperte ENTER para voltar ao menu: ")


def pesquisar_item():
    encontrado_importacao = False
    encontrado_consumo = False
    item = input("Qual item deseja pesquisar: ")
    item = item.lower()
    print()

    for i in lista_importacao_item:
        if i == item:
            print(f"{item} foi encontrado e é um item de importação\n")
            encontrado_importacao = True

    for j in lista_consumo_item:
        if j == item:
            print(f"{item} foi encontrado e foi um item consumido\n")
            encontrado_consumo = True

    if not (encontrado_importacao or encontrado_consumo):
        print(f"{item} não foi encontrado no sistema\n")

    input("Aperte ENTER para voltar ao menu:")

def remover_item(total_para_importar):
    removido = False
    impcon = int(input("Deseja remover um item da lista de importação ou consumo (digite 1 para importação e 2 para consumo): "))
    if impcon == 1:
        item = input("Qual item deseja remover: ")
        item = item.lower()
        for i in range(len(lista_importacao_item)):
            if lista_importacao_item[i] == item:
                lista_importacao_item.pop(i)
                aux = lista_importacao_preco_dolar[i]
                total_para_importar += aux
                lista_importacao_preco_dolar.pop(i)
                lista_importacao_preco_iene.pop(i)
                lista_importacao_preco_real.pop(i)
                print(f"\n{item} removido com sucesso da lista de importação")
                removido = True
                break
        if not removido:
            print(f"\n{item} não foi encontrado")
    elif impcon == 2:
        item = input("Qual item deseja remover: ")
        item = item.lower()
        for i in range(len(lista_consumo_item)):
            if lista_consumo_item[i] == item:
                lista_consumo_item.pop(i)
                lista_consumo_preco_iene.pop(i)
                lista_consumo_preco_real.pop(i)
                print(f"\n{item} removido com sucesso da lista de consumo")
                removido = True
                break
        if not removido:
            print(f"\n{item} não foi encontrado")
    input("\nPressione ENTER para voltar ao menu:")
    return total_para_importar

def editar_item(total_para_importar):
    encontrado = False
    impcon = int(input("Deseja editar um item da lista de importação ou consumo (digite 1 para importação e 2 para consumo): "))
    if impcon == 1:
        item = input("Qual item deseja editar: ")
        item = item.lower()
        for i in range(len(lista_importacao_item)):
            if lista_importacao_item[i] == item:
                preco_novo = float(input("Item encontrado, qual o novo preço(em ¥): "))
                preco_antigo_dolar = lista_importacao_preco_dolar[i]
                total_para_importar += preco_antigo_dolar
                preco_antigo = lista_importacao_preco_iene[i]
                lista_importacao_preco_iene[i] = preco_novo
                preco_novo_dolar = preco_novo * cotacao_iene_dolar
                preco_novo_real = preco_novo *cotacao_iene_real
                lista_importacao_preco_dolar[i] = preco_novo_dolar
                lista_importacao_preco_real[i] = preco_novo_real
                total_para_importar -= preco_novo_dolar
                print(f"\n o preço de {item} foi editado, de ¥{preco_antigo} para ¥{preco_novo} com sucesso da lista de importação")
                encontrado = True
                break
        if not encontrado:
            print(f"\n{item} não foi encontrado")
    elif impcon == 2:
        item = input("Qual item deseja editar: ")
        item = item.lower()
        for i in range(len(lista_consumo_item)):
            if lista_consumo_item[i] == item:
                preco_novo = float(input("\nItem encontrado, qual o novo preço(em ¥): "))
                preco_antigo = lista_consumo_preco_iene[i]
                lista_consumo_preco_iene[i] = preco_novo
                preco_novo_real = preco_novo * cotacao_iene_real
                lista_consumo_preco_real[i] = preco_novo_real 
                print(f"\n o preço de {item} foi editado, de ¥{preco_antigo}  para ¥{preco_novo} com sucesso da lista de consumo")
                encontrado = True
                break
        if not encontrado:
            print(f"\n{item} não foi encontrado")
    input("\nPressione ENTER para voltar ao menu:")
    return total_para_importar


def listar_itens():
    print("=" * 50)
    print("         ITENS PARA IMPORTAR PARA O BRASIL")
    print("=" * 50)
    for i in range(len(lista_importacao_item)):
        print(f"\nVocê comprou {lista_importacao_item[i]}, e custou:")
        print(f"¥{lista_importacao_preco_iene[i]}")
        print(f"R${lista_importacao_preco_real[i]:.2f}")
        print(f"US${lista_importacao_preco_dolar[i]:.2f}\n")

    print("=" * 50)
    print("            ITENS DE CONSUMO NO JAPÃO")
    print("=" * 50)
    for j in range(len(lista_consumo_item)):
        print(f"\nVocê consumiu {lista_consumo_item[j]}, e custou:")
        print(f"¥{lista_consumo_preco_iene[j]}")
        print(f"R${lista_consumo_preco_real[j]:.2f}\n")
    opcao = input("Aperte ENTER para voltar ao menu: ")


def saldo_restante_importacao(total_para_importar):
    print(f"Você ainda pode gastar US${total_para_importar:.2f}\n")
    input("Aperte ENTER para voltar ao menu: ")


def cotação_atual():
    print("=" * 50)
    print("             COTAÇÃO IENE ---> DOLAR")
    print("=" * 50)
    print("\nA cotação atual de iene para dolar é de", cotacao_iene_dolar)
    print(f"100 ienes é igual a US${cotacao_iene_dolar * 100:.2f}")
    print(
        f"\nVocê pode gastar até aproximadamente {1000 / cotacao_iene_dolar:.2f} ienes em produtos para levar para o Brasil\n")

    print("=" * 50)
    print("             COTAÇÃO IENE ---> REAL")
    print("=" * 50)
    print("\nA cotação atual de iene para real é de", cotacao_iene_real)
    print(f"100 ienes é igual a R${cotacao_iene_real * 100:.2f}\n")
    input("Aperte ENTER para voltar para o menu: ")


while (rodando):
    opcao = menu()

    if opcao == 1:
        total_para_importar = adicionar_importacao(total_para_importar)

    elif opcao == 2:
        adicionar_consumo()

    elif opcao == 3:
        pesquisar_item()

    elif opcao == 4:
        total_para_importar = remover_item(total_para_importar)

    elif opcao == 5:
        total_para_importar = editar_item(total_para_importar)

    elif opcao == 6:
        listar_itens()

    elif opcao == 7:
        saldo_restante_importacao(total_para_importar)

    elif opcao == 8:
        cotação_atual()

    elif opcao == 9:
        rodando = False
