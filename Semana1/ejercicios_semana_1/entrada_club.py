edad= int(input("ingrese su edad: "))
print("tiene el pase dorado? si o no")
pase= input()

if(edad >= 18):
    if(pase == "si"):
        print("puede entrar al club")
    elif(edad <= 25):
        print("puede entrar al club")
    else:
        print("no puede entrar al club")
else:
    print("no puede entrar al club")