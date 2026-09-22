continuar = 's'

while continuar == 's':
    num1 = float(input('Digite o primeiro numero: '))
    operacao = input('Escolha a operação (+, -, *, /, **): ')
    num2 = float(input('Digite o segundo numero: '))

    if operacao == '+':
        resultado = num1 + num2
        print(f'{num1} + {num2} = {resultado}')

    elif operacao == '-':
        resultado = num1 - num2
        print(f'{num1} - {num2} = {resultado}')

    elif operacao == '*':
        resultado = num1 * num2
        print(f'{num1} * {num2} = {resultado}')

    elif operacao == '/':
        if num2 == 0:
            print('Não é possível dividir por zero')
        else:
            resultado = num1 / num2
            print(f'{num1} / {num2} = {resultado}')

    elif operacao == '**':
        resultado = num1 ** num2
        print(f'{num1} ** {num2} = {resultado:.2f}')

    else:
        print('Operação inválida')

    continuar = input('Quer fazer outra conta? (s/n): ').lower()

print('Calculadora encerrada!')