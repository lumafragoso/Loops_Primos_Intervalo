divisor = 0
primos = 0
condicao = True
while condicao:
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))
    if n1 > n2:
        print('Digite n1 e n2 tal que n2 > n1')
        condicao = True
    elif n2 > n1:
        for i in range(n1, n2):
            divisor = 0
            for j in range(1, n2 + 1):
                if i % j == 0:
                    divisor = divisor + 1
            if divisor == 2:
                primos = primos + 1
    print('Existem {} numeros primos entre {} e {}'.format(primos, n1, n2))
    condicao = False
