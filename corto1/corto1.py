
A = 25

def colatz (a):
    c=[]
    while (a != 1):

        if (a%2) == 0:
            a = int(a/2)
            c.append(a)
            
            
        else:
            a = int(a*3) + 1
            c.append(a)
    return (c)


#def escribir (fileName = 'collatz.txt'):
fileName = 'collatz.txt'
archivo = open(fileName, 'w')
archivo.write('\n\nLista de collatz nueva \n')
for i in range (2,A+1):
    b=[i]
    for x in colatz(i):
        b.append(x)
    print (b)
    archivo.write(str(b))
    archivo.write("\n")

archivo.close()
print ("escrito")
    




