from getpass4 import getpass


saldo = 0
saque = 0
limite = 500
novo_limite_saque = 0
extrato = ' '
numero_de_saques = 0
LIMITE_SAQUES = 3
novo_usuarios = [ ]


def guardar_usuarios(novo_nome, criar_senha):
    
    novo_usuarios.append([novo_nome, criar_senha])
    print(novo_usuarios)
    return novo_nome, criar_senha
   

def novo_deposito(depositar):
    global saldo
    saldo+=depositar
    
    print(f'Saldo atual da conta R$ {saldo:.2f}')
    return 

def retirar(saque_novo):
    global saldo
    saldo-=saque_novo
    

def exibir_extrato(saldo):
    return saldo

def new_opcoes():
    return new_opcoes

def login ():    
    while True:

        novas_opcoes = input('''
            1 - Criar conta                 
            2 -  Login
        
            Digite uma opção: ''' )

        if novas_opcoes == '1':
            novo_nome = input('Digite seu nome: ')
            criar_senha = getpass('Digite a senha: ')
        
            
            guardar_usuarios(novo_nome, criar_senha)
            
        elif novas_opcoes == '2': 
            
            nome_login = input('Digite seu nome: ')  
            senha  = getpass('Digite sua senha: ')
            i = (len(novo_usuarios)) - 1
            while i >= 0:
                if nome_login == novo_usuarios[i][0] and senha == novo_usuarios[i][1] :
                     
                    print ('logado')     
                    return new_opcoes()  
                elif nome_login is not novo_usuarios[i][0] and senha is not novo_usuarios[i][1] :
                    print('Usuário Errado')  
                    break    
                else:
                    i -= 1
                    break
                 
  
login()
def new_opcoes():
    
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
            if saque_novo < 0 or saldo < 0:
                print(' Erro ')
            if saque >= -1:
                print('Você nao tem saldo suficiente')
                break    
        elif opcao == '3':
            exibicao_saldo = exibir_extrato(saldo)    
            print(exibicao_saldo) 
        
        elif opcao == '4':
            
            break    
      
new_opcoes()
    
    
    

