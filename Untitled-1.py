

import math

lados=0
lado1=0
lado2=0
lado3=0

opcion=0
area=0
perimetro=0


historial = []

while True:

    lados = int(input("¿Cuantos lados tiene la figura?: "))

    if lados != 3:
        print("La figura no es un triangulo vualve a ingresar los datos")
    else:
        lado1 = float(input("Ingrese el lado 1: "))
        lado2 = float(input("Ingrese el lado 2: "))
        lado3 = float(input("Ingrese el lado 3: "))

        if lado1 == lado2 == lado3:
            print("el triangulo es un Equilatero")
        elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
            print("el triangulo es un Isosceles")
        else:
            print("el triangulo es un Escaleno")

    print("1.calcular el area del triangulo")  
    print("2.calcular el perimetro del triangulo")  
    print("3. ninguna ")  

    opcion=input("¿que opcion necesita saber?")

    if opcion =="1":

        s=(lado1 + lado2 + lado3) / 2
        area=math.sqrt()



           
        
