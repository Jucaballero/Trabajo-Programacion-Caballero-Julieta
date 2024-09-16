#Programa Gestion de pacientes.

pacientes = []  #Matriz 
pac_registrados = set()  #Conjunto vacio
diag_previos = set() #Conjunto vacio
id_paciente = 1
numero_paciente = id_paciente

#Creamos una funcion para agregar un paciente
def agregar_paciente(pacientes, pac_registrados, id_paciente):
    nombre = input("Ingrese el nombre del paciente: ").lower()
    edad = int(input("Ingrese la edad del paciente: "))
    sexo = input("Ingrese el sexo del paciente (M/F): ").upper()
    
    paciente = { #crear un diccionario con los datos del paciente
        'ID': numero_paciente,
        'Nombre': nombre,
        'Edad': edad,
        'Sexo': sexo,
        'diagnosticos': diag_previos
    }
    if nombre in pac_registrados: #for_in_ recorre elemento por elemento
        print(f"El paciente {nombre} ya está registrado.") #busca en el diccionario
        return id_paciente
    
    # Conjunto para crear el diagnostico
    while True: #ingresa siempre
        diagnostico = input("Ingrese el diagnostico del paciente o 'salir' para volver al menu principal: ").lower()
        if diagnostico == 'salir':
            break #sale del while
        diag_previos.add(diagnostico) #agrego el elemento "diagnostico" al conjunto de "diag_previos"
    
    # Agregamos el paciente a la lista
    pacientes.append(paciente) #append: agregar un elemento al final de la lista
    pac_registrados.add(nombre) #add: agregar elemento que no estan en el conjunto
    print(f"Paciente {nombre} (ID: {numero_paciente}) agregado correctamente.")
    return id_paciente + 1 # Incremento el id para otro paciente

# Función para ver la lista de pacientes: 1 imprimimos si no esta, 2 recorremos los elementos y si esta imprimimos el diccionario
def mostrar_pacientes(pacientes):
    if not pacientes:
        print("No hay pacientes registrados.")
        return
    
    print("\nLista de pacientes registrados:") #impirmo el diccionario con los datos del paciente
    for paciente in pacientes:                 #primero el print
        print(f"Paciente ID: {paciente['ID']}") #luego la clave : valor
        print(f"Nombre: {paciente['Nombre']}")
        print(f"Edad: {paciente['Edad']}")
        print(f"Sexo: {paciente['Sexo']}")
        print(f"diagnosticos previos: {paciente['diagnosticos']}")

#Creamos una funcion para buscar el pac por nombre
def buscar_paciente(pacientes, nombre):
    for paciente in pacientes: #for (diccionario) in (matriz) recorre elemento por elemento
        if paciente['Nombre'].lower() == nombre.lower(): #pongo la condicion, diccionario == variable
            print(f"Datos del paciente {nombre} (ID: {paciente['ID']}):")
            print(f"Edad: {paciente['Edad']}")
            print(f"Sexo: {paciente['Sexo']}")
            print(f"diagnosticos previas:{paciente['diagnosticos']}")
            return
        else: print(f"El paciente {nombre} no está registrado.")

#Creamos una funcion para buscar paciente por id
def buscar_paciente_id(pacientes, numero_paciente):
    for paciente in pacientes: #for (diccionario) in (matriz) recorre elemento por elemento
        if paciente['ID'] == numero_paciente: #o por id
            print(f"Datos del paciente {nombre} (ID: {paciente['ID']}):")
            print(f"Edad: {paciente['Edad']}")
            print(f"Sexo: {paciente['Sexo']}")
            print(f"diagnosticos previos:{paciente['diagnosticos']}")
            return
    print(f"El paciente {paciente['ID']} no está registrado.")

#Definimos la funcion principal
def main():
    while True:
        print("\nOpciones:")
        print("1. Agregar paciente")
        print("2. Mostrar lista de pacientes")
        print("3. Buscar paciente por nombre")
        print("4. Buscar paciente por ID")
        print("5. Ingresar otro paciente")
        print("6. Salir")
        opcion = input("Seleccione una opción (1-6): ")
        
        if opcion == '1':
            agregar_paciente(pacientes, pac_registrados, id_paciente)
        elif opcion == '2':
            mostrar_pacientes(pacientes)
        elif opcion == '3':
            nombre_buscar = input("Ingrese el nombre del paciente a buscar: ")
            buscar_paciente(pacientes, nombre_buscar)
        elif opcion == '4':
            numero_paciente = input("Ingrese numero de ID del paciente: ")
            buscar_paciente_id(pacientes, numero_paciente)
        elif opcion == '5':
            agregar_paciente(pacientes, pac_registrados, id_paciente)
        elif opcion == '6':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")
main()