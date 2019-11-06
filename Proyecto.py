def menu():
    while True:
        print ("Menú \n")
        print ("1. Registrar Producto.")
        print ("2. Mostrar Catálogo.")
        print ("3. Facturar Compra.")
        print ("4. Salir del programa. \n")
        x= int (input ("Elija un número para ejecutar una acción.\n \n"))

        if x==1:
            registrar()
            
            

        if x==2:
            print("Mostrar Catálogo.")
            mostrar()

        if x==3:
            BuscarCodigo()

def BuscarCodigo():
    print("************************************************************************\n")
    print("Bienvenido al sistema de facturacion\n")
    codigoFactura = input ("Digite el codigo del producto: ")
    archivo3 = open("Ejemplo.txt","r")
    for lineaFactura in archivo3.readlines():
        cod = lineaFactura.split()
        if codigoFactura == cod[0]:
            print("************************************************************************\n")
            print("FACTURAR")
            print("Codigo Nombre Precio Cantidad\n")
            print(cod[0]+"  "+cod[1]+"  "+cod[2]+"  0\n")
            cantidad = input ("Digite la cantidad de " +cod[1] +" que desea facturar: ")
            precio = (int(cod[2]) * int(cantidad))
            print(cod[0]+"  "+cod[1]+"  "+str(precio)+"  "+ cantidad)
            opcion = int(input ("Es correcta la informacion, 0 si, 1 no: "))
            if opcion == 0:
                total = int(cantidad) * int(cod[2])
                print("El total a cancelar sin impuesto es: " + str(total))
                impuesto = (total * 0.13)
                print("El impuesto de la compra es: " + str(impuesto))
                print("Total final: " + str(total + impuesto))
                input ("Digite cualquier tecla para regresar al menu principal")
                
            else:
                BuscarCodigo()            
    archivo3.close()
    
    

def registrar():
    codigo = input ("Digite el codigo del producto.\n")
    nombre = input ("Digite el nombre del producto.\n")
    precio = input ("Digite el precio del producto.\n")
    cantidad = int (input ("Digite la cantidad de productos.\n"))

    archivo2 = open("Ejemplo.txt","r")
    for linea in archivo2.readlines():
        cod = linea[:3]
        if codigo == cod:
            partir = linea.split()
            entero = int (partir[3])
            cantidad = entero + cantidad
            print(entero)
            #Aqui quede
            archivo2.close()
            menu()
    archivo = open("Ejemplo.txt", "a+")
    archivo.write(codigo + " " + nombre + " " + precio + " " +cantidad + '\n')
    archivo.close()
            
            
            

    
    

def mostrar():
    archivo2 = open("Ejemplo.txt","r")
    print("Codigo" + "  " + "Nombre" + "  "+"Precio"+"  " + "Cantidad")
    for linea in archivo2.readlines():
        print(linea)
    archivo2.close()
    

    
    



menu()


