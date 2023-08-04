saldo = 0
saque = 0

limite = 500
novo_limite_saque = 0
extrato = ' '
numero_de_saques = 0

LIMITE_SAQUES = 3

def novo_deposito(depositar):
    global saldo
    saldo+=depositar
    
    print(f'Saldo atual da conta R$ {saldo:.2f}')
    return 

def retirar(saque_novo):
    global saldo
    saldo-=saque_novo

while True:

    opcao = input('''
    1 - deposito
    2 - sacar
    3 - extrato
    4 - sair 
    Digite uma opção: ''')

   

    if opcao == '1':
        
        depositar = float(input('Digite o valor  que deseja depositar: R$ '))
        novo_deposito(depositar)
       
    elif depositar < 0:
        print('Digite um valor valido')  
    elif opcao == '2':
        saque_novo = float(input('Digite o valor que você deseja sacar: R$ '))
        retirar(saque_novo)
        numero_de_saques += 1
        saque += saque_novo
        novo_limite_saque = saque
        if numero_de_saques > LIMITE_SAQUES:
            print('Excedeu o número de saques')
            break
        if  novo_limite_saque > limite:
            print('Você excedeu o limite máximo de R$ 500.00')
            break
        if saque_novo < 0 and saldo < 0:
            print(' Erro ')
        if saque > saldo:
            print('Você nao tem saldo suficiente')
            break    
    elif opcao == '3':
       print(saldo) 
    
    elif opcao == '4':
        
        break    

    
    
    
    

