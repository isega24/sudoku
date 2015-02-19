#!/usr/bin/python
def imprime(sudoku):
    print "_ _ _ _ _ _ _ _ _ _ _ _ _"
    for i in range(9):
        string = "|| "
        for j in range(9):
            string = string + str(sudoku[i][j])+" "
            if j%3 == 2:
                string +="|"
                if j == 8 :
                    string += "|"
        print string
        if i%3 ==2:
            print "_ _ _ _ _ _ _ _ _ _ _ _ _"
                
def comprueba_cuadro(sudoku,i,j):
    n = i-i%3
    m = j-j%3
    p = n
    q = m
    posible = True
    if sudoku[i][j] == 0:
        return True

    while p < n+3:
        while q < m+3:
            if sudoku[i][j] == sudoku[p][q] and  not(p == i and q == j):
                posible = False
            q+=1
        q = m
        p+=1
    return posible

def comprueba_fila(sudoku,i,j):
    if sudoku[i][j] == 0:
        return True
    posible = True
    for k in range(9):
        if sudoku[i][k] == sudoku[i][j] and not k == j:
            posible = False

    return posible

def comprueba_columna(sudoku,i,j):
    if sudoku[i][j] == 0:
        return True
    posible = True
    for k in range(9):
        if sudoku[k][j] == sudoku[i][j] and not k == i:
            posible = False
            
    return posible

def comprueba_todo_h(sudoku,x,y):
    return comprueba_fila(sudoku,x,y) and comprueba_cuadro(sudoku,x,y) and comprueba_columna(sudoku,x,y)

def comprueba_todo(sudoku):
    es_sol = True
    for i in range(9):
        for j in range(9):
            if not comprueba_todo_h(sudoku,i,j):
                es_sol = False

    return es_sol
def rellena_sudoku(sudoku):
    nx = 0
    ny = 0
    x = -1
    y = -1

    #Busco la primera casilla vacia

    solucionado = True
    while nx < 9 and solucionado:
        while ny < 9 and solucionado:
            if sudoku[nx][ny] == 0:
                x = nx
                y = ny
                solucionado = False
            ny+=1
        nx +=1
        ny = 0

    #Si no hay ninguna vacia, devolvemos un bool si es Solucion y el sudoku
    if x == -1 and y == -1:
        #Esto lo hago para comprobar
        imprime(sudoku)
            
        return [comprueba_todo_h(sudoku,8,8),sudoku]
    i = 1
    while i < 10:
        sudoku[x][y] = i
        if comprueba_todo_h(sudoku,x,y):
            solucion = rellena_sudoku(sudoku)

            if solucion[0]:
                print "Esta es la solucion?"
                imprime(solucion[1])
                return solucion
        i+=1

    return [False,sudoku]


sudoku = []
for i in range(9):
    lista = []
    for j in range(9):
        cas = 0
        lista.append(cas)
    sudoku.append(lista)
fichero = raw_input("Que sudoku quieres solucionar?: ")
f = open(fichero)
for i in range(9):
    cadena = f.readline().split(" ",9)
    for j in range(9):
        sudoku[i][j] = int(cadena[j])

imprime(sudoku)
solucion = rellena_sudoku(sudoku)
if solucion[0]:
    print "Es la solucion:"
imprime(solucion[1])
'''
while True:
    sudoku[0][0] = 9
    imprime(sudoku)
    x = int(raw_input("Primera coordenada"))
    y = int(raw_input("Segunda coordenada"))
    if comprueba_fila(sudoku,x,y):
        print "Esta bien ", str(x), str(y)

'''
f.close()