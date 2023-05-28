estoque = {}

def adicionar_item(nome, quantidade, preco):
    if nome not in estoque:
        estoque[nome] = {
            'quantidade': quantidade,
            'preco': preco
        }
        print("Item adicionado ao estoque com sucesso!")
    else:
        print("Item já existe no estoque.")

def remover_item(nome):
    if nome in estoque:
        del estoque[nome]
        print("Item removido do estoque com sucesso!")
    else:
        print("Item não encontrado no estoque.")

def atualizar_item(nome, quantidade, preco):
    if nome in estoque:
        estoque[nome]['quantidade'] = quantidade
        estoque[nome]['preco'] = preco
        print("Item atualizado no estoque com sucesso!")
    else:
        print("Item não encontrado no estoque.")

def pesquisar_item(nome):
    if nome in estoque:
        item = estoque[nome]
        print(f"Item: {nome}")
        print(f"Quantidade: {item['quantidade']}")
        print(f"Preço: {item['preco']}")
    else:
        print("Item não encontrado no estoque.")

def listar_itens():
    print("--- Lista de Itens no Estoque ---")
    if len(estoque) == 0:
        print("Estoque vazio.")
    else:
        for nome, detalhes in estoque.items():
            print(f"Item: {nome}")
            print(f"Quantidade: {detalhes['quantidade']}")
            print(f"Preço: {detalhes['preco']}")
            print()

def calcular_valor_total():
    total = 0
    for detalhes in estoque.values():
        quantidade = detalhes['quantidade']
        preco = detalhes['preco']
        total += quantidade * preco
    print(f"Valor total do estoque: R$ {total:.2f}")

def exibir_itens_quantidade_abaixo(valor):
    print(f"--- Itens com Quantidade Abaixo de {valor} ---")
    encontrou = False
    for nome, detalhes in estoque.items():
        quantidade = detalhes['quantidade']
        if quantidade < valor:
            print(f"Item: {nome}")
            print(f"Quantidade: {quantidade}")
            print(f"Preço: {detalhes['preco']}")
            print()
            encontrou = True
    if not encontrou:
        print("Nenhum item encontrado com quantidade abaixo do valor especificado.")

def vender_item(nome, quantidade):
    if nome in estoque:
        item = estoque[nome]
        if quantidade <= item['quantidade']:
            item['quantidade'] -= quantidade
            print(f"Venda de {quantidade} unidades do item '{nome}' realizada com sucesso!")
        else:
            print("Quantidade insuficiente no estoque para realizar a venda.")
    else:
        print("Item não encontrado no estoque.")

while True:
    print("\n--- Gerenciador de Estoque ---")
    print("1. Adicionar item")
    print("2. Remover item")
    print("3. Atualizar item")
    # ...resto das opções...

    print("0. Sair do programa")  # Adicionando a opção de sair

    opcao = input("Escolha uma opção: ")

    if opcao == "0":
        print("Programa encerrado.")
        break  # Sai do loop while

    elif opcao == "1":
        nome = input("Nome do item: ")
        quantidade = int(input("Quantidade: "))
        preco = float(input("Preço: "))
        adicionar_item(nome, quantidade, preco)

    elif opcao == "2":
        nome = input("Nome do item: ")
        remover_item(nome)

    elif opcao == "3":
        nome = input("Nome do item: ")
        quantidade = int(input("Quantidade: "))
        preco = float(input("Preço: "))
        atualizar_item(nome, quantidade, preco)

    # ...resto das opções...

    else:
        print("Opção inválida. Tente novamente.")