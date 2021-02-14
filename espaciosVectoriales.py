import numpy as np
import math

def separarMatrix(a,x,y):
    matriz = []
    aux1 = []
    aux2 = []
    final = []
    for i in range(len(a)):
        for j in range(len(a[0])):
            if i!= x and j !=y:
                matriz.append(a[i][j])

    for i in range(len(matriz)):
        if i //2 != 0:
            aux1.append (matriz[i])
        else:
            aux2.append(matriz[i])

    final.append(aux2)
    final.append(aux1)
    return final

def valorad(a):
    b = a[::-1]
    diagonalPrincipal = 1
    diagonalSecundaria = 1
    for i in range(len(a)):
        diagonalPrincipal = diagonalPrincipal * a[i][i]
        diagonalSecundaria = diagonalSecundaria * b[i][i]
    valor = diagonalPrincipal - diagonalSecundaria
    return valor

#--------------------------------------------------------------
#1
def suma_vec(a,b):
    c = a + b
    resp = [0 for i in range(len(c))]
    for i in range(len(c)):
        resp[i] = c[i]
    return resp

#2
def inversoVec(a):
    inverso = []
    for i in range(len(a)):
        inverso.append(-a[i])
    return inverso

#3
def mult_escalar_vec(k,a):
    resp = [0 for i in range(len(a))]
    for i in range(len(a)):
        resp[i] = k * a[i]
    return resp
#4
def sumMatriz(a, b):
    c = a + b
    return c

#5
def inversoMatriz(a):
    inverso =  [[0 for i in range(len(a[0]))] for j in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a[0])):
            inverso[i][j] = -a[i][j]
    return inverso
#6
def mult_escalar_matriz(k,a):
    resp = [[0 for i in range(len(a[0]))] for j in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a[0])):
            resp[i][j] = k * a[i][j]
    return resp
#7
def transpuesta(a):
    resp = [[0 for i in range(len(a[0]))] for j in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a)):
            resp[i][j] = a[j][i]
    return resp

#8
def conjugada(a):
    conjugado = [[0 for i in range(len(a[0]))] for j in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a[0])):
            x = (a[i][j])
            var1 = str(x[0])
            var2 = str(-x[1])
            if "-" in var2:
                conjugado[i][j] = (var1 + var2 + "j")
            else:
                conjugado[i][j] = (var1 + "+" + var2 + "j")
    return conjugado
#9
def adjunta(a):
    resp = [[0 for i in range(len(a[0]))] for j in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a)):
            if (i + j) % 2 != 0:
                resp[i][j] = -valorad(separarMatrix(a,i,j))
            else:
                resp[i][j] = valorad(separarMatrix(a, i, j))
    return resp
#10
def multiplicar(a,b):
    ans = [[0 for i in range(len(b[0]))] for j in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            resp = 0
            val = 0
            for k in range(len(b)):
                resp = a[i][k] * b[k][j]
                val += resp
            ans[i][j] = val
    return ans
#11
def accion(a,b): #donde sabemos que b tiene que ser un vector
    ans = []
    for i in range(len(a)):
        resp = 0
        val = 0
        for j in range(len(b[0])):
            for k in range(len(b)):
                resp = a[i][j] * b[k][j]
                val += resp
        ans.append(val)
    return ans
#12
def productoInterno(a,b):
    for i in range(len(a)):
        x = a[i]
        var1 = x[0]
        var2 = x[1]
        a[i] = complex(var1, -var2)
    sum = 0
    for i in range(len(b)):
        resp = b[i] * a[i]
        sum += resp
    return sum
#13
def norma(a):
    sum = []
    for i in range(len(a)):
        x = a[i]
        var1 = x[0]
        sum.append(var1)
        var2 = x[1]
        sum.append(var2)
    for i in range(len(sum)):
        sum[i] = sum[i]**2
    math.fsum(sum)
    resp = (math.fsum(sum))**(1/2)
    return resp
#14
def distancia(a,b):
    resta = b - a
    return norma(resta)
#15
def unitaria(a):
    ans = [[0 for i in range(len(a))] for j in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a)):
            if i == j:
                ans[i][j] = 1
    b = a.H
    c = a * b
    return True if np.array_equal(c,ans) else False
#a = np.matrix([[complex(1,1), complex(0,0)], [complex(0,0),complex(0,1)]])
#16
def hermitiana(a):
    b = a.H
    return True if np.array_equal(a, b) else False
#a = np.matrix([[complex(1,1), complex(0,0)], [complex(0,0),complex(0,1)]])
#17
def productoTensor(a,b):
    m = len(a)
    m_ = len(a[0])
    n = len(b)
    n_ =len(b[0])
    nuevaM = m*n
    nuevaN = m_*n_
    matrix = [[0 for i in range(nuevaN)] for j in range(nuevaM)]
    for i in range(nuevaM):
        for j in range(nuevaN):
            matrix[i][j] = a[i//n][j//n_] * b[i % n][j % n_]
    return matrix








