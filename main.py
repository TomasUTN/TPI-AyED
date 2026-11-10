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
ubicaciones = [None] 
########################################## CARGADO DE ARCHIVOS EN VARIABLES ##########################################
archivo_funcion = open("DB/funciones.txt", "r+", encoding="utf-8")
funciones = archivo_funcion.readlines()
archivo_funcion.close()
archivo_obras = open("DB/obras.txt", "r+", encoding="utf-8")
obras = archivo_obras.readlines()
archivo_obras.close()
archivo_salas = open("DB/salas.txt", "r+", encoding="utf-8")
salas = archivo_salas.readlines()
archivo_salas.close()

########################################## FUNCIONES DE FUNCIONES XD ##########################################
def printear_funcion(linea):
    funcion = linea.strip().split("-")
    nombre_obra = obras[int(funcion[1])].strip().split("-")[1]
    print("-"*155)
    print(f"ID:{funcion[0]} - Obra:{nombre_obra} - Fecha:{funcion[2]} - Horario:{funcion[3]} - Sala:{funcion[4]} - Precio de platea:${funcion[5]} - Precio de palco:${funcion[6]}")
    print("-"*155)
    
def listar_funciones():
    limpiar_pantalla()
    if len(funciones) <= 1:
        print("")
        print("X ---> Upss, todavia no hay funciones registradas <--- X")
    else:
        for i in range(1, len(funciones)):
            printear_funcion(funciones[i])
        
def buscar_funcion_por_id(id):
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
    input = input.strip().lower()
    if input == "":
        print("")
        print("X ---> Upss, no ingresaste ningun texto para buscar <--- X")
        return
    encontrado = False
    for i in range(1, len(funciones)):
        funcion = funciones[i].strip().split("-")
        nombre_obra = obras[int(funcion[1])].strip().split("-")[1].lower()
        if coincide(nombre_obra, input):
            printear_funcion(funciones[i])
            encontrado = True
    if encontrado == False:
        print("")
        print("X ---> Upss, parece que no tenemos obras con ese nombre <--- X")

def listar_obras():
    limpiar_pantalla()
    for i in range(1,len(obras)):
        obra= obras[i].split("-")
        print("-"*155)
        print(f"ID:{obra[0]} - Nombre de la obra o espectáculo:{obra[1]}  - Genero:{obra[3]}")
        print("-"*155)
        
def listar_salas():
    limpiar_pantalla()
    for i in range(1,len(salas)):
        sala= salas[i].split("-")
        print("-"*155)
        print(f"ID:{sala[0]} - Descripcion:{sala[1]}")
        print("-"*155)
        
def registrar_funcion():
    id_funcion = len(funciones)
    listar_obras()

    id_obra = input("Ingrese el ID de la obra: ")
    while id_obra.isdigit() == False or int(id_obra) < 1 or int(id_obra) >= len(obras):
        listar_obras()
        id_obra = input("ID invalido. Ingrese el ID de la obra: ")

    limpiar_pantalla()
    fecha = input("Ingrese la fecha (dd/mm/aaaa): ")
    limpiar_pantalla()
    hora = input("Ingrese el horario (hh:mm): ")

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


def ordenar_funciones_por_nombre_de_obras():
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

def buscar_indice_funcion(id_buscado):
    i = 1
    while i < len(funciones):
        funcion = funciones[i].strip().split("-")
        if int(funcion[0]) == id_buscado:
            return i
        i = i + 1
    return -1
########################################## UBICACIONES ##################################################################
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
    return ubicaciones[id_funcion][int(sector) - 1]

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
    for i in range(1, len(funciones)):
        ubicaciones.append([crear_matriz(FILAS_PLATEA, COLUMNAS), crear_matriz(FILAS_PALCO, COLUMNAS)])

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
    
    
    
    
#######################################            MENUES             #################################################
def menu_funciones():
    opcion = ""

    while opcion != "6":

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
        elif opcion == "2":
            listar_funciones()
        elif opcion == "3":
            id_pedido = input("Ingrese el ID de la funcion que desea visualizar: ")
            buscar_funcion_por_id(id_pedido)
        elif opcion == "4":
            nombre_pedido = input("Ingrese el nombre o fragmento de nombre de la funcion que desea visualizar: ")            
            buscar_funcion_por_nombre(nombre_pedido)
        elif opcion == "5":
            ordenar_funciones_por_nombre_de_obras()
        else:
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
        print("2. Consultar ubicaciones")
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
            #()
            input("\nPresione Enter para continuar...")
        elif opcion == "4":
            #()
            input("\nPresione Enter para continuar...")
        elif opcion == "5":
            print("Gracias por utilizar el sistema.")

        else:
            print("Opción incorrecta. Intente nuevamente.")
menu()