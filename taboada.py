import time
while True :
    taboada = float (input("qual tabuada vc quer? \n 1- 2- 3- 4- 5- 6- 7- 8- 9- 10-\n"))
    for count in range (-10,11):
        print("%d x %d = %d" % (taboada, count, taboada*(count)))
    cont= str(input("vc quer continuar?\n y-sim n-não\n"))
    if (cont=='y'):
        print("reiniciando")
        print("===================================")
        time.sleep(1)
    elif(cont=='n'):
        print ("fechando programa")
        print("==========================")
        time.sleep(1)
        break 


