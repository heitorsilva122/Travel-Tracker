COTACAO_IENE_DOLAR = 0.00620644
COTACAO_IENE_REAL = 0.032206
LIMITE_PARA_IMPORTAR = 1000
rodando = True
lista_importacao = []
lista_consumo = []

def ler_sim_nao():
    opcao = ler_item("")
    while opcao != "s" and opcao != "n":
        print("\nOpção inválida\n")
        opcao = ler_item("")
    print()
    return opcao


def validar_min_max(min, max, mensagem = "Escolha uma opção: "):
    opcao = ler_inteiro(mensagem)
    while opcao > max or opcao < min:
        print("\nOpção inválida\n")
        opcao = ler_inteiro(mensagem)
    print()
    return opcao


def converter_iene_real(preco_iene):
    preco_real = preco_iene * COTACAO_IENE_REAL
    return preco_real


def converter_iene_dolar(preco_iene):
    preco_dolar = preco_iene * COTACAO_IENE_DOLAR
    return preco_dolar


def ler_item(mensagem="Digite o item: "):
    item = input(mensagem)
    item = item.strip().lower()
    return item


def ler_inteiro(mensagem="Digite uma entrada válida"):
    while True:
        try:
            num = int(input(mensagem))
            return num
        except ValueError:
            print("\nEntrada inválida. Digite um número válido\n")


def ler_float(mensagem="Digite um Valor válido"):
    while True:
        try:
            preco = float(input(mensagem).replace(",", "."))
            if preco < 0:
                print("\nInsira um valor maior ou igual a 0\n")
            else:
                return preco
        except ValueError:
            print("\nEntrada inválida. Insira um valor válido\n")


def pausa_menu():
    input("\nAperte ENTER para voltar ao menu:")
    print()


def calcular_saldo_importacao():
    total_gasto = 0

    for item in lista_importacao:
        total_gasto += item["preco_dolar"]

    saldo_restante = LIMITE_PARA_IMPORTAR - total_gasto

    return saldo_restante


def calcular_total_importacao():
    total_gasto_iene = 0
    total_gasto_dolar = 0
    total_gasto_real = 0

    for importado in lista_importacao:
        total_gasto_dolar += importado["preco_dolar"]
        total_gasto_iene += importado["preco_iene"]
        total_gasto_real += importado["preco_real"]

    return total_gasto_iene, total_gasto_dolar, total_gasto_real


def calcular_total_consumo():
    total_gasto_iene = 0
    total_gasto_real = 0

    for consumido in lista_consumo:
        total_gasto_iene += consumido["preco_iene"]
        total_gasto_real += consumido["preco_real"]

    return total_gasto_iene, total_gasto_real


def achar_indice(lista, item):
    for i in range(len(lista)):
        if item == lista[i]["item"]:
            return i
    return -1


def remover_importacao_por_indice(i):
    lista_importacao.pop(i)
    print("Item removido da lista de importação")


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
    print("8 - Verificar total gasto")
    print("9 - Cotação atual")
    print("10 - Sair\n")

    opcao = validar_min_max(1, 10, "Escolha uma opção: ")
    return opcao


def adicionar_importacao():
    while True:
        item = ler_item("Digite o item ou aperte ENTER para finalizar: ")
        print()
        if item == "":
            break

        preco_iene = ler_float("Qual o preço desse item(em ¥): ")
        preco_dolar = converter_iene_dolar(preco_iene)
        preco_real = converter_iene_real(preco_iene)
        saldo_atual = calcular_saldo_importacao()
        print()

        if preco_dolar <= saldo_atual:
            dic_importacao = {
                "item": item,
                "preco_iene": preco_iene,
                "preco_dolar": preco_dolar,
                "preco_real": preco_real
            }
            lista_importacao.append(dic_importacao)
        else:
            print(
                "Esse item ultrapassa o limite de US$1000 e não foi adicionado à lista\n")


def adicionar_consumo():
    while True:
        # adicionando o item na lista
        item = ler_item("Digite o item que foi consumido ou aperte ENTER para finalizar: ")
        if item == "":
            break
        preco_iene = ler_float("Qual foi o preço(em ¥): ")
        preco_real = converter_iene_real(preco_iene)
        print()
        dic_consumo = {
            "item": item,
            "preco_iene": preco_iene,
            "preco_real": preco_real
        }
        lista_consumo.append(dic_consumo)


def pesquisar_item():
    achou_imp = False
    achou_con = False
    item = ler_item("Qual item deseja pesquisar: ")
    print()

    i = achar_indice(lista_importacao, item)
    if i != -1:
        print(f"{item} foi encontrado e é um item de importação")
        achou_imp = True

    i = achar_indice(lista_consumo, item)
    if i != -1:
        print(f"{item} foi encontrado e foi um item consumido")
        achou_con = True

    if not (achou_imp or achou_con):
        print(f"{item} não foi encontrado no sistema")
    pausa_menu()


def remover_item():
    print("Deseja remover um item da lista de importação ou consumo (digite 1 para importação e 2 para consumo): ")
    impcon = validar_min_max(1, 2, "Escolha uma opção: ")
    if impcon == 1:
        item = ler_item("Qual item deseja remover: ")
        i = achar_indice(lista_importacao, item)
        if i != -1:
            lista_importacao.pop(i)
            print(f"\n{item} removido com sucesso da lista de importação")
        else:
            print(f"\n{item} não foi encontrado")
    elif impcon == 2:
        item = ler_item("Qual item deseja remover: ")
        i = achar_indice(lista_consumo, item)
        if i != -1:
            lista_consumo.pop(i)
            print(f"\n{item} removido com sucesso da lista de consumo")
        else:
            print(f"\n{item} não foi encontrado")
    pausa_menu()


def editar_item():
    print("Deseja editar um item da lista de importação ou consumo (digite 1 para importação e 2 para consumo): ")
    impcon = validar_min_max(1, 2, "Escolha uma opção: ")
    if impcon == 1:
        item = ler_item("Qual item deseja editar: ")
        i = achar_indice(lista_importacao, item)
        if i != -1:
            preco_novo = ler_float(
                "Item encontrado, qual o novo preço(em ¥): ")
            saldo_restante = calcular_saldo_importacao()
            preco_novo_dolar = converter_iene_dolar(preco_novo)
            preco_antigo_dolar = lista_importacao[i]["preco_dolar"]
            diferenca_preco = preco_novo_dolar - preco_antigo_dolar
            if diferenca_preco <= saldo_restante:
                preco_novo_real = converter_iene_real(preco_novo)
                lista_importacao[i]["preco_iene"] = preco_novo
                lista_importacao[i]["preco_dolar"] = preco_novo_dolar
                lista_importacao[i]["preco_real"] = preco_novo_real
                print(
                    f"\nO preço de {item} foi alterado para ¥{preco_novo:.0f} com sucesso da lista de importação")
            else:
                print("\nO novo preço ultrapassa os US$1000")
                print("Deseja remover esse item? (s/n) ")
                remov = ler_sim_nao()
                if remov == "s":
                    remover_importacao_por_indice(i)
                elif remov == "n":
                    print("O preço do item não foi removido e nem alterado")
        else:
            print(f"\n{item} não foi encontrado")
    elif impcon == 2:
        item = ler_item("Qual item deseja editar: ")
        i = achar_indice(lista_consumo, item)
        if i != -1:
            preco_novo = ler_float(
                "\nItem encontrado, qual o novo preço(em ¥): ")
            lista_consumo[i]["preco_iene"] = preco_novo
            preco_novo_real = converter_iene_real(preco_novo)
            lista_consumo[i]["preco_real"] = preco_novo_real
            print(
                f"\nO preço de {item} foi alterado para ¥{preco_novo} com sucesso da lista de consumo")
        else:
            print(f"\n{item} não foi encontrado")
    pausa_menu()


def listar_itens():
    print("=" * 50)
    print("         ITENS PARA IMPORTAR PARA O BRASIL")
    print("=" * 50)
    if not lista_importacao:
        print("\nNenhum item de importação cadastrado\n")
    else:
        for importado in lista_importacao:
            print(f"\nVocê comprou {importado['item']}, e custou:")
            print(f"¥{importado['preco_iene']:.0f}")
            print(f"R${importado['preco_real']:.2f}")
            print(f"US${importado['preco_dolar']:.2f}")

    print("=" * 50)
    print("            ITENS DE CONSUMO NO JAPÃO")
    print("=" * 50)
    if not lista_consumo:
        print("\nNenhum item de consumo cadastrado")
    else:
        for consumido in lista_consumo:
            print(f"\nVocê consumiu {consumido['item']}, e custou:")
            print(f"¥{consumido['preco_iene']:.0f}")
            print(f"R${consumido['preco_real']:.2f}")
    pausa_menu()


def saldo_restante_importacao():
    saldo_restante = calcular_saldo_importacao()
    print(
        f"Você ainda pode gastar US${saldo_restante:.2f}, ou ¥{saldo_restante / COTACAO_IENE_DOLAR:.0f}")
    pausa_menu()


def verificar_total_gasto():
    gasto_total_real_imp = 0
    gasto_total_dolar_imp = 0
    gasto_total_iene_imp = 0
    gasto_total_real_con = 0
    gasto_total_iene_con = 0
    importacao_vazia = False
    consumo_vazio = False
    print("=" * 50)
    print("             Total gasto em importação")
    print("=" * 50)
    if not lista_importacao:
        print("\nVocê não gastou nada em itens para importação\n")
        importacao_vazia = True
    else:
        gasto_total_iene_imp, gasto_total_dolar_imp, gasto_total_real_imp = calcular_total_importacao()

        print(f"\nTotal gasto em ¥{gasto_total_iene_imp:.0f}")
        print(f"\nTotal gasto em US${gasto_total_dolar_imp:.2f}")
        print(f"\nTotal gasto em R${gasto_total_real_imp:.2f}\n")

    print("=" * 50)
    print("             Total gasto em consumo")
    print("=" * 50)

    if not lista_consumo:
        print("\nVocê não gastou nada em itens para consumo")
        consumo_vazio = True
    else:
        gasto_total_iene_con, gasto_total_real_con = calcular_total_consumo()

        print(f"\nTotal gasto em ¥{gasto_total_iene_con:.0f}")
        print(f"\nTotal gasto em R${gasto_total_real_con:.2f}")

    if not consumo_vazio or not importacao_vazia:
        print()

        gasto_total_real = gasto_total_real_con + gasto_total_real_imp
        gasto_total_iene = gasto_total_iene_con + gasto_total_iene_imp

        print("=" * 50)
        print("                  Total gasto")
        print("=" * 50)
        print(f"\nTotal gasto em ¥{gasto_total_iene:.0f}")
        print(f"\nTotal gasto em R${gasto_total_real:.2f}")
        print(
            f"\nTotal gasto em US${gasto_total_dolar_imp:.2f} (apenas os preços de importação foram considerados)")

    pausa_menu()


def cotacao_atual():
    print("=" * 50)
    print("             COTAÇÃO ¥ ---> US$")
    print("=" * 50)
    print("\nA cotação atual de ¥ para US$ é de", COTACAO_IENE_DOLAR)
    print(f"¥100 é igual a US${COTACAO_IENE_DOLAR * 100:.2f}")
    print(
        f"\nVocê pode gastar até aproximadamente ¥{LIMITE_PARA_IMPORTAR / COTACAO_IENE_DOLAR:.0f} em produtos para levar para o Brasil\n")

    print("=" * 50)
    print("             COTAÇÃO ¥ ---> R$")
    print("=" * 50)
    print("\nA cotação atual de ¥ para R$ é de", COTACAO_IENE_REAL)
    print(f"¥100 é igual a R${COTACAO_IENE_REAL * 100:.2f}")
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
        verificar_total_gasto()

    elif opcao == 9:
        cotacao_atual()

    elif opcao == 10:
        rodando = False