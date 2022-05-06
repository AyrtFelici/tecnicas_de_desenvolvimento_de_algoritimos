import time
import math
while True:
    tinta= float(input("qual o tamanho de metros quadrados que você quer\n"))
    litros=tinta/3
    lata= math.ceil(litros/18)
    preço= lata*80
    print("o preço é", preço)
    print("você terá de comprar", lata,"de tinta")

    cont=input("deseja realizar outra operação \n y-sim n-não\n")
    if (cont=='y'):
        print ("reiniciando")
        print("================")
        time.sleep(1)
    elif(cont=="n"):
        print("fechando programa")
        print("==============")
        time.sleep(1)
        break





