print()
print()
print('********************* Calculdora em Python *********************')
print()
print('Selecione a operação desejada:')
print()
print('1 - Soma')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão')
print()

def soma(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def multiplicacao(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    return num1 / num2

while True:

    opcao = int(input('Digite sua opção (1/2/3/4): '))

    if (opcao in [1, 2, 3, 4]):
        break

    print('Opção inválida, digite 1, 2, 3 ou 4')
    print() 

print()
num1 = float(input('Digite o primeiro valor: '))
num2 = float(input('Digite o segundo valor: '))
print()

if (opcao == 1):
    print(f'{num1} + {num2} = {soma(num1, num2)}')

elif (opcao == 2):
    print(f'{num1} - {num2} = {subtracao(num1, num2)}')

elif (opcao == 3):
    print(f'{num1} * {num2} = {multiplicacao(num1, num2)}')

else:
    print(f'{num1} / {num2} = {divisao(num1, num2)}')

  

