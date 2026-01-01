#Projeto de caixa eletrônico completo
import time

print('=================>Caixa eletrônico<=================')

#==========login==========

senha = '1234'

while True:
    chute=input('Digite a senha: ')

    if chute == senha:
        print('Senha correta, Acesso concedido!')
        break
    else: print('Senha incorreta, Acesso negado!')

#==========Bancário==========

saldo = 1000.00

while True:
    print(f'Seu saldo atual é {saldo:.2f}')
    print('(1)Sacar dinheiro')
    print('(2)Depositar')
    print('(3)Sair')

    opcao = input('Escolha entre as opções (1/2/3)')

    if opcao == '1':
        valor= float(input('Quanto deseja sacar? R$'))

        #verificar se tem o valor

        if valor <= saldo:
         saldo = saldo - valor

         time.sleep(3)
         print(f'Sucesso! Você sacou {valor:.2f}')
        else:
            print('Negado! saldo insuficiente.')

    elif opcao == '2':
       valor = float(input('Quanto você deseja depositar?'))
       saldo = saldo + valor
       time.sleep(3)
       print(f'Sucesso! Você depositou {valor:.2f}')

    elif opcao == '3':
        print('Fechando sistema...')
        time.sleep(3)
        print('...')
        time.sleep(2)
        break

    else:
        print('Opção inválida! Digite (1/2/3)')

    time.sleep(2)


print('Obrigado por usar nosso banco!')
