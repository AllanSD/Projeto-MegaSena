#1129521 Dennis Souza/ 1130042 Allan D'ávila/ 1133577 Pedro Fanton
from random import randint

print('SORTEIO DA MEGA-SENA!\nDIGITE SEUS 6 NÚMEROS.')
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
n4 = int(input('Digite o quarto número: '))
n5 = int(input('Digite o quinto número: '))
n6 = int(input('Digite o sexto número: '))

sorteio = 0

listaEscolha = [n1, n2, n3, n4, n5, n6]
listaSorteada = []
cont = 0


while True: 
    listaSorteada=[]
    cont = 0
    while True:
        num = randint(0, 60)
        if num not in listaSorteada:
            listaSorteada.append(num)
            cont += 1
        if cont >= 6:
            break
    listaSorteada.sort()
    print(listaSorteada)

    if (listaEscolha != listaSorteada):
        sorteio += 1
        print(f'O programa rodou {sorteio} vezes.')
    else:
        print('Você foi premiado!')
        print(f'O programa rodou {sorteio} vezes.')
        break