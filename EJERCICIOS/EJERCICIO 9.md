# EJERCICIO 1
1 - Realiza un programa que solicite dos números y una operación (suma, resta, división y multiplicación) e imprima el resultado.

Además deberá mostrar un menú con las siguientes opciones:

Mostrar números

Sumar

Restar

Dividir (considerar la división entre 0)

multipicar

cerrar calculadora


# EJERCICIO 2
2 - Realizar un programa que administre una agenda. Se debe almacenar para cada contacto el nombre, el teléfono y el email.

Además deberá mostrar un menú con las siguientes opciones:

Añadir contacto

Lista de contactos

Buscar contacto

Editar contacto

Cerrar agenda
agenda=agenda()
def nuevoContacto():
    nombre = input('ingrese nombre: ')
    telefono = int(input('ingrese telefono: '))
    email = input('ingrse email: ')
    return usuario(nombre, telefono, email)
    
def buscacontacto():
    nombre =input('ingrse nombre a buscar: ')
    return agenda.buscarcontacto(nombre)
    
def menu():
    opcion = 0
    print('agenda de contactos')
    while opcion !=5:
        print('1) Añadir contacto')
        print('2) Lista de contactos')
        print('3) Buscar contacto')
        print('4) Actualizar contacto')
        print('5) Cerrar agenda')    
        opcion = int(input('\nIngrese una opcion')
    
    if opcion == 1:
            contacto = nuevoContacto()
            agenda.añadirContacto(contacto)
            print(contacto)

        elif opcion == 2:
            agenda.mostrarContacto(contacto)

        elif opcion == 3:
            buscarcontacto()

        elif opcion == 4:
            menu()
    
