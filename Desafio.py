import textwrap


def menu():
    menu = """\n
   ================ MENU ================
    [d]\Depositar
    [s]\Sacar
    [e]\Extrato
    [q]\Sair
    
    
    => """
    return input(textwrap.dedent(menu))


saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("Informe o valor do deposito: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
            
        else:
            print("Operacao falhou! O valor informado é invalido")
            
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        
        excedeu_saldo = valor > saldo
        
        excedeu_limite = valor > limite
        
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Operacao invalida! Voce nao tem saldo sufuciente. ")
            
        elif excedeu_limite:
            print("Operacao invalida! Voce excedeu o limite. ")
            
        elif excedeu_saques:
            print("Operacao invalida! Voce excedeu o limite de saque. ")
            
        elif valor > 0:
            saldo += valor
            extrato += f"Saques: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Operacao falhou! O valor informado é invalido. ")
            
            

       
            
        
    
                      
        
    
    
    
  





