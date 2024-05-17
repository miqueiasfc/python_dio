# Função para realizar saque
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo:
        print("Saldo insuficiente. Operação de saque não realizada.")
    elif valor > limite:
        print("Valor do saque excede o limite permitido.")
    elif numero_saques >= limite_saques:
        print("Limite de saques diários excedido.")
    else:
        saldo -= valor
        extrato.append(f"Saque: R$ {valor:.2f}")
        numero_saques += 1
        print("Saque realizado com sucesso.")
    return saldo, extrato


# Função para realizar depósito
def depositar(saldo, valor, extrato):
    saldo += valor
    extrato.append(f"Depósito: R$ {valor:.2f}")
    print("Depósito realizado com sucesso.")
    return saldo, extrato


# Função para exibir extrato
def exibir_extrato(saldo, extrato):
    print("Extrato:")
    for operacao in extrato:
        print(operacao)
    print(f"Saldo atual: R$ {saldo:.2f}")


# Função para listar usuários
def listar_usuarios(usuarios):
    print("Usuários cadastrados:")
    for usuario in usuarios:
        print(usuario)


# Função para cadastrar usuário
def cadastrar_usuario(usuarios, nome, cpf, data_nascimento, endereco):
    # Verifica se o CPF já está cadastrado
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            print("CPF já cadastrado. Não foi possível criar usuário.")
            return usuarios

    # Cria um novo usuário e adiciona à lista de usuários
    novo_usuario = {
        "nome": nome,
        "cpf": cpf,
        "data_nascimento": data_nascimento,
        "endereco": endereco
    }
    usuarios.append(novo_usuario)
    print("Usuário cadastrado com sucesso.")
    return usuarios


# Função para criar conta bancária
def criar_conta(contas, usuarios, cpf):
    # Verifica se o usuário existe
    usuario_existente = False
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            usuario_existente = True
            break

    if not usuario_existente:
        print("Usuário não encontrado. Não foi possível criar a conta.")
        return contas

    # Encontra o próximo número de conta disponível
    numero_conta = len(contas) + 1

    # Cria uma nova conta e adiciona à lista de contas
    nova_conta = {
        "agencia": "0001",
        "numero_conta": numero_conta,
        "usuario": cpf
    }
    contas.append(nova_conta)
    print("Conta criada com sucesso.")
    return contas


# Função principal
def main():
    # Listas para armazenar usuários e contas
    usuarios = []
    contas = []

    # Variáveis para controle de limite de saques diários
    numero_saques = 0
    limite_saques = 3

    # Variáveis para saldo e extrato
    saldo = 0
    extrato = []

    # Menu de opções
    while True:
        print("\nMenu:")
        print("[d] Depositar")
        print("[s] Sacar")
        print("[e] Extrato")
        print("[lu] Listar usuários")
        print("[nc] Nova conta")
        print("[lc] Listar contas")
        print("[nu] Novo usuário")
        print("[q] Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "d":
            valor = float(input("Digite o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)
        elif opcao == "s":
            valor = float(input("Digite o valor do saque: "))
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=500,
                numero_saques=numero_saques,
                limite_saques=limite_saques
            )
        elif opcao == "e":
            exibir_extrato(saldo, extrato)
        elif opcao == "lu":
            listar_usuarios(usuarios)
        elif opcao == "nc":
            cpf = input("Digite o CPF do usuário para criar a conta: ")
            contas = criar_conta(contas, usuarios, cpf)
        elif opcao == "lc":
            print("Contas cadastradas:")
            for conta in contas:
                print(conta)
        elif opcao == "nu":
            nome = input("Digite o nome do usuário: ")
            cpf = input("Digite o CPF do usuário: ")
            data_nascimento = input("Digite a data de nascimento do usuário: ")
            endereco = input("Digite o endereço do usuário: ")
            usuarios = cadastrar_usuario(usuarios, nome, cpf, data_nascimento, endereco)
        elif opcao == "q":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


if __name__ == "__main__":
    main()
