#!/usr/bin/python
def Sudoku:
    def __init__(self,fichero):
        self.sudoku = []
        f = open(fichero)
        for i in range(9):
            cadena = f.readline().split(" ",9)
            self.sudoku[i].append(cadena[0:9])
            
    def copia(self,sudoku):
        for i in range(9):
            self.sudoku[i].append(sudoku[i][0:9])

    def asigna(self,i,j,num):
        self.sudoku[i][j] = num