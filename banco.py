# Código de resolução do projeto de "Sistema Bancário" do bootcamp "Formação Python Developer" da DIO.me
saldo = 1000.00
opcao = -1
extrato = ''
limite = 0
while True:
    print(
"""===============ESCOLHA UMA OPÇÃO===============
1 - Deposito
2 - Saque
3 - Extrato
0 - Sair
===============================================""")
    opcao = int(input('Escolha: '))

    if opcao == 1:
        deposito = float(input(f"""===============================================
Seu saldo atual é de R$ {saldo:.2f}
Digite o valor que deseja depositar: """))
        if deposito >= 0:
            print('Depositando...')
            saldo += deposito
            extrato += f'Deposito de R$ {deposito:.2f}\n'
            print(f'Seu novo saldo é R${saldo:.2f}')
        else:
            print('Você não digitou um valor válido para depósito, tente novamente.')
    elif opcao == 2:
        saque = float(input(f"""
===============================================
Seu saldo atual é de R$ {saldo:.2f}
Digite o valor que deseja sacar: """))
        if saque > saldo:
            print("Você digitou um valor de saque maior do que o seu saldo, tente novamente.")
        elif (saque < saldo) and (limite != 3) and (saque < 500.00):
            print('Sacando...')
            saldo -= saque
            extrato += f'Saque de R$ {saque:.2f}\n'
            limite += 1
            print(f'Seu novo saldo é R${saldo:.2f}')
        elif limite == 3:
            print('Você atingiu o limite de saques diários')
        else:
            print('Você está tentando sacar mais do que o limite de R$ 500.00, tente um valor abaixo desse limite.')
    elif opcao == 3:
        print(
f"""Gerando seu extrato...
====================EXTRATO====================
Seu saldo atual é R${saldo:.2f}""")
        print(extrato)
    elif opcao == 0:
        break
    else: print('Você não digitou uma opção válida, tente novamente.') 
