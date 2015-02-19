#!/usr/bin/python
class Sudoku:
    def __init__(self):
        self.sudoku = []
        for i in range(9):
            lista = []
            for j in range(9):
                cas = 0
                lista.append(cas)
            self.sudoku.append(lista)

    def lee(self,fichero):
        f = open(fichero)
        for i in range(9):
            cadena = f.readline().split(" ",9)
            for j in range(9):
                self.sudoku[i][j] = int(cadena[j])

    def copia(self,sudoku):
        for i in range(9):
            for j in range(9):
                self.sudoku[i][j] =sudoku.sudoku[i][j]

    def asigna(self,i,j,num):
        self.sudoku[i][j] = num

    def comprueba_cuadro(self,i,j):
        n = i-i%3
        m = j-j%3
        p = n
        q = m
        posible = True
        if self.sudoku[i][j] == 0:
            return True

        while p < n+3:
            while q < m+3:
                if self.sudoku[i][j] == self.sudoku[p][q] and  not(p == i and q == j):
                    posible = False
                q+=1
            q = m
            p+=1
        return posible

    def comprueba_fila(self,i,j):
        if self.sudoku[i][j] == 0:
            return True
        posible = True
        for k in range(9):
            if self.sudoku[i][k] == self.sudoku[i][j] and not k == j:
                posible = False

        return posible

    def comprueba_columna(self,i,j):
        if self.sudoku[i][j] == 0:
            return True
        posible = True
        for k in range(9):
            if self.sudoku[k][j] == self.sudoku[i][j] and not k == i:
                posible = False
                
        return posible

    def comprueba_todo_h(self,x,y):
        return self.comprueba_fila(x,y) and self.comprueba_cuadro(x,y) and self.comprueba_columna(x,y)

    def comprueba_todo(self):
        es_sol = True
        for i in range(9):
            for j in range(9):
                if not self.comprueba_todo_h(i,j):
                    es_sol = False

        return es_sol

    def imprime(self):
        print "_ _ _ _ _ _ _ _ _ _ _ _ _"
        for i in range(9):
            string = "|| "
            for j in range(9):
                string = string + str(self.sudoku[i][j])+" "
                if j%3 == 2:
                    string +="|"
                    if j == 8 :
                        string += "|"
            print string
            if i%3 ==2:
                print "_ _ _ _ _ _ _ _ _ _ _ _ _"

def rellena_sudoku(sudoku):
    nx = 0
    ny = 0
    x = -1
    y = -1

    #Busco la primera casilla vacia

    solucionado = True
    while nx < 9 and solucionado:
        while ny < 9 and solucionado:
            if sudoku.sudoku[nx][ny] == 0:
                x = nx
                y = ny
                solucionado = False
            ny+=1
        nx +=1
        ny = 0

    #Si no hay ninguna vacia, devolvemos un bool si es Solucion y el sudoku

    if x == -1 and y == -1:
        return [sudoku.comprueba_todo(),sudoku]
    i = 1
    copia = Sudoku()
    copia.copia(sudoku)
    while i < 10:
        copia.sudoku[x][y] = i
        if copia.comprueba_todo_h(x,y):
            solucion = rellena_sudoku(copia)

            if solucion[0]:
                return solucion
        i+=1

    return [False,sudoku]
sudok = Sudoku()
sudok.lee(raw_input("Que sudoku quieres solucionar?: "))
solucion = rellena_sudoku(sudok)

print "Sudoku inicial"
sudok.imprime()
if solucion[0]:
    print "Solucion del sudoku"
else:
    print "No hay solucion"

solucion[1].imprime()