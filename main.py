import subprocess
import os

def limpiar_pantalla():
    if os.name == "nt":
        subprocess.run(["cmd", "/c", "cls"])
    else:
        subprocess.run(["clear"])
    
# UBIOCACIONES 14x25 = 350 platea, 10x25 = 250 palcos 
# ubicaciones[id_funcion] = [matriz_platea, matriz_palco]
FILAS_PLATEA = 14
FILAS_PALCO = 10
COLUMNAS = 25      
ubicaciones = [] 
########################################## CARGADO DE ARCHIVOS EN VARIABLES ######################################################################################################################
def carga_funciones():
    archivo_funcion = open("DB/funciones.txt", "r+", encoding="utf-8")
    funciones = archivo_funcion.readlines()
    archivo_funcion.close()
    return funciones
def carga_obras():    
    archivo_obras = open("DB/obras.txt", "r+", encoding="utf-8")
    obras = archivo_obras.readlines()
    archivo_obras.close()
    return obras
def carga_salas():
    archivo_salas = open("DB/salas.txt", "r+", encoding="utf-8")
    salas = archivo_salas.readlines()
    archivo_salas.close()
    return salas
def carga_socios():    
    archivo_socios = open("DB/socios.txt", "r+", encoding="utf-8")
    socios = archivo_socios.readlines()
    archivo_socios.close()
    return socios
def carga_ventas():
    archivo_ventas = open("DB/ventas.txt", "r+", encoding="utf-8")
    ventas = archivo_ventas.readlines()
    archivo_ventas.close()
    return ventas

########################################## FUNCIONES DE FUNCIONES XD ######################################################################################################################
def printear_funcion(linea):
    obras = carga_obras()
    funcion = linea.strip().split("-")
    nombre_obra = obras[int(funcion[1])].strip().split("-")[1]
    print("-"*155)
    print(f"ID:{funcion[0]} - Obra:{nombre_obra} - Fecha:{funcion[2]} - Horario:{funcion[3]} - Sala:{funcion[4]} - Precio de platea:${funcion[5]} - Precio de palco:${funcion[6]}")
    print("-"*155)
    
def listar_funciones():
    limpiar_pantalla()
    funciones = carga_funciones()
    if len(funciones) <= 1:
        print("")
        print("X ---> Upss, todavia no hay funciones registradas <--- X")
    else:
        for i in range(1, len(funciones)):
            printear_funcion(funciones[i])
        
def buscar_funcion_por_id(id):
    funciones = carga_funciones()
    if id.isdigit() == False:
        print("")
        print("X ---> Upss, solo se reciben valores numericos <--- X")
    else:
            encontrado = False
            i = 1
            while i < len(funciones) and encontrado == False:
                funcion = funciones[i].strip().split("-")
                if int(funcion[0]) == int(id):
                    printear_funcion(funciones[i])
                    encontrado = True
                i = i + 1
            if encontrado == False:
                print("")
                print("X ---> Upss, no tenemos ninguna funcion con esa ID <--- X")

def coincide(palabra, buscada):
    if len(palabra) < len(buscada):
        return False
    for i in range(len(buscada)):
        if palabra[i].upper() != buscada[i].upper():
            return False
    return True

def buscar_funcion_por_nombre(input):
    funciones = carga_funciones()
    input = input.strip().lower()
    if input == "":
        print("")
        print("X ---> Upss, no ingresaste ningun texto para buscar <--- X")
        return
    encontrado = False
    for i in range(1, len(funciones)):
        obras = carga_obras()
        funcion = funciones[i].strip().split("-")
        nombre_obra = obras[int(funcion[1])].strip().split("-")[1].lower()
        if coincide(nombre_obra, input):
            printear_funcion(funciones[i])
            encontrado = True
    if encontrado == False:
        print("")
        print("X ---> Upss, parece que no tenemos obras con ese nombre <--- X")

def listar_obras():
    obras = carga_obras()
    limpiar_pantalla()
    for i in range(1,len(obras)):
        obra = obras[i].strip().split("-")
        print("-"*155)
        print(f"ID:{obra[0]} - Nombre de la obra o espectáculo:{obra[1]}  - Genero:{obra[3]}")
        print("-"*155)
        
def listar_salas():
    salas = carga_salas()
    limpiar_pantalla()
    for i in range(1,len(salas)):
        sala = salas[i].strip().split("-")
        print("-"*155)
        print(f"ID:{sala[0]} - Descripcion:{sala[1]}")
        print("-"*155)
        
def registrar_funcion():
    funciones = carga_funciones()
    obras = carga_obras()
    salas = carga_salas()
    id_funcion = len(funciones)
    listar_obras()

    id_obra = input("Ingrese el ID de la obra: ")
    while id_obra.isdigit() == False or int(id_obra) < 1 or int(id_obra) >= len(obras):
        listar_obras()
        id_obra = input("ID invalido. Ingrese el ID de la obra: ")

    limpiar_pantalla()
    fecha = input("Ingrese la fecha (dd/mm/aaaa): ")
    while "-" in fecha or fecha.strip() == "":
        limpiar_pantalla()
        fecha = input("Formato invalido. Ingrese la fecha (dd/mm/aaaa): ")
    
    limpiar_pantalla()
    hora = input("Ingrese el horario (hh:mm): ")
    while "-" in hora or hora.strip() == "":
        limpiar_pantalla()
        hora = input("Formato invalido. Ingrese el horario (hh:mm): ")

    listar_salas()
    id_sala = input("Ingrese el ID de la sala: ")
    while id_sala.isdigit() == False or int(id_sala) < 1 or int(id_sala) >= len(salas):
        listar_salas()
        id_sala = input("ID invalido. Ingrese el ID de la sala: ")

    limpiar_pantalla()
    precio_plat = input("Ingrese el precio de platea: ")
    while precio_plat.isdigit() == False:
        limpiar_pantalla()
        precio_plat = input("Solo numeros. Ingrese el precio de platea: ")

    limpiar_pantalla()
    precio_palco = input("Ingrese el precio de palco: ")
    while precio_palco.isdigit() == False:
        limpiar_pantalla()
        precio_palco = input("Solo numeros. Ingrese el precio de palco: ")

    linea = f"{id_funcion}-{id_obra}-{fecha}-{hora}-{id_sala}-{precio_plat}-{precio_palco}"

    archivo = open("DB/funciones.txt", "a", encoding="utf-8")
    archivo.write(linea + "\n")
    archivo.close()
    funciones.append(linea + "\n")
    ubicaciones.append([crear_matriz(FILAS_PLATEA, COLUMNAS), crear_matriz(FILAS_PALCO, COLUMNAS)])
    limpiar_pantalla()
    print("Funcion registrada con exito")

# METODO BURBUJA -- ORDENAMIENTO DE MENOR A MAYOR (ALFABETICAMENMTE)
def ordenar_funciones_por_nombre_de_obras():
    funciones = carga_funciones()
    obras = carga_obras()
    copia = funciones[1:]
    for i in range(len(copia) - 1):
        for j in range(len(copia) - 1 - i):
            funcion_A = copia[j].strip().split("-")
            funcion_B = copia[j + 1].strip().split("-")
            nombre_de_la_funcion_A = obras[int(funcion_A[1])].strip().split("-")[1].lower()
            nombre_de_la_funcion_B = obras[int(funcion_B[1])].strip().split("-")[1].lower()
            if nombre_de_la_funcion_A > nombre_de_la_funcion_B:
                auxiliar = copia[j]
                copia[j] = copia[j + 1]
                copia[j + 1] = auxiliar
    for i in range(len(copia)):
        printear_funcion(copia[i])

# TRATAR AL RESULTDAO IF buscar_indice_funcion(id_buscado) == -1 : NO ENCONTRADO
def buscar_indice_funcion(id_buscado):
    funciones = carga_funciones()
    i = 1
    while i < len(funciones):
        funcion = funciones[i].strip().split("-")
        if int(funcion[0]) == id_buscado:
            return i
        i = i + 1
    return -1
########################################## UBICACIONES ##############################################################################################################################################
def crear_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(0)
        matriz.append(fila)
    return matriz

#sector 1=platea 2=palco
def obtener_matriz(id_funcion, sector):
    return ubicaciones[id_funcion - 1][int(sector) - 1]

def numero_valido(matriz, numero):
    if numero >= 1 and numero <= len(matriz) * COLUMNAS:
        return True
    else:
        return False

def esta_disponible(matriz, numero):
    fila = (numero - 1) // COLUMNAS
    columna = (numero - 1) % COLUMNAS
    return matriz[fila][columna] == 0

def marcar_vendida(matriz, numero):
    fila = (numero - 1) // COLUMNAS
    columna = (numero - 1) % COLUMNAS
    matriz[fila][columna] = 1

def contar_estado(matriz, estado):
    cantidad = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == estado:
                cantidad = cantidad + 1
    return cantidad

def mostrar_ubicaciones(matriz):
    numero = 1
    for i in range(len(matriz)):
        linea = ""
        for j in range(len(matriz[i])):
            if matriz[i][j] == 0:
                linea = linea + str(numero).ljust(5)
            else:
                linea = linea + "XX".ljust(5)
            numero = numero + 1
        print(linea)
    print("XX = vendida")
    
#una matriz de platea y una de palco por cada funcion con la cantidad de filas y columnas ya definidas (ESTAN AL PRINCIPIO)
def cargar_ubicaciones():
    funciones = carga_funciones()
    for i in range(1, len(funciones)):
        ubicaciones.append([crear_matriz(FILAS_PLATEA, COLUMNAS), crear_matriz(FILAS_PALCO, COLUMNAS)])
    ventas = carga_ventas()
    for i in range(1, len(ventas)):
        venta = ventas[i].strip().split("-")
        matriz = obtener_matriz(int(venta[1]), venta[2])
        for ubicacion in venta[3].split(","):
            marcar_vendida(matriz, int(ubicacion))

def consultar_ubicaciones():
    limpiar_pantalla()
    
    id_pedido = input("ID de la funcion: ")
    if id_pedido.isdigit() == False:
        print("")
        print("X ---> Upss, solo se reciben valores numericos <--- X")
        return
    
    if buscar_indice_funcion(int(id_pedido)) == -1:
        print("")
        print("X ---> Upss, no tenemos ninguna funcion con esa ID <--- X")
        return

    sector = input("Sector (1-Platea, 2-Palco): ")
    if sector != "1" and sector != "2":
        print("")
        print("X ---> Upss, sector invalido <--- X")
        return

    matriz = obtener_matriz(int(id_pedido), sector)
    limpiar_pantalla()
    mostrar_ubicaciones(matriz)
    print("Disponibles:", contar_estado(matriz, 0), "- Vendidas:", contar_estado(matriz, 1))



########################################## PILA (ESTRUCTURA DINAMICA OBLIGATORIA) ##############################################################################################################
# UN nodo es [dato, siguiente]
def pila_vacia(tope):
    return tope == None

def apilar(tope, dato):
    return [dato, tope] # el nuevo nodo apunta al tope anterior

# devuelve el dato sacado y el nuevo tope
def desapilar(tope):
    if tope == None:
        return None, None# caso limite: pila vacia
    return tope[0], tope[1]

def pila_contiene(tope, dato):
    actual = tope
    while actual != None:
        if actual[0] == dato:
            return True
        actual = actual[1]
    return False


##########################################        VENTAS       ########################################################################################################
def es_socio(dni):
    socios = carga_socios()
    for i in range(1, len(socios)):
        socio = socios[i].strip().split("-")
        if socio[1] == dni:
            return True
    return False

def registrar_venta():
    limpiar_pantalla()
    funciones = carga_funciones()

    id_pedido = input("ID de la funcion: ")
    if id_pedido.isdigit() == False:
        print("")
        print("X ---> Upss, solo se reciben valores numericos <--- X")
        return
    indice = buscar_indice_funcion(int(id_pedido))
    if indice == -1:
        print("")
        print("X ---> Upss, no tenemos ninguna funcion con esa ID <--- X")
        return

    sector = input("Sector (1-Platea, 2-Palco): ")
    if sector != "1" and sector != "2":
        print("")
        print("X ---> Upss, sector invalido <--- X")
        return
    matriz = obtener_matriz(int(id_pedido), sector)

    cantidad = input("Cantidad de entradas: ")
    if cantidad.isdigit() == False or int(cantidad) < 1:
        print("")
        print("X ---> Upss, cantidad invalida <--- X")
        return
    cantidad = int(cantidad)
    if cantidad > contar_estado(matriz, 0):
        print("")
        print("X ---> Upss, no hay tantas ubicaciones disponibles <--- X")
        return

    #usamos la setruictura dinamica para las ubicaciones elegidas
    elegidas= None
    cantidad_elegidas= 0
    limpiar_pantalla()
    matriz = obtener_matriz(int(id_pedido),sector)
    mostrar_ubicaciones(matriz)
    while cantidad_elegidas < cantidad:
        numero= input("Numero de ubicacion (0 para deshacer la ultima): ")
        if numero == "0":
            if pila_vacia(elegidas):
                print("No hay ubicaciones para deshacer")
            else:
                quitada, elegidas = desapilar(elegidas)
                cantidad_elegidas = cantidad_elegidas - 1
                print("Se quito la ubicacion", quitada)
        elif numero.isdigit()==False:
            print("Solo numeros")
        elif numero_valido(matriz, int(numero))== False:
            print("Esa ubicacion no existe")
        elif esta_disponible(matriz, int(numero))== False:
            print("Esa ubicacion ya esta vendida")
        elif pila_contiene(elegidas, int(numero)):
            print("Ya la elegiste")
        else:
            elegidas = apilar(elegidas, int(numero))
            cantidad_elegidas = cantidad_elegidas + 1

    # extraerprecio segun el sector
    funcion = funciones[indice].strip().split("-")
    if sector == "1":
        precio= int(funcion[5])
    else:
        precio =int(funcion[6])

    dni = input("Dni del comprador: ")
    while dni.isdigit() == False:
        dni = input("Solo numeros. Dni del comprador: ")
    descuento = 0
    if es_socio(dni):
        descuento = 0.30
        print("El comprador es Socio: 30% de descuento aplicado")
    importe =precio * cantidad
    importe =round(importe -(importe* descuento))

    #recien ahora las saca de la pila y se marcan como vendidas las ubis
    texto_ubicaciones =""
    while pila_vacia(elegidas) == False:
        numero, elegidas = desapilar(elegidas)
        marcar_vendida(matriz, numero)
        if texto_ubicaciones!= "":
            texto_ubicaciones = texto_ubicaciones + ","
        texto_ubicaciones = texto_ubicaciones + str(numero)

    codigo = len(carga_ventas())
    linea = f"{codigo}-{id_pedido}-{sector}-{texto_ubicaciones}-{cantidad}-{precio}-{descuento}-{importe}-{dni}"
    archivo = open("DB/ventas.txt", "a", encoding="utf-8")
    archivo.write(linea + "\n")
    archivo.close()
    print("Venta registrada. Importe final: $", importe)
##########################################        INFORMES       ########################################################################################################

def informe_cantidad_vendidas_por_funcion(id_funcion):
        
    ventas = carga_ventas()    
    cant_platea = 0
    cant_palco = 0
    
    if id_funcion.isdigit() == False:
        print("")
        print("X ---> Upss, solo se reciben valores numericos <--- X")
        return
    
    if buscar_indice_funcion(int(id_funcion)) == -1:
        print("")
        print("X ---> Upss, no tenemos ninguna funcion con esa ID <--- X")
        return
    
    for i in range(len(ventas)):
        venta = ventas[i].strip().split("-")
        if venta[1] == id_funcion:
            if venta[2] == "1":#es platea
                cant_platea = cant_platea + int(venta[4])
            elif venta[2] == "2":#es palco
                 cant_palco =  cant_palco + int(venta[4])
    
    print(f"Entradas vendidas en platea: {cant_platea} \nEntradas vendidas en palco: {cant_palco}")
    return


def informe_recaudacion_funcion():
    listar_funciones()
    print("")
    
    id_pedido = input("ID de la funcion: ")
    if id_pedido.isdigit() == False:
        print("")
        print("X ---> Upss, solo se reciben valores numericos <--- X")
        return
    
    ventas = carga_ventas()
    total = 0
    cant_ventas =0
    for i in range(1,len(ventas)):
        venta = ventas[i].strip().split("-")
        id_funcion = venta[1]
        total_importe = int(venta[7])
        if id_funcion == id_pedido:
            total += total_importe
            cant_ventas += 1
            
    if cant_ventas == 0:
        print("")
        print("X ---> Upss, no hay ventas registradas para esta función <--- X")
        return
    else:
        print("-"*155)
        print(f"Ventas realizadas: {cant_ventas}")
        print(f"Recaudacion de la funcion: ${total}")

#RECURSIVO OBLIGATORIO
def sumar_importes(ventas, i):
    if i >= len(ventas):# PASO base: no quedan ventas
        return 0
    venta = ventas[i].strip().split("-")
    return int(venta[7]) + sumar_importes(ventas, i + 1)#PASO recursivo

def informe_recaudacion_total():
    ventas = carga_ventas()
    total = sumar_importes(ventas, 1)
    
    if total == 0:
        print("")
        print("X ---> Upss, todavia no hay ventas registradas <--- X")
        return
    else:
        print("-"*155)
        print(f"Recaudacion total distribuida entre todas las funciones: ${total}")

def informe_funcion_mas_vendida():
    funciones = carga_funciones()
    ventas = carga_ventas()
    if len(ventas) <= 1:
        print("")
        print("X ---> Upss, todavia no hay ventas registradas <--- X")
        return

    id_mas_vendida = 0
    max_entradas = 0
    for i in range(1, len(funciones)):
        funcion = funciones[i].strip().split("-")
        id_funcion = funcion[0]
        entradas = 0
        for j in range(1, len(ventas)):
            venta = ventas[j].strip().split("-")
            if venta[1] == id_funcion:
                entradas += int(venta[4])
        if entradas > max_entradas:
            max_entradas = entradas
            id_mas_vendida = id_funcion

    print("-"*155)
    print(f"Funcion con mas entradas vendidas: id {id_mas_vendida}")
    print(f"Entradas vendidas: {max_entradas}")
    
def informe_cantidad_ubicaciones_disp_funcion(id_funcion):
    ventas = carga_ventas()    
    cant_platea = 0
    cant_palco = 0
    
    if id_funcion.isdigit() == False:
        print("")
        print("X ---> Upss, solo se reciben valores numericos <--- X")
        return
    
    if buscar_indice_funcion(int(id_funcion)) == -1:
        print("")
        print("X ---> Upss, no tenemos ninguna funcion con esa ID <--- X")
        return
    
    for i in range(len(ventas)):
        venta = ventas[i].strip().split("-")
        if venta[1] == id_funcion:
            if venta[2] == "1":#es platea
                cant_platea = cant_platea + int(venta[4])
            elif venta[2] == "2":#es palco
                 cant_palco =  cant_palco + int(venta[4])
    
    cant_platea = 350 - cant_platea
    cant_palco = 250 - cant_palco
    print(f"Cantidad de ubicaciones disponibles en platea: {cant_platea} \nCantidad de ubicaciones disponibles en palco: {cant_palco}")
    return



#######################################            MENUES             #################################################
def menu_consultas():    
    opcion = ""

    while opcion != "7":
        limpiar_pantalla()
        print("\n======================================")
        print("        Teatro CaPaz S.A.")
        print("======================================")
        print("1. Cantidad de entradas vendidas para una función.")
        print("2. Cantidad de ubicaciones disponibles para una función.")
        print("3. Informe de recaudación total de una función.")
        print("4. Informe de recaudación total de todas las funciones.")
        print("5. Listado de funciones ordenado según un criterio de demanda.")
        print("6. Identificación de la función con mayor cantidad de entradas vendidas.")
        print("7. Salir.")  
        print("======================================")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_funcion = input("Ingrese el ID de la funcion que desea saber la cantidad de entradas vendidas: ")
            informe_cantidad_vendidas_por_funcion(id_funcion)
            input("\nPresione Enter para continuar...")
        elif opcion == "2":
            id_funcion = input("Ingrese el ID de la funcion que desea saber la cantidad de lugares disponibles: ")
            informe_cantidad_ubicaciones_disp_funcion(id_funcion)
            input("\nPresione Enter para continuar...")
        elif opcion == "3":
            informe_recaudacion_funcion()
            input("\nPresione Enter para continuar...")
        elif opcion == "4":
            informe_recaudacion_total()
            input("\nPresione Enter para continuar...")
        elif opcion == "5":
            input("\nPresione Enter para continuar...")
        elif opcion == "6":
            informe_funcion_mas_vendida()
            input("\nPresione Enter para continuar...")
        elif opcion != "7":
            limpiar_pantalla()
            print("Opción incorrecta. Intente nuevamente.")

def menu_funciones():
    opcion = ""

    while opcion != "6":
        limpiar_pantalla()
        print("\n======================================")
        print("        Teatro CaPaz S.A.")
        print("======================================")
        print("1. Registrar una nueva funcion")
        print("2. Consultar funciones registradas")
        print("3. Buscar funcion por ID")
        print("4. Buscador de funciones por nombre")
        print("5. Ordenar funciones por nombre de obra")
        print("6. Salir")
        print("======================================")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_funcion()
            input("\nPresione Enter para continuar...")

        elif opcion == "2":
            listar_funciones()
            input("\nPresione Enter para continuar...")
        elif opcion == "3":
            id_pedido = input("Ingrese el ID de la funcion que desea visualizar: ")
            buscar_funcion_por_id(id_pedido)
            input("\nPresione Enter para continuar...")
        elif opcion == "4":
            nombre_pedido = input("Ingrese el nombre o fragmento de nombre de la funcion que desea visualizar: ")            
            buscar_funcion_por_nombre(nombre_pedido)
            input("\nPresione Enter para continuar...")
        elif opcion == "5":
            ordenar_funciones_por_nombre_de_obras()
            input("\nPresione Enter para continuar...")
        elif opcion != "6":
            limpiar_pantalla()
            print("Opción incorrecta. Intente nuevamente.")

def menu():
    opcion = ""
    
    while opcion != "5":
        limpiar_pantalla()
        print("\n======================================")
        print("        Teatro CaPaz S.A.")
        print("======================================")
        print("1. Administrar Funciones")
        print("2. Consultar ubicaciones de una sección de la función")
        print("3. Realizar una venta")
        print("4. Consultas y reportes")
        print("5. Salir")
        print("======================================")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_funciones()
        elif opcion == "2":
            consultar_ubicaciones()
            input("\nPresione Enter para continuar...")
        elif opcion == "3":
            registrar_venta()
            input("\nPresione Enter para continuar...")
        elif opcion == "4":
            menu_consultas()
            input("\nPresione Enter para continuar...")
        elif opcion == "5":
            print("Gracias por utilizar el sistema.")

        else:
            print("Opción incorrecta. Intente nuevamente.")
            input("\nPresione Enter para continuar...")
cargar_ubicaciones()
menu()