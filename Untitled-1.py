import math

print(" :v CLASIFICADOR DE TRIÁNGULOS :v ")

historial = []  
tipo=0
lados=0
l1=0
l2=0
l3=0
opciones=0
perimetro=0
area=0
registro=0
resultado=0

while True:

    print("\n")

    opciones = input("1. Nueva consulta\n2. Ver historial\n3. Salir\nSeleccione una opcion: ")

    if opciones == "3":
        print("Gracias por usar el clasificador de triangulos")
        break
    
    if opciones == "2":

        print("\n**** HISTORIAL DE CONSULTAS ****")
        if not historial:
            print("No hay consultas.")

        else:
            for item in historial:
                print(f"• {item}")
        

    if opciones == "1":
        lados = int(input("\n¿Cuántos lados tiene la figura?: "))
        
        if lados != 3:
            print("\nLos datos ingresasor no pertenecen a un triangulo.")
            print("\nvuelve a intentarlo")
            

        l1 = float(input("Lado 1: "))
        l2 = float(input("Lado 2: "))
        l3 = float(input("Lado 3: "))


        if l1 == l2 == l3:
            tipo = "Equilátero"
        elif l1 == l2 or l1 == l3 or l2 == l3:
            tipo = "Isósceles"
        else:
            tipo = "Escaleno"
        
        print("\nEs un triángulo: ",tipo)

        perimetro = l1 + l2 + l3
        s = perimetro / 2
        area = math.sqrt