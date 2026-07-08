cotacao_iene_dolar = 0.00620644
cotacao_iene_real = 0.032206
limite_para_importar = 1000
rodando = True
lista_importacao_item = []
lista_importacao_preco_iene = []
lista_importacao_preco_dolar = []
lista_importacao_preco_real = []
lista_consumo_item = []
lista_consumo_preco_iene = []
lista_consumo_preco_real = []

def converter_iene_real(preco_iene):
    preco_real = preco_iene * cotacao_iene_real
    return preco_real

def converter_iene_dolar(preco_iene):
    preco_dolar = preco_iene * cotacao_iene_dolar
    return preco_dolar

def ler_item(mensagem = "Digite o item: "):
    item = input(mensagem)
    item = item.strip().lower()
    return item

def ler_inteiro(mensagem = "Digite uma entrada válida"):
    while True:
        try:
            num = int(input(mensagem))
            return num
        except ValueError:
            print("\nEntrada inválida. Digite um número válido\n")

def ler_float(mensagem = "Digite um Valor válido"):
    while True:
        try:
            preco = float(input(mensagem).replace(",", "."))
            if preco < 0:
                print("Insira um valor maior ou igual a 0")
            else:
                return preco
        except ValueError:
            print("\nEntrada inválida. Insira um valor válido\n")

def pausa_menu():
    input("\nAperte ENTER para voltar ao menu:")
    print()

def calcular_saldo_importacao():
    saldo_restante = limite_para_importar - sum(lista_importacao_preco_dolar)
    return saldo_restante

def achar_indice(lista, item):
    for i in range(len(lista)):
        if item == lista[i]:
            return i
    return -1

def menu():
    print("=" * 50)
    print("             Bem vindo ao Travel Tracker!\n            Escolha uma das opções abaixo")
    print("=" * 50)
    print()
    print("1 - Vou levar um item para o Brasil (lembrancinhas, etc)")
    print("2 - Vou consumir no Japão (comida, hospedagem, etc)")
    print("3 - Pesquisar item")
    print("4 - Remover item")
    print("5 - Editar item")
    print("6 - Listar itens")
    print("7 - Verificar saldo de importação para o Brasil")
    print("8 - Cotação atual")
    print("9 - Sair\n")

    opcao = ler_inteiro("Escolha um opção: ")
    while opcao > 9 or opcao < 1:
        print("\nOpção Inválida\n")
        opcao = ler_inteiro("Escolha um opção: ")
    print()
    return opcao

def adicionar_importacao():
    while True:
        item = ler_item("Digite o item ou aperte ENTER para finalizar: ")
        if item == "":
            break

        preco_iene = ler_float("Qual o preço desse item(em ¥): ")
        preco_dolar = converter_iene_dolar(preco_iene)
        saldo_atual = calcular_saldo_importacao()
        
        if preco_dolar <= saldo_atual:
            lista_importacao_preco_dolar.append(preco_dolar)

            lista_importacao_preco_iene.append(preco_iene)
            
            lista_importacao_item.append(item)

            preco_real = converter_iene_real(preco_iene)
            lista_importacao_preco_real.append(preco_real)
        else:
            print("Esse item ultrapassa o limite de US$1000 e não foi adicionado à lista")

    print("\nVocê comprou um total de", len(lista_importacao_item), "item(s)")
    print("Sendo eles", lista_importacao_item)
    print()
    print("Nessas compras você gastou um total de:")
    print(f"¥{sum(lista_importacao_preco_iene)}")
    print("Ou")
    print(f"US${sum(lista_importacao_preco_dolar):.2f}")
    print("Ou")
    print(f"R${sum(lista_importacao_preco_real):.2f}\n")
    print(f"Você ainda pode gastar US${calcular_saldo_importacao():.2f}")
    pausa_menu()

def adicionar_consumo():
    while True:
        # adicionando o item na lista
        item = ler_item("Digite o item que foi consumido ou aperte ENTER para finalizar: ")
        if item == "":
            break
        lista_consumo_item.append(item)

        # adicionando os preço em iene e real
        preco_iene = ler_float("Qual foi o preço(em ¥): ")
        lista_consumo_preco_iene.append(preco_iene)

        preco_real = converter_iene_real(preco_iene)
        lista_consumo_preco_real.append(preco_real)


    print("\nVocê consumiu um total de", len(lista_consumo_item), "coisas")
    print("Sendo elas", lista_consumo_item)
    print()
    print("Nessas compras você gastou um total de:")
    print(f"¥{sum(lista_consumo_preco_iene)}")
    print("Ou")
    print(f"R${sum(lista_consumo_preco_real):.2f}")
    pausa_menu()

def pesquisar_item():   
    achou_imp = False
    achou_con = False
    item = ler_item("Qual item deseja pesquisar: ")
    print()

    i = achar_indice(lista_importacao_item, item)
    if i != -1:
        print(f"{item} foi encontrado e é um item de importação\n")
        achou_imp = True

    i = achar_indice(lista_consumo_item, item)
    if i != -1:
        print(f"{item} foi encontrado e foi um item consumido\n")
        achou_con = True

    if not (achou_imp or achou_con):
        print(f"{item} não foi encontrado no sistema")
    pausa_menu()

def remover_item():
    impcon = ler_inteiro("Deseja remover um item da lista de importação ou consumo (digite 1 para importação e 2 para consumo): ")
    while impcon != 1 and impcon != 2:
        print("\nOpção Inválida\n")
        impcon = ler_inteiro("Escolha um opção: ")
        print()
    if impcon == 1:
        item = ler_item("Qual item deseja remover: ")
        i = achar_indice(lista_importacao_item, item)
        if i != -1:
            lista_importacao_item.pop(i)
            lista_importacao_preco_dolar.pop(i)
            lista_importacao_preco_iene.pop(i)
            lista_importacao_preco_real.pop(i)
            print(f"\n{item} removido com sucesso da lista de importação")
        else:
            print(f"\n{item} não foi encontrado")
    elif impcon == 2:
        item = ler_item("Qual item deseja remover: ")
        i = achar_indice(lista_consumo_item, item)
        if i != -1:
            lista_consumo_item.pop(i)
            lista_consumo_preco_iene.pop(i)
            lista_consumo_preco_real.pop(i)
            print(f"\n{item} removido com sucesso da lista de consumo")
        else:
            print(f"\n{item} não foi encontrado")
    else:
        print("\nOpção Inválida\n")
    pausa_menu()

def editar_item():
    impcon = ler_inteiro("Deseja editar um item da lista de importação ou consumo (digite 1 para importação e 2 para consumo): ")
    while impcon != 1 and impcon != 2:
        print("\nOpção Inválida\n")
        impcon = ler_inteiro("Escolha um opção: ")
        print()
    if impcon == 1:
        item = ler_item("Qual item deseja editar: ")
        i = achar_indice(lista_importacao_item, item)
        if i != -1:
            preco_novo = ler_float("Item encontrado, qual o novo preço(em ¥): ")
            saldo_restante = calcular_saldo_importacao()
            preco_novo_dolar = converter_iene_dolar(preco_novo)
            preco_antigo_dolar = lista_importacao_preco_dolar[i]
            diferenca_preco = preco_novo_dolar - preco_antigo_dolar
            if diferenca_preco <= saldo_restante:
                preco_antigo = lista_importacao_preco_iene[i]
                lista_importacao_preco_iene[i] = preco_novo
                preco_novo_real = converter_iene_real(preco_novo)
                lista_importacao_preco_dolar[i] = preco_novo_dolar
                lista_importacao_preco_real[i] = preco_novo_real
                print(f"\n o preço de {item} foi editado, de ¥{preco_antigo} para ¥{preco_novo} com sucesso da lista de importação")
            else:
                print("O novo preço ultrapassa os US$1000, por favor use a função de remover itens para remove-lo")
        else:
            print(f"\n{item} não foi encontrado")
    elif impcon == 2:
        item = ler_item("Qual item deseja editar: ")
        i = achar_indice(lista_consumo_item, item)
        if i != -1:
            preco_novo = ler_float("\nItem encontrado, qual o novo preço(em ¥): ")
            preco_antigo = lista_consumo_preco_iene[i]
            lista_consumo_preco_iene[i] = preco_novo
            preco_novo_real = converter_iene_real(preco_novo)
            lista_consumo_preco_real[i] = preco_novo_real 
            print(f"\n o preço de {item} foi editado, de ¥{preco_antigo}  para ¥{preco_novo} com sucesso da lista de consumo")
        else:
            print(f"\n{item} não foi encontrado")
    else:
        print("\nOpção Inválida\n")
    pausa_menu()

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
        print(f"R${lista_consumo_preco_real[j]:.2f}")
    pausa_menu()

def saldo_restante_importacao():
    saldo_restante = calcular_saldo_importacao()
    print(f"Você ainda pode gastar US${saldo_restante:.2f}, ou ¥{saldo_restante / cotacao_iene_dolar:.0f}\n")
    pausa_menu()

def cotacao_atual():
    print("=" * 50)
    print("             COTAÇÃO ¥ ---> US$")
    print("=" * 50)
    print("\nA cotação atual de ¥ para US$ é de", cotacao_iene_dolar)
    print(f"¥100 é igual a US${cotacao_iene_dolar * 100:.2f}")
    print(f"\nVocê pode gastar até aproximadamente ¥{limite_para_importar / cotacao_iene_dolar:.0f} em produtos para levar para o Brasil\n")

    print("=" * 50)
    print("             COTAÇÃO ¥ ---> R$")
    print("=" * 50)
    print("\nA cotação atual de ¥ para R$ é de", cotacao_iene_real)
    print(f"¥100 é igual a R${cotacao_iene_real * 100:.2f}")
    pausa_menu()

while (rodando):
    opcao = menu()

    if opcao == 1:
        adicionar_importacao()

    elif opcao == 2:
        adicionar_consumo()

    elif opcao == 3:
        pesquisar_item()

    elif opcao == 4:
        remover_item()

    elif opcao == 5:
        editar_item()

    elif opcao == 6:
        listar_itens()

    elif opcao == 7:
        saldo_restante_importacao()

    elif opcao == 8:
        cotacao_atual()

    elif opcao == 9:
        rodando = False