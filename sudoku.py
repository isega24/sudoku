#!/usr/bin/python

class casilla:

    def __init__(self):
        self.num = 0
        self.list =[False,False,False,False,False,False,False,False,False]
        self.marcados = 0

    #Funciona perfectamente:

    def marcar_imposible(self,num):
        if not self.list[num-1]:
            self.list[num-1] = True
            self.marcados = +1
            if self.marcados == len(self.list)-1:
                for i in range(len(self.list)):
                    if not self.list[i]:
                        self.num = i+1
                return True
        
        return False

    #Funciona perfectamente:

    def escribir(self,num):
        if self.num == 0 and num > 0 and num < 10 and not self.list[num-1]:
            self.num = num
            for i in range(9):
                self.list[i] = True

            return True
        else:
            return False

class sudoku:

    #Funciona perfectamente:

    def __init__(self):
        self.sudoku = []
        for i in range(9):
            lista = []
            for j in range(9):
                cas = casilla()
                lista.append(cas)
            self.sudoku.append(lista)
        self.rellenadas = 0

    #No lo tengo tan claro...

    def comprueba_cuadro(self,i,j):
        i = i - i%3
        j = j - j%3
        contador = [0,0,0,0,0,0,0,0,0]
        p = i
        q = j
        while p < i+3:
            while q < j+3:
                for l in range(9):
                    if self.sudoku[p][q].list[l]:
                        contador[l]+=1
                q+=1
            q = j
            p+=1

        p = i
        q = j
        for l in range(9):
            if contador[l] == 8:
                while p < i+3:
                    while q < j+3:
                        if not self.sudoku[p][q].list[l]:
                            self.inserta(p,q,l+1)
                        q+=1
                    q = j
                    p+=1

    #Funciona perfectamente:

    def imprime(self):
        print "_ _ _ _ _ _ _ _ _ _ _ _ _"
        for i in range(9):
            string = "|| "
            for j in range(9):
                string = string + str(self.sudoku[i][j].num)+" "
                if j%3 == 2:
                    string +="|"
                    if j == 8 :
                        string += "|"
            print string
            if i%3 ==2:
                print "_ _ _ _ _ _ _ _ _ _ _ _ _"

    #Funciona perfectamente:

    def inicializa(self,fichero):
        f = open(fichero)
        for i in range(9):
            cadena = f.readline().split(" ",9)
            for j in range(9):
                self.inserta(i,j,int(cadena[j]))


    #Funciona perfectamente:

    def rellena(self,i,j):
        self.marcar_cuadro_imposible(i,j)
        self.marcar_fila_imposible(i,j,self.sudoku[i][j].num)
        self.marcar_columna_imposible(i,j,self.sudoku[i][j].num)
        lista = [0,3,6]
        for k in lista:
            for l in lista:
                self.comprueba_cuadro(k,l)

        for k in range(9):
            self.comprueba_fila(k)
            self.comprueba_columna(k)

    def comprueba_fila(self,fil):
        lista1 = [False,False,False,False,False,False,False,False,False]
        posicion = 0
        contador = 0
        for i in range(9):
            if not self.sudoku[i][fil].num ==0:
                contador+=1
                lista1[self.sudoku[i][fil].num-1] = True
            else:
                posicion = i

        if contador==8:
            for j in range(9):
                if not lista1[j]:
                    self.inserta(posicion,fil,j+1)

    
    def comprueba_columna(self,col):
        lista1 = [False,False,False,False,False,False,False,False,False]
        posicion = 0
        contador = 0
        for i in range(9):
            if not self.sudoku[col][i].num ==0:
                contador+=1
                lista1[self.sudoku[col][i].num-1] = True
            else:
                posicion = i

        if contador==8:
            for j in range(9):
                if not lista1[j]:
                    self.inserta(col,posicion,j+1)
    

    #Funciona perfectamente:

    def inserta(self,i,j,num):
        if self.sudoku[i][j].escribir(num):
            self.rellenadas += 1
            self.rellena(i,j)

    #Funciona perfectamente.
    '''
    Marca la fila i como imposible para el numero num
    Solo marca las que no estan en el cuadro.
    '''
    def marcar_fila_imposible(self,i,j,num):
        for k in range(9):
            if k < i -i%3 or k > (i-i%3)+3:
                if self.sudoku[k][j].num ==0:
                    self.sudoku[k][j].marcar_imposible(num)
                    if not self.sudoku[k][j].num == 0:
                        self.rellena(k,j)


    #Funciona perfectamente.

    '''
    Marla la columna j como imposible para el numero num
    Solo marca las que no estan en en el cuadro.
    '''

    def marcar_columna_imposible(self,i,j,num):
        for k in range(9):
            if k < j-j%3 or k > (j-j%3)+3:
                if self.sudoku[i][k].num ==0:
                    self.sudoku[i][k].marcar_imposible(num)
                    if not self.sudoku[i][k].num == 0:
                        self.rellena(i,k)

    #Funciona perfectamente.

    '''
    Marca el cuadro del elemento i j como imposible, ya que el elemento
    i j ya tiene elemento.
    '''

    def marcar_cuadro_imposible(self,i,j):
        n = i-i%3
        m = j-j%3
        while n < (i-i%3)+3:
            while m < (j-j%3)+3:
                if self.sudoku[n][m].num ==0:
                    self.sudoku[n][m].marcar_imposible(self.sudoku[i][j].num)
                    if not self.sudoku[n][m].num == 0:
                        self.rellena(n,m)
                m+=1
            m = j-j%3
            n+=1

    #Tengo que ver si funciona bien.

    '''
    Descubre los elementos que solo pueden estar en una casilla de un
    cuadro en especial.
    '''



sudok = sudoku()
sudok.inicializa(raw_input("Que sudoku quieres solucionar?:"))
'''
while True:
    sudok.imprime()
    cadena = raw_input("Datos:").split(" ",3)
    sudok.inserta(int(cadena[1])-1,int(cadena[0])-1,int(cadena[2]))
'''

sudok.imprime()



