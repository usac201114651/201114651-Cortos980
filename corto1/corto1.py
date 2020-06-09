
A = 651 #número de carné

def colatz (a): #definición que genera una a una las listas de collatz, recibe un número natural hasta el cual se calcula la serie
    c=[] #se crea una lista vacía para almacenar los elementos de la serie
    while (a != 1): #se detiene hasta que sea 1

        if (a%2) == 0: #si es par ejecuta a/2 y agrega a la lista c
            a = int(a/2)
            c.append(a)
            
            
        else: #si es impar ejecuta 3*a +1 y agrega a la lista c
            a = int(a*3) + 1
            c.append(a)
    return (c) #regresa la lista en el valor i de la iteración del ciclo for 


fileName = 'collatz.txt' # asignar una variable y la ruta del archivo
archivo = open(fileName, 'w') #abrir el archivo en modo escritura, Borra y escribe "w"
archivo.write('\nLista de collatz nueva \n')#coloca el puntero en una nueva linea
for i in range (2,A+1): #genera sucesiones de collatz desde el natural 2 hasta el valor A que es últimos tres del numero de carne
    b=[i]
    for x in colatz(i): #recorre la lista obtenida de la función colatz
        b.append(x) #agrega a una nueva lista con valor inicial del valor inicial de la sucesion
    print (b)
    archivo.write(str(b)) #escribe la lista en el archivo
    archivo.write("\n")#coloca el puntero en una nueva línea

archivo.close() #cierra el archivo
print ("la lista fue escrita en el archivo collatz.txt")
    




