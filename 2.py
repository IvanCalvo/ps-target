#funcao que calcula fibonacci ate o numero escolhido
def fibonacci(num):
    n0 = 0
    n1 = 1
    n2 = n1 + n0

    #caso n2 seja maior ou igual ao numero alvo, o laco para
    while n2 < num:
        n0 = n1
        n1 = n2
        n2 = n1 + n0

    if n2 == num:
        return True
    else:
        return False
    
num = int(input('Numero escolhido: '))
if fibonacci(num):
    print('Pertence')
else:
    print('Não Pertence')