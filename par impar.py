print('Informe 10 numeros: ')
a = int(input('numero 1: '))
b = int(input('numero 2: '))
c = int(input('numero 3: '))
d = int(input('numero 4: '))
e = int(input('numero 5: '))
f = int(input('numero 6: '))
g = int(input('numero 7: '))
h = int(input('numero 8: '))
i = int(input('numero 9: '))
j = int(input('numero 10: '))
ctp = 0
cti = 0
while True:
    if a % 2 == 0:
        print(a, 'é par')
        ctp = ctp + 1
    else:
        print(a, 'é impar')
        cti = cti + 1
    if b % 2 == 0:
        print(b, 'é par')
        ctp = ctp + 1
    else:
        print(b, 'é impar')
        cti = cti + 1
    if c % 2 == 0:
        print(c, 'é par')
        ctp = ctp + 1
    else:
        print(c, 'é impar')
        cti = cti + 1
    if d % 2 == 0:
        print(d, 'é par')
        ctp = ctp + 1
    else:
        print(d, 'é impar')
        cti = cti + 1
    if e % 2 == 0:
        print(e, 'é par')
        ctp = ctp + 1
    else:
        print(e, 'é impar')
        cti = cti + 1
    if f % 2 == 0:
        print(f, 'é par')
        ctp = ctp + 1
    else:
        print(f, 'é impar')
        cti = cti + 1
    if g % 2 == 0:
        print(g, 'é par')
        ctp = ctp + 1
    else:
        print(g, 'é impar')
        cti = cti + 1
    if h % 2 == 0:
        print(h, 'é par')
        ctp = ctp + 1
    else:
        print(h, 'é impar')
        cti = cti + 1
    if i % 2 == 0:
        print(i, 'é par')
        ctp = ctp + 1
    else:
        print(i, 'é impar')
        cti = cti + 1
    if j % 2 == 0:
        print(j, 'é par')
        ctp = ctp + 1
    else:
        print(j, 'é impar')
        cti = cti + 1
    print('Total de numeros pares: ', ctp)
    print('Total de numeros impares: ', cti)
    break
