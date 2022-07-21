# Práctica 4. 6 puntos
## Tipos de colección de datos.
### 4.1 Ejercicio 1(1.2 puntos)
Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10)
y posteriormente muestre en pantalla cada elemento de la lista junto con su
cuadrado y su cubo.
Respuesta:
```
import random 
lista_numeros = [] 
for indice in range(1,11):
lista_numeros.append(random.randint(1,10))
for numero in lista_numeros:
 print(numero," ",numero ** 2," ",numero ** 3)
```

### 4.2 Ejercicio 2 (1.2 puntos)
Crea una lista e inicializarla con 5 cadenas de caracteres leídas por teclado. Copia
los elementos de la lista en otra lista pero en orden inverso, y muestra sus
elementos por la pantalla.
```
lista1 = []
lista2 = []
for indice in range (1,6):
  lista1.append(input("Dame la cadena %d:" % indice))
  lista2 = lista1[::-1]
for cadena in lista2:
  print(cadena)
  
```

### 4.3 Ejercicio 3 (1.2 puntos)
Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un
alumno (comprendidas entre 0 y 10). A continuación debe mostrar todas las notas,
la nota media, la nota más alta que ha sacado y la menor.
```
notas = []
cont=1
while cont<6:
    nota = int(input("Introduce la nota %i:" % cont))
    if nota>=0 and nota<=10:
      cont=cont+1
      notas.append(nota)
    else:
      print('dato incorrecto, ingresa de nuevo la calificación')

print('Notas: ')
print('---)
print("Nota media: ",sum(notas)/len(notas))
print("Nota max: ",max(notas))
print("Nota min: ",min(notas))
```

### 4.4 Ejercicio 4 (1.2 puntos)
Codifica un programa en python que nos permita guardar los nombres de los
alumnos de una clase y las notas que han obtenido. Cada alumno puede tener
distinta cantidad de notas. Guarda la información en un diccionario cuya claves
serán los nombres de los alumnos y los valores serán listados con las notas de
cada alumno.

El programa pedirá el número de alumnos que vamos a introducir, pedirá su
nombre e irá pidiendo sus notas hasta que introduzcamos un número negativo. Al
final el programa nos mostrará la lista de alumnos y la nota media obtenida por
cada uno de ellos. Nota: si se introduce el nombre de un alumno que ya existe el
programa nos dará un error.
```
alumnos = {}
calificacion=[]
cantidad = int(input("digita cantidad de alumnos que vamos a guardar:"))
for num in range(cantidad):
    alumno = input("Nombre del alumno:")
    while alumno in alumnos:
      print("Alumno ya existe.")
      alumno = input("Nombre del alumno:")
    nota = int(input("Dame una calificacion del alumno (negativo para terminar):"))
    while calificacion > 0:
      notas.append(calificacion)
      calificacion = int(input("Dame una calificacion del alumno (negativo para terminar):"))
      alumnos[alumno] = notas.copy()
    for alumno, calificacion in alumnos.items():
      print("%s ha sacado de nota media %f" % (alumno,sum(calificacion)/len(calificacion)))
```

### 4.5 Ejercicio 5 (1.2 puntos)
Crea una tupla con los meses del año, pide números al usuario, si el número está
entre 1 y la longitud máxima de la tupla, muestra el contenido de esa posición sino
muestra un mensaje de error. El programa termina cuando el usuario introduce un
cero.
```
meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre","Noviembre", "Diciembre")
numero = int(input("coloca un numero: "))
while (numero!=0):
 if(numero>=1 and numero<=len(meses)):
    print(meses[numero-1])
    numero = int(input("coloca un numero: ")) 
 else:
    print("Inserta un número entre 1 y ",len(meses))
    numero = int(input("coloca  un numero: "))
else:
 print('salir')
 ```

# TRATA DE RESOLVER Y AVANZAR LO MÁS POSIBLE EN LOS EJERICICIOS, EL MARTES HABILITO "AYUDAS" EN CADA EJERCICIO
