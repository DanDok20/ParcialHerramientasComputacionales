def Verificar():
    bandera = 0
    numero = 0
    while bandera == 0:
        try:
            numero = int(input(""))
            if numero == 1 or numero == 2:
                bandera = 1
            else:
                print()
                print("Digite un numero valido")
                print()
        except ValueError:
            print()
            print("Digite un numero valido")
            print()
    return numero

def Verificar_2():
    bandera = 0
    numero = 0
    while bandera == 0:
        try:
            numero = int(input(""))
            if numero > 0:
                bandera = 1
            else:
                print()
                print("Digite un numero valido")
                print()
        except ValueError:
            print()
            print("Digite un numero valido")
            print()
    return numero
t = 1
while t == 1:
    print("Bienvenido a nuestro sistema")
    print("Digite 1 para continuar o 2 para salir: ")
    opcion = Verificar()
    if opcion == 1:
        CompraTotal = []
        print("Digite su cedula: ")
        cedula = Verificar_2()
        print("Digite 1 si es estudiante, o 2 si es profesor: ")
        rol = Verificar()
        i = 1
        while i == 1:
            print("Digite el codigo del producto: ")
            codigo = Verificar_2()
            print("¿ Cuantas unidades lleva ?: ")
            und = Verificar_2()
            print("Digite el precio del producto: ")
            precio = Verificar_2()
            if rol == 1:
                descuento = (precio*und)*0.5
                lista = [descuento,codigo]
                CompraTotal.append(lista)
            else:
                descuento = (precio*und)*0.8
                lista = [descuento,codigo]
                CompraTotal.append(lista)
                
            print("Desea registrar otro producto, Digite 1 para si, 2 Para no: ")
            continuar = Verificar_2()
            if continuar == 2:
                print("")
                if rol == 1:
                    rol = "estudiante"
                else:
                    rol = "profesor"
                total = 0
                flag = 0
                print("El ",rol,"con cedula ",cedula)
                print("")
                for y in range(len(CompraTotal)):
                    for r in range(2):
                        if r == 0:
                            total+= CompraTotal[y][r]
                    print("Debe pagar $", CompraTotal[y][0],"por el producto ", CompraTotal[y][1])
                print("TOTAL :", total)
                print("")
                i = 2
            else:
                print("")
    elif opcion == 2:
        print("")
        print("Hasta pronto")
        t = 2
    else:
        print("Digito Invalido")
        print("")

