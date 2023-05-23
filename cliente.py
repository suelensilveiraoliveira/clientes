import csv
clientes = []


def carrega_dados():
    with open('clientes.csv', mode='r', encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for linha in csv_reader:
            clientes.append(linha)

def titulo(msg, traco="-"):
    print()
    print(msg)
    print(traco*40)

def salvar():
    with open('clientes.csv', mode='w', encoding="utf-8", newline="") as csv_file:
        colunas = ['nome', 'idade', 'cidade', 'sexo']
        writer = csv.DictWriter(csv_file, fieldnames=colunas)
        writer.writeheader() 

        #percorre a lista de dicionarios e salva os dados
        for cliente in clientes:
            writer.writerow(cliente)
    
    

def incluir():
    titulo("Incluir Cliente")
    nome = input("Nome do cliente: ")
    idade= input("Idade do Cliente: ")
    cidade = input("Cidade: ")
    sexo = input("sexo: ")
    clientes.append({"nome": nome, "idade": idade, "cidade": cidade, "sexo": sexo})
    
    
    print("Ok! Cliente cadastrado com sucesso.")


def listar_clientes():
    for cliente in clientes:
        nome = cliente.get('nome')
        idade = cliente.get('idade')
        cidade = cliente.get('cidade')
        sexo = cliente.get('sexo')
        print(f"Nome: {nome}\nIdade: {idade}\nCidade: {cidade}\nSexo: {sexo}\n")

def alterar_cliente():
    titulo("Alterar Cliente")
    nome_antigo = input("Nome do cliente a ser alterado: ")
    novo_nome = input("Novo nome do cliente: ")
    nova_idade = input("Nova idade do cliente: ")
    novo_cidade = input("Nova cidade do cliente: ")
    
    for cliente in clientes:
        if cliente['nome'] == nome_antigo:
            cliente['nome'] = novo_nome
            cliente['idade'] = nova_idade
            cliente['cidade'] = novo_cidade
            print("Ok! Cliente alterado com sucesso.")
            return
    
    print("Cliente não encontrado.")


def excluir():
    titulo("Excluir Cliente")
    nome_excluir = input("Nome do cliente a ser excluído: ")

    for cliente in clientes:
        if cliente['nome'] == nome_excluir:
            clientes.remove(cliente)
            print("Ok! Cliente excluído com sucesso.")
            return

    print("Cliente não encontrado.")

def pesquisar_clientes_por_nome():
    titulo("Pesquisar Cliente por Nome")
    nome_pesquisar = input("Digite o nome do cliente: ")
    
    clientes_encontrados = []
    for cliente in clientes:
        if cliente['nome'].lower() == nome_pesquisar.lower():
            clientes_encontrados.append(cliente)
    
    if clientes_encontrados:
        titulo("Clientes Encontrados")
        for cliente in clientes_encontrados:
            nome = cliente.get('nome')
            idade = cliente.get('idade')
            cidade = cliente.get('cidade')
            print(f"Nome: {nome}\nIdade: {idade}\nCidade: {cidade}\n")
    else:
        print("Nenhum cliente encontrado com o nome especificado.")

def pesquisar_clientes_por_cidade():
    titulo("Pesquisar Cliente por Cidade")
    cidade_pesquisar = input("Digite o nome da cidade: ")
    
    clientes_encontrados = []
    for cliente in clientes:
        if cliente['cidade'].lower() == cidade_pesquisar.lower():
            clientes_encontrados.append(cliente)
    
    if clientes_encontrados:
        titulo("Clientes Encontrados")
        for cliente in clientes_encontrados:
            nome = cliente.get('nome')
            idade = cliente.get('idade')
            cidade = cliente.get('cidade')
            print(f"Nome: {nome}\nIdade: {idade}\nCidade: {cidade}\n")
    else:
        print("Nenhum cliente encontrado na cidade especificada.")

def ordenar_clientes_decrescente():
    titulo("Ordenar Clientes por Ordem Decrescente")
    clientes_ordenados = sorted(clientes, key=lambda cliente: cliente['nome'].lower(), reverse=True)
    
    titulo("Clientes Ordenados por Ordem Decrescente")
    for cliente in clientes_ordenados:
        nome = cliente.get('nome')
        idade = cliente.get('idade')
        cidade = cliente.get('cidade')
        print(f"Nome: {nome}\nIdade: {idade}\nCidade: {cidade}\n")

def listar_maiores_de_idade():
    titulo("Listar Clientes Maiores de Idade")
    for cliente in clientes:
        idade = int(cliente.get('idade'))
        if idade > 18:
            nome = cliente.get('nome')
            idade = cliente.get('idade')
            cidade = cliente.get('cidade')
            print(f"Nome: {nome}\nIdade: {idade}\nCidade: {cidade}\n")




carrega_dados()


while True:
    titulo("Lista de clientes", "=")
    print("1. incluir clientes")
    print("2. Listar clientes")
    print("3. Alterar clientes")
    print("4. Excluir Cliente")
    print("5. Pesquisa por nome do cliente")
    print("6. Pesquisa por cidade do cliente")
    print("7. clientes por ordem decrescente")
    print("8. Lista de maior idade")
    print("9. Salvar")
    
   
    opcao = int(input("Opção: "))
    if opcao == 1:
        incluir()
    elif opcao == 2:
        listar_clientes()
    elif opcao == 3:
        alterar_cliente()
    elif opcao == 4:
        excluir()
    elif opcao == 5:
        pesquisar_clientes_por_nome()
    elif opcao == 6:
        pesquisar_clientes_por_cidade()
    elif opcao == 7:
        ordenar_clientes_decrescente()
    elif opcao == 8:
        listar_maiores_de_idade()
    elif opcao == 9:
        salvar()
    else:
        break
