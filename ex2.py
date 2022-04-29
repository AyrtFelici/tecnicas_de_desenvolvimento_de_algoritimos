
import time

class init:
    def step(self):
        while True:
            print ("escoilha qual calculo você quer fazer")
            a= int(input("1-soma 2-subtração 3-divisão 4-multiplicação\n:"))

            if(a==1):self.soma()
            if(a==2):self.subtracao()
            if(a==3):self.divisao()
            if(a==4):self.multi()

            cont=str(input("deseja realizar outra operação?\n: y-sim n-não\n:"))
            if(cont=="y"):
                print ("reiniciando")
                print("================")
                time.sleep(1)
            elif(cont=="n"):
                print("fechando programa")
                print("==============")
                time.sleep(1)
                break





    def soma(self):
            soma1= float(input("digite valor 1\n:"))
            soma2= float(input("digite valor 2\n:"))
            calculo= float(soma1+soma2)
            print (f"esse é o resultado do calculo\n:{calculo}")

    def subtracao(self):
        sub1=float(input("digite o primeiro valor\n:"))
        sub2=float(input("digite o segundo valor\n:"))
        calculo=float(sub1-sub2)
        print(f"esse e o resultado do calculo\n:{calculo}")

    def divisao(self):
        div1=float(input("digite o primeiro valor\n:"))
        div2=float(input("digite o segundo valor\n:"))
        calculo=float(div1/div2)
        print(f"esse é o resultado\n:{calculo}")

    def multi(self):
        mul1= float(input("digite o primeiro valor\n:"))
        mul2= float(input("digite o segundo valor\n:"))
        calculo=float(mul1*mul2)
        print(f"esse é o resultado\n:{calculo}")






start=init()
start.step()

            
