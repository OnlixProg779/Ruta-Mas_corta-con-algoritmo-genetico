from interseccion import Interseccion
import random
from ruta import Ruta
from copy import deepcopy



def crearRutas(matriz, puntoInicial, puntoFinal):

    ruta = []
    ruta.append(Interseccion(name=puntoInicial, x=0, y=0, distancia=0))
    crearRutasOptimizada(matriz,puntoInicial, puntoFinal, ruta)
    return ruta
    # pass

def crearRutasOptimizada(matriz, puntoInicial, puntoFinal, ruta):
    romper =  False
    # print()
    # print(puntoInicial)
    # print(puntoFinal)
    if(puntoInicial == puntoFinal):
        return
    else:
        inicio, fin = _encontrarPuntoInicial(puntoInicial, puntoFinal)
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                if(i == inicio and matriz[i][j] != 0):
                    interseccion= Interseccion(name=_encontrarNombre(j), x=i, y=j, distancia=matriz[i][j]);
                    if(comprobarSiExiste(interseccion, ruta)):
                        continue
                    if(0.8 > random.random()):
                        ruta.append(interseccion)
                    else:
                        continue
                    # print(ruta)
                    return crearRutasOptimizada(matriz, _encontrarNombre(j),puntoFinal,ruta)
                    romper = True
                    break
            if(romper):
                break

def selecciona_padres(poblacion, seleccion):
    ordenados_por_distancia = sorted(poblacion, key=lambda ruta: ruta.distancia)
    return ordenados_por_distancia[:seleccion]


def cruza(mejores_padres, iteracionPoblacion): #Recibe los padres y se define el tamaño de la poblacion
    nuevos_hijos = deepcopy(mejores_padres)
    for _ in range(iteracionPoblacion):
        for i in range(len(mejores_padres)):
            _cruza_dos_padres(mejores_padres[i], mejores_padres, nuevos_hijos)


    return nuevos_hijos


def _cruza_dos_padres(padre1, padres, nuevos_hijos):#Aqui se especifica el tratamiento de cruce exclusivo para el problema de optimizacion de ruta
    copiaPadres = deepcopy(padres)
    aleatorio = random.randint(1, len(padre1.intersecciones))
    hijo = deepcopy(padre1.intersecciones[:aleatorio]); #genera una copia de las 3 primeras intersecciones
    aux = []
    
    # print("hijo")
    # print(hijo)


    ciudadTresHijo = hijo[aleatorio-1].name #El nombre del ultimo hijo
    for i in range(len(padres)):
        for j in range(len(padres[i].intersecciones)):
            hijoNuevoAux = []
            if(padres[i].intersecciones[j].name == ciudadTresHijo):
                aux = deepcopy(padres[i].intersecciones[j+1:])
                hijoNuevoAux = hijo + aux
                rutaAux = Ruta(hijoNuevoAux)
                if(noExisteLista(rutaAux.intersecciones, nuevos_hijos)):
                    # print("Candidato calificado")
                    # print(rutaAux.intersecciones)
                    nuevos_hijos.append(rutaAux)
                    # print(Ruta(hijoNuevoAux).distancia)
                    break
     
     
         
  
 
def noExisteLista(inter, lista):
    for i in range(len(lista)):
        for j in range(len(lista[i].intersecciones)):
            if(inter == lista[i].intersecciones):
                return False
    return True
    
def comprobarSiExiste(interseccion, ruta):
    for i in range(len(ruta)):
        if(ruta[i].name == interseccion.name):
            return True
    return False;


def _encontrarPuntoInicial(puntoInicial, puntoFinal):
    i = 9999
    j = 9999
    if(puntoInicial == 'a'):
        i = 0
    if(puntoInicial == 'b'):
        i = 1
    if(puntoInicial == 'c'):
        i = 2
    if(puntoInicial == 'd'):
        i = 3
    if(puntoInicial == 'e'):
        i = 4
    if(puntoInicial == 'f'):
        i = 5
    if(puntoInicial == 'g'):
        i = 6
    if(puntoInicial == 'h'):
        i = 7
    if(puntoInicial == 'i'):
        i = 8
    if(puntoInicial == 'j'):
        i = 9
    if(puntoInicial == 'k'):
        i = 10
    if(puntoInicial == 'l'):
        i = 11
    if(puntoInicial == 'm'):
        i = 12
    if(puntoInicial == 'n'):
        i = 13
    if(puntoInicial == 'o'):
        i = 14
    if(puntoInicial == 'p'):
        i = 15
    if(puntoInicial == 'q'):
        i = 16
    if(puntoInicial == 'r'):
        i = 17
    if(puntoInicial == 's'):
        i = 18
    if(puntoInicial == 't'):
        i = 19
    if(puntoInicial == 'u'):
        i = 20
    if(puntoInicial == 'v'):
        i = 21
    if(puntoInicial == 'w'):
        i = 22
    if(puntoInicial == 'x'):
        i = 23
    if(puntoInicial == 'y'):
        i = 24
    if(puntoInicial == 'z'):
        i = 25
    if(puntoInicial == 'a1'):
        i = 26
    if(puntoInicial == 'b1'):
        i = 27
    if(puntoInicial == 'c1'):
        i = 28
    if(puntoInicial == 'd1'):
        i = 29
    if(puntoInicial == 'e1'):
        i = 30
    if(puntoInicial == 'f1'):
        i = 31
    if(puntoInicial == 'g1'):
        i = 32
    if(puntoInicial == 'h1'):
        i = 33
    if(puntoInicial == 'i1'):
        i = 34
    if(puntoInicial == 'j1'):
        i = 35
    if(puntoInicial == 'k1'):
        i = 36
    if(puntoInicial == 'l1'):
        i = 37
    if(puntoInicial == 'm1'):
        i = 38
    if(puntoInicial == 'n1'):
        i = 39
    if(puntoInicial == 'o1'):
        i = 40
    if(puntoInicial == 'p1'):
        i = 41
    if(puntoFinal == 'a'):
        j = 0
    if(puntoFinal == 'b'):
        j = 1
    if(puntoFinal == 'c'):
        j = 2
    if(puntoFinal == 'd'):
        j = 3
    if(puntoFinal == 'e'):
        j = 4
    if(puntoFinal == 'f'):
        j = 5
    if(puntoFinal == 'g'):
        j = 6
    if(puntoFinal == 'h'):
        j = 7
    if(puntoFinal == 'j'):
        j = 8
    if(puntoFinal == 'j'):
        j = 9
    if(puntoFinal == 'k'):
        j = 10
    if(puntoFinal == 'l'):
        j = 11
    if(puntoFinal == 'm'):
        j = 12
    if(puntoFinal == 'n'):
        j = 13
    if(puntoFinal == 'o'):
        j = 14
    if(puntoFinal == 'p'):
        j = 15
    if(puntoFinal == 'q'):
        j = 16
    if(puntoFinal == 'r'):
        j = 17
    if(puntoFinal == 's'):
        j = 18
    if(puntoFinal == 't'):
        j = 19
    if(puntoFinal == 'u'):
        j = 20
    if(puntoFinal == 'v'):
        j = 21
    if(puntoFinal == 'w'):
        j = 22
    if(puntoFinal == 'x'):
        j = 23
    if(puntoFinal == 'y'):
        j = 24
    if(puntoFinal == 'z'):
        j = 25
    if(puntoFinal == 'a1'):
        j = 26
    if(puntoFinal == 'b1'):
        j = 27
    if(puntoFinal == 'c1'):
        j = 28
    if(puntoFinal == 'd1'):
        j = 29
    if(puntoFinal == 'e1'):
        j = 30
    if(puntoFinal == 'f1'):
        j = 31
    if(puntoFinal == 'g1'):
        j = 32
    if(puntoFinal == 'h1'):
        j = 33
    if(puntoFinal == 'i1'):
        j = 34
    if(puntoFinal == 'j1'):
        j = 35
    if(puntoFinal == 'k1'):
        j = 36
    if(puntoFinal == 'l1'):
        j = 37
    if(puntoFinal == 'm1'):
        j = 38
    if(puntoFinal == 'n1'):
        j = 39
    if(puntoFinal == 'o1'):
        j = 40
    if(puntoFinal == 'p1'):
        j = 41
    return i,j


def _encontrarNombre(punto):
    nombre = ""
    if(punto == 0):
        nombre = 'a'
    if(punto == 1):
        nombre = 'b'
    if(punto == 2):
        nombre = 'c'
    if(punto == 3):
        nombre = 'd'
    if(punto == 4):
        nombre = 'e'
    if(punto == 5):
        nombre = 'f'
    if(punto == 6):
        nombre = 'g'
    if(punto == 7):
        nombre = 'h'
    if(punto == 8):
        nombre = 'i'
    if(punto == 9):
        nombre = 'j'
    if(punto == 10):
        nombre = 'k'
    if(punto == 11):
        nombre = 'l'
    if(punto == 12):
        nombre = 'm'
    if(punto == 13):
        nombre = 'n'
    if(punto == 14):
        nombre = 'o'
    if(punto == 15):
        nombre = 'p'
    if(punto == 16):
        nombre = 'q'
    if(punto == 17):
        nombre = 'r'
    if(punto == 18):
        nombre = 's'
    if(punto == 19):
        nombre = 't'
    if(punto == 20):
        nombre = 'u'
    if(punto == 21):
        nombre = 'v'
    if(punto == 22):
        nombre = 'w'
    if(punto == 23):
        nombre = 'x'
    if(punto == 24):
        nombre = 'y'
    if(punto == 25):
        nombre = 'z'
    if(punto == 26):
        nombre = 'a1'
    if(punto == 27):
        nombre = 'b1'
    if(punto == 28):
        nombre = 'c1'
    if(punto == 29):
        nombre = 'd1'
    if(punto == 30):
        nombre = 'e1'
    if(punto == 31):
        nombre = 'f1'
    if(punto == 32):
        nombre = 'g1'
    if(punto == 33):
        nombre = 'h1'
    if(punto == 34):
        nombre = 'i1'
    if(punto == 35):
        nombre = 'j1'
    if(punto == 36):
        nombre = 'k1'
    if(punto == 37):
        nombre = 'l1'
    if(punto == 38):
        nombre = 'm1'
    if(punto == 39):
        nombre = 'n1'
    if(punto == 40):
        nombre = 'o1'
    if(punto == 41):
        nombre = 'p1'
    if(punto == 42):
        nombre = 'q1'
    return nombre



def iniciarMatriz():
    w, h = 42, 42
    datos = [[0 for x in range(w)] for y in range(h)]
    # Fila 0
    datos[0][0]=0
    datos[0][1]=9
    datos[0][2]=0
    datos[0][3]=0
    datos[0][4]=0
    datos[0][5]=0
    datos[0][6]=0
    datos[0][7]=0
    datos[0][8]=0
    datos[0][9]=0
    datos[0][10]=0
    datos[0][11]=0
    datos[0][12]=0
    datos[0][13]=0
    datos[0][14]=0
    datos[0][15]=0
    datos[0][16]=0
    datos[0][17]=0
    datos[0][18]=0
    datos[0][19]=0
    datos[0][20]=0
    datos[0][21]=0
    datos[0][22]=0
    datos[0][23]=0
    datos[0][24]=0
    datos[0][25]=0
    datos[0][26]=0
    datos[0][27]=0
    datos[0][28]=0
    datos[0][29]=0
    datos[0][30]=0
    datos[0][31]=0
    datos[0][32]=0
    datos[0][33]=0
    datos[0][34]=0
    datos[0][35]=0
    datos[0][36]=0
    datos[0][37]=0
    datos[0][38]=0
    datos[0][39]=0
    datos[0][40]=0
    datos[0][41]=0

    # Fila 1
    datos[1][0]=0
    datos[1][1]=0
    datos[1][2]=7
    datos[1][3]=0
    datos[1][4]=0
    datos[1][5]=0
    datos[1][6]=13
    datos[1][7]=0
    datos[1][8]=0
    datos[1][9]=0
    datos[1][10]=0
    datos[1][11]=0
    datos[1][12]=0
    datos[1][13]=0
    datos[1][14]=0
    datos[1][15]=0
    datos[1][16]=0
    datos[1][17]=0
    datos[1][18]=0
    datos[1][19]=0
    datos[1][20]=0
    datos[1][21]=0
    datos[1][22]=0
    datos[1][23]=0
    datos[1][24]=0
    datos[1][25]=0
    datos[1][26]=0
    datos[1][27]=0
    datos[1][28]=0
    datos[1][29]=0
    datos[1][30]=0
    datos[1][31]=0
    datos[1][32]=0
    datos[1][33]=0
    datos[1][34]=0
    datos[1][35]=0
    datos[1][36]=0
    datos[1][37]=0
    datos[1][38]=0
    datos[1][39]=0
    datos[1][40]=0
    datos[1][41]=0

    # Fila 2
    datos[2][0]=0
    datos[2][1]=0
    datos[2][2]=0
    datos[2][3]=14
    datos[2][4]=0
    datos[2][5]=0
    datos[2][6]=0
    datos[2][7]=8
    datos[2][8]=0
    datos[2][9]=0
    datos[2][10]=0
    datos[2][11]=0
    datos[2][12]=0
    datos[2][13]=0
    datos[2][14]=0
    datos[2][15]=0
    datos[2][16]=0
    datos[2][17]=0
    datos[2][18]=0
    datos[2][19]=0
    datos[2][20]=0
    datos[2][21]=0
    datos[2][22]=0
    datos[2][23]=0
    datos[2][24]=0
    datos[2][25]=0
    datos[2][26]=0
    datos[2][27]=0
    datos[2][28]=0
    datos[2][29]=0
    datos[2][30]=0
    datos[2][31]=0
    datos[2][32]=0
    datos[2][33]=0
    datos[2][34]=0
    datos[2][35]=0
    datos[2][36]=0
    datos[2][37]=0
    datos[2][38]=0
    datos[2][39]=0
    datos[2][40]=0
    datos[2][41]=0

    # Fila 3
    datos[3][0]=0
    datos[3][1]=0
    datos[3][2]=0
    datos[3][3]=0
    datos[3][4]=10
    datos[3][5]=0
    datos[3][6]=0
    datos[3][7]=0
    datos[3][8]=0
    datos[3][9]=0
    datos[3][10]=0
    datos[3][11]=0
    datos[3][12]=0
    datos[3][13]=0
    datos[3][14]=0
    datos[3][15]=0
    datos[3][16]=0
    datos[3][17]=0
    datos[3][18]=0
    datos[3][19]=0
    datos[3][20]=0
    datos[3][21]=0
    datos[3][22]=0
    datos[3][23]=0
    datos[3][24]=0
    datos[3][25]=0
    datos[3][26]=0
    datos[3][27]=0
    datos[3][28]=0
    datos[3][29]=0
    datos[3][30]=0
    datos[3][31]=0
    datos[3][32]=0
    datos[3][33]=0
    datos[3][34]=0
    datos[3][35]=0
    datos[3][36]=0
    datos[3][37]=0
    datos[3][38]=0
    datos[3][39]=0
    datos[3][40]=0
    datos[3][41]=0

    # Fila 4
    datos[4][0]=0
    datos[4][1]=0
    datos[4][2]=0
    datos[4][3]=0
    datos[4][4]=0
    datos[4][5]=0
    datos[4][6]=0
    datos[4][7]=0
    datos[4][8]=0
    datos[4][9]=11
    datos[4][10]=0
    datos[4][11]=0
    datos[4][12]=0
    datos[4][13]=0
    datos[4][14]=0
    datos[4][15]=0
    datos[4][16]=0
    datos[4][17]=0
    datos[4][18]=0
    datos[4][19]=0
    datos[4][20]=0
    datos[4][21]=0
    datos[4][22]=0
    datos[4][23]=0
    datos[4][24]=0
    datos[4][25]=0
    datos[4][26]=0
    datos[4][27]=0
    datos[4][28]=0
    datos[4][29]=0
    datos[4][30]=0
    datos[4][31]=0
    datos[4][32]=0
    datos[4][33]=0
    datos[4][34]=0
    datos[4][35]=15
    datos[4][36]=0
    datos[4][37]=0
    datos[4][38]=0
    datos[4][39]=0
    datos[4][40]=0
    datos[4][41]=0

    # Fila 5
    datos[5][0]=9
    datos[5][1]=0
    datos[5][2]=0
    datos[5][3]=0
    datos[5][4]=0
    datos[5][5]=0
    datos[5][6]=0
    datos[5][7]=0
    datos[5][8]=0
    datos[5][9]=0
    datos[5][10]=0
    datos[5][11]=0
    datos[5][12]=0
    datos[5][13]=0
    datos[5][14]=0
    datos[5][15]=0
    datos[5][16]=0
    datos[5][17]=0
    datos[5][18]=0
    datos[5][19]=0
    datos[5][20]=0
    datos[5][21]=0
    datos[5][22]=0
    datos[5][23]=0
    datos[5][24]=0
    datos[5][25]=0
    datos[5][26]=0
    datos[5][27]=0
    datos[5][28]=0
    datos[5][29]=0
    datos[5][30]=0
    datos[5][31]=0
    datos[5][32]=0
    datos[5][33]=0
    datos[5][34]=0
    datos[5][35]=0
    datos[5][36]=0
    datos[5][37]=0
    datos[5][38]=0
    datos[5][39]=0
    datos[5][40]=0
    datos[5][41]=0

    # Fila 6
    datos[6][0]=0
    datos[6][1]=8
    datos[6][2]=0
    datos[6][3]=0
    datos[6][4]=0
    datos[6][5]=9
    datos[6][6]=0
    datos[6][7]=0
    datos[6][8]=0
    datos[6][9]=0
    datos[6][10]=0
    datos[6][11]=8
    datos[6][12]=0
    datos[6][13]=0
    datos[6][14]=0
    datos[6][15]=0
    datos[6][16]=0
    datos[6][17]=0
    datos[6][18]=0
    datos[6][19]=0
    datos[6][20]=0
    datos[6][21]=0
    datos[6][22]=0
    datos[6][23]=0
    datos[6][24]=0
    datos[6][25]=0
    datos[6][26]=0
    datos[6][27]=0
    datos[6][28]=0
    datos[6][29]=0
    datos[6][30]=0
    datos[6][31]=0
    datos[6][32]=0
    datos[6][33]=0
    datos[6][34]=0
    datos[6][35]=0
    datos[6][36]=0
    datos[6][37]=0
    datos[6][38]=0
    datos[6][39]=0
    datos[6][40]=0
    datos[6][41]=0

    # File 7
    datos[7][0]=0
    datos[7][1]=0
    datos[7][2]=0
    datos[7][3]=0
    datos[7][4]=0
    datos[7][5]=0
    datos[7][6]=10
    datos[7][7]=0
    datos[7][8]=0
    datos[7][9]=0
    datos[7][10]=0
    datos[7][11]=0
    datos[7][12]=17
    datos[7][13]=0
    datos[7][14]=0
    datos[7][15]=0
    datos[7][16]=0
    datos[7][17]=0
    datos[7][18]=0
    datos[7][19]=0
    datos[7][20]=0
    datos[7][21]=0
    datos[7][22]=0
    datos[7][23]=0
    datos[7][24]=0
    datos[7][25]=0
    datos[7][26]=0
    datos[7][27]=0
    datos[7][28]=0
    datos[7][29]=0
    datos[7][30]=0
    datos[7][31]=0
    datos[7][32]=0
    datos[7][33]=0
    datos[7][34]=0
    datos[7][35]=0
    datos[7][36]=0
    datos[7][37]=0
    datos[7][38]=0
    datos[7][39]=0
    datos[7][40]=0
    datos[7][41]=0

    # Fila 8
    datos[8][0]=0
    datos[8][1]=0
    datos[8][2]=0
    datos[8][3]=12
    datos[8][4]=0
    datos[8][5]=0
    datos[8][6]=0
    datos[8][7]=14
    datos[8][8]=0
    datos[8][9]=0
    datos[8][10]=0
    datos[8][11]=0
    datos[8][12]=0
    datos[8][13]=0
    datos[8][14]=0
    datos[8][15]=0
    datos[8][16]=0
    datos[8][17]=0
    datos[8][18]=0
    datos[8][19]=0
    datos[8][20]=0
    datos[8][21]=0
    datos[8][22]=0
    datos[8][23]=0
    datos[8][24]=0
    datos[8][25]=0
    datos[8][26]=0
    datos[8][27]=0
    datos[8][28]=0
    datos[8][29]=0
    datos[8][30]=0
    datos[8][31]=0
    datos[8][32]=0
    datos[8][33]=0
    datos[8][34]=0
    datos[8][35]=0
    datos[8][36]=0
    datos[8][37]=0
    datos[8][38]=0
    datos[8][39]=0
    datos[8][40]=0
    datos[8][41]=0

    # Fila 9
    datos[9][0]=0
    datos[9][1]=0
    datos[9][2]=0
    datos[9][3]=0
    datos[9][4]=16
    datos[9][5]=0
    datos[9][6]=0
    datos[9][7]=0
    datos[9][8]=7
    datos[9][9]=0
    datos[9][10]=0
    datos[9][11]=0
    datos[9][12]=0
    datos[9][13]=0
    datos[9][14]=12
    datos[9][15]=0
    datos[9][16]=0
    datos[9][17]=0
    datos[9][18]=0
    datos[9][19]=0
    datos[9][20]=0
    datos[9][21]=0
    datos[9][22]=0
    datos[9][23]=0
    datos[9][24]=0
    datos[9][25]=0
    datos[9][26]=0
    datos[9][27]=0
    datos[9][28]=0
    datos[9][29]=0
    datos[9][30]=0
    datos[9][31]=0
    datos[9][32]=0
    datos[9][33]=0
    datos[9][34]=0
    datos[9][35]=0
    datos[9][36]=0
    datos[9][37]=0
    datos[9][38]=0
    datos[9][39]=0
    datos[9][40]=0
    datos[9][41]=0

    # Fila 10
    datos[10][0]=0
    datos[10][1]=0
    datos[10][2]=0
    datos[10][3]=0
    datos[10][4]=0
    datos[10][5]=10
    datos[10][6]=0
    datos[10][7]=0
    datos[10][8]=0
    datos[10][9]=0
    datos[10][10]=0
    datos[10][11]=14
    datos[10][12]=0
    datos[10][13]=0
    datos[10][14]=0
    datos[10][15]=0
    datos[10][16]=0
    datos[10][17]=0
    datos[10][18]=0
    datos[10][19]=0
    datos[10][20]=0
    datos[10][21]=0
    datos[10][22]=0
    datos[10][23]=0
    datos[10][24]=0
    datos[10][25]=0
    datos[10][26]=0
    datos[10][27]=0
    datos[10][28]=0
    datos[10][29]=0
    datos[10][30]=0
    datos[10][31]=0
    datos[10][32]=0
    datos[10][33]=0
    datos[10][34]=0
    datos[10][35]=0
    datos[10][36]=0
    datos[10][37]=0
    datos[10][38]=0
    datos[10][39]=0
    datos[10][40]=0
    datos[10][41]=0

    # Fila 11
    datos[11][0]=0
    datos[11][1]=0
    datos[11][2]=0
    datos[11][3]=0
    datos[11][4]=0
    datos[11][5]=0
    datos[11][6]=13
    datos[11][7]=0
    datos[11][8]=0
    datos[11][9]=0
    datos[11][10]=0
    datos[11][11]=0
    datos[11][12]=0
    datos[11][13]=11
    datos[11][14]=0
    datos[11][15]=0
    datos[11][16]=15
    datos[11][17]=0
    datos[11][18]=0
    datos[11][19]=0
    datos[11][20]=0
    datos[11][21]=0
    datos[11][22]=0
    datos[11][23]=0
    datos[11][24]=0
    datos[11][25]=0
    datos[11][26]=0
    datos[11][27]=0
    datos[11][28]=0
    datos[11][29]=0
    datos[11][30]=0
    datos[11][31]=0
    datos[11][32]=0
    datos[11][33]=0
    datos[11][34]=0
    datos[11][35]=0
    datos[11][36]=0
    datos[11][37]=0
    datos[11][38]=0
    datos[11][39]=0
    datos[11][40]=0
    datos[11][41]=0

    # Fila 12
    datos[12][0]=0
    datos[12][1]=0
    datos[12][2]=0
    datos[12][3]=0
    datos[12][4]=0
    datos[12][5]=0
    datos[12][6]=0
    datos[12][7]=0
    datos[12][8]=0
    datos[12][9]=0
    datos[12][10]=0
    datos[12][11]=0
    datos[12][12]=0
    datos[12][13]=12
    datos[12][14]=7
    datos[12][15]=0
    datos[12][16]=0
    datos[12][17]=10
    datos[12][18]=0
    datos[12][19]=0
    datos[12][20]=0
    datos[12][21]=0
    datos[12][22]=0
    datos[12][23]=0
    datos[12][24]=0
    datos[12][25]=0
    datos[12][26]=0
    datos[12][27]=0
    datos[12][28]=0
    datos[12][29]=0
    datos[12][30]=0
    datos[12][31]=0
    datos[12][32]=0
    datos[12][33]=0
    datos[12][34]=0
    datos[12][35]=0
    datos[12][36]=0
    datos[12][37]=0
    datos[12][38]=0
    datos[12][39]=0
    datos[12][40]=0
    datos[12][41]=0

    # Fila 13
    datos[13][0]=0
    datos[13][1]=0
    datos[13][2]=0
    datos[13][3]=0
    datos[13][4]=0
    datos[13][5]=0
    datos[13][6]=0
    datos[13][7]=0
    datos[13][8]=8
    datos[13][9]=0
    datos[13][10]=0
    datos[13][11]=0
    datos[13][12]=0
    datos[13][13]=0
    datos[13][14]=9
    datos[13][15]=0
    datos[13][16]=0
    datos[13][17]=0
    datos[13][18]=0
    datos[13][19]=0
    datos[13][20]=0
    datos[13][21]=0
    datos[13][22]=0
    datos[13][23]=0
    datos[13][24]=0
    datos[13][25]=0
    datos[13][26]=0
    datos[13][27]=0
    datos[13][28]=0
    datos[13][29]=0
    datos[13][30]=0
    datos[13][31]=0
    datos[13][32]=0
    datos[13][33]=0
    datos[13][34]=0
    datos[13][35]=0
    datos[13][36]=0
    datos[13][37]=0
    datos[13][38]=0
    datos[13][39]=0
    datos[13][40]=0
    datos[13][41]=0

    # Fila 14
    datos[14][0]=0
    datos[14][1]=0
    datos[14][2]=0
    datos[14][3]=0
    datos[14][4]=0
    datos[14][5]=0
    datos[14][6]=0
    datos[14][7]=0
    datos[14][8]=0
    datos[14][9]=12
    datos[14][10]=0
    datos[14][11]=0
    datos[14][12]=0
    datos[14][13]=0
    datos[14][14]=0
    datos[14][15]=0
    datos[14][16]=0
    datos[14][17]=0
    datos[14][18]=0
    datos[14][19]=18
    datos[14][20]=0
    datos[14][21]=0
    datos[14][22]=0
    datos[14][23]=0
    datos[14][24]=0
    datos[14][25]=0
    datos[14][26]=0
    datos[14][27]=0
    datos[14][28]=0
    datos[14][29]=0
    datos[14][30]=0
    datos[14][31]=0
    datos[14][32]=0
    datos[14][33]=0
    datos[14][34]=0
    datos[14][35]=0
    datos[14][36]=0
    datos[14][37]=15
    datos[14][38]=0
    datos[14][39]=0
    datos[14][40]=0
    datos[14][41]=0

    # Fila 15
    datos[15][0]=0
    datos[15][1]=0
    datos[15][2]=0
    datos[15][3]=0
    datos[15][4]=0
    datos[15][5]=0
    datos[15][6]=0
    datos[15][7]=0
    datos[15][8]=0
    datos[15][9]=0
    datos[15][10]=14
    datos[15][11]=0
    datos[15][12]=0
    datos[15][13]=0
    datos[15][14]=0
    datos[15][15]=0
    datos[15][16]=11
    datos[15][17]=0
    datos[15][18]=0
    datos[15][19]=0
    datos[15][20]=0
    datos[15][21]=0
    datos[15][22]=0
    datos[15][23]=0
    datos[15][24]=0
    datos[15][25]=0
    datos[15][26]=0
    datos[15][27]=0
    datos[15][28]=0
    datos[15][29]=0
    datos[15][30]=0
    datos[15][31]=0
    datos[15][32]=0
    datos[15][33]=0
    datos[15][34]=0
    datos[15][35]=0
    datos[15][36]=0
    datos[15][37]=0
    datos[15][38]=0
    datos[15][39]=0
    datos[15][40]=0
    datos[15][41]=0

    # Fila 16
    datos[16][0]=0
    datos[16][1]=0
    datos[16][2]=0
    datos[16][3]=0
    datos[16][4]=0
    datos[16][5]=0
    datos[16][6]=0
    datos[16][7]=0
    datos[16][8]=0
    datos[16][9]=0
    datos[16][10]=0
    datos[16][11]=8
    datos[16][12]=0
    datos[16][13]=0
    datos[16][14]=0
    datos[16][15]=10
    datos[16][16]=0
    datos[16][17]=11
    datos[16][18]=0
    datos[16][19]=0
    datos[16][20]=0
    datos[16][21]=14
    datos[16][22]=0
    datos[16][23]=0
    datos[16][24]=0
    datos[16][25]=0
    datos[16][26]=0
    datos[16][27]=0
    datos[16][28]=0
    datos[16][29]=0
    datos[16][30]=0
    datos[16][31]=0
    datos[16][32]=0
    datos[16][33]=0
    datos[16][34]=0
    datos[16][35]=0
    datos[16][36]=0
    datos[16][37]=0
    datos[16][38]=0
    datos[16][39]=0
    datos[16][40]=0
    datos[16][41]=0

    # Fila 17
    datos[17][0]=0
    datos[17][1]=0
    datos[17][2]=0
    datos[17][3]=0
    datos[17][4]=0
    datos[17][5]=0
    datos[17][6]=0
    datos[17][7]=0
    datos[17][8]=0
    datos[17][9]=0
    datos[17][10]=0
    datos[17][11]=0
    datos[17][12]=0
    datos[17][13]=0
    datos[17][14]=0
    datos[17][15]=0
    datos[17][16]=9
    datos[17][17]=0
    datos[17][18]=13
    datos[17][19]=0
    datos[17][20]=0
    datos[17][21]=0
    datos[17][22]=8
    datos[17][23]=0
    datos[17][24]=0
    datos[17][25]=0
    datos[17][26]=0
    datos[17][27]=0
    datos[17][28]=0
    datos[17][29]=0
    datos[17][30]=0
    datos[17][31]=0
    datos[17][32]=0
    datos[17][33]=0
    datos[17][34]=0
    datos[17][35]=0
    datos[17][36]=0
    datos[17][37]=0
    datos[17][38]=0
    datos[17][39]=0
    datos[17][40]=0
    datos[17][41]=0

    # Fila 18
    datos[18][0]=0
    datos[18][1]=0
    datos[18][2]=0
    datos[18][3]=0
    datos[18][4]=0
    datos[18][5]=0
    datos[18][6]=0
    datos[18][7]=0
    datos[18][8]=0
    datos[18][9]=0
    datos[18][10]=0
    datos[18][11]=0
    datos[18][12]=0
    datos[18][13]=14
    datos[18][14]=0
    datos[18][15]=0
    datos[18][16]=0
    datos[18][17]=17
    datos[18][18]=0
    datos[18][19]=11
    datos[18][20]=0
    datos[18][21]=0
    datos[18][22]=0
    datos[18][23]=0
    datos[18][24]=0
    datos[18][25]=0
    datos[18][26]=0
    datos[18][27]=0
    datos[18][28]=0
    datos[18][29]=0
    datos[18][30]=0
    datos[18][31]=0
    datos[18][32]=0
    datos[18][33]=0
    datos[18][34]=0
    datos[18][35]=0
    datos[18][36]=0
    datos[18][37]=0
    datos[18][38]=0
    datos[18][39]=0
    datos[18][40]=0
    datos[18][41]=0

    # Fila 19
    datos[19][0]=0
    datos[19][1]=0
    datos[19][2]=0
    datos[19][3]=0
    datos[19][4]=0
    datos[19][5]=0
    datos[19][6]=0
    datos[19][7]=0
    datos[19][8]=0
    datos[19][9]=0
    datos[19][10]=0
    datos[19][11]=0
    datos[19][12]=0
    datos[19][13]=0
    datos[19][14]=10
    datos[19][15]=0
    datos[19][16]=0
    datos[19][17]=0
    datos[19][18]=12
    datos[19][19]=0
    datos[19][20]=0
    datos[19][21]=0
    datos[19][22]=0
    datos[19][23]=0
    datos[19][24]=8
    datos[19][25]=0
    datos[19][26]=0
    datos[19][27]=0
    datos[19][28]=0
    datos[19][29]=0
    datos[19][30]=0
    datos[19][31]=0
    datos[19][32]=0
    datos[19][33]=0
    datos[19][34]=0
    datos[19][35]=0
    datos[19][36]=0
    datos[19][37]=0
    datos[19][38]=9
    datos[19][39]=0
    datos[19][40]=0
    datos[19][41]=0

    # Fila 20
    datos[20][0]=0
    datos[20][1]=0
    datos[20][2]=0
    datos[20][3]=0
    datos[20][4]=0
    datos[20][5]=0
    datos[20][6]=0
    datos[20][7]=0
    datos[20][8]=0
    datos[20][9]=0
    datos[20][10]=0
    datos[20][11]=0
    datos[20][12]=0
    datos[20][13]=0
    datos[20][14]=0
    datos[20][15]=7
    datos[20][16]=0
    datos[20][17]=0
    datos[20][18]=0
    datos[20][19]=0
    datos[20][20]=0
    datos[20][21]=0
    datos[20][22]=0
    datos[20][23]=0
    datos[20][24]=0
    datos[20][25]=0
    datos[20][26]=0
    datos[20][27]=0
    datos[20][28]=0
    datos[20][29]=0
    datos[20][30]=0
    datos[20][31]=0
    datos[20][32]=0
    datos[20][33]=0
    datos[20][34]=0
    datos[20][35]=0
    datos[20][36]=0
    datos[20][37]=0
    datos[20][38]=0
    datos[20][39]=0
    datos[20][40]=0
    datos[20][41]=0

    # Fila 21
    datos[21][0]=0
    datos[21][1]=0
    datos[21][2]=0
    datos[21][3]=0
    datos[21][4]=0
    datos[21][5]=0
    datos[21][6]=0
    datos[21][7]=0
    datos[21][8]=0
    datos[21][9]=0
    datos[21][10]=0
    datos[21][11]=0
    datos[21][12]=0
    datos[21][13]=0
    datos[21][14]=0
    datos[21][15]=0
    datos[21][16]=13
    datos[21][17]=0
    datos[21][18]=0
    datos[21][19]=0
    datos[21][20]=11
    datos[21][21]=0
    datos[21][22]=0
    datos[21][23]=0
    datos[21][24]=0
    datos[21][25]=0
    datos[21][26]=16
    datos[21][27]=0
    datos[21][28]=0
    datos[21][29]=0
    datos[21][30]=0
    datos[21][31]=0
    datos[21][32]=0
    datos[21][33]=0
    datos[21][34]=0
    datos[21][35]=0
    datos[21][36]=0
    datos[21][37]=0
    datos[21][38]=0
    datos[21][39]=0
    datos[21][40]=0
    datos[21][41]=0

    # Fila 22
    datos[22][0]=0
    datos[22][1]=0
    datos[22][2]=0
    datos[22][3]=0
    datos[22][4]=0
    datos[22][5]=0
    datos[22][6]=0
    datos[22][7]=0
    datos[22][8]=0
    datos[22][9]=0
    datos[22][10]=0
    datos[22][11]=0
    datos[22][12]=0
    datos[22][13]=0
    datos[22][14]=0
    datos[22][15]=0
    datos[22][16]=0
    datos[22][17]=0
    datos[22][18]=0
    datos[22][19]=0
    datos[22][20]=0
    datos[22][21]=9
    datos[22][22]=0
    datos[22][23]=0
    datos[22][24]=0
    datos[22][25]=0
    datos[22][26]=0
    datos[22][27]=11
    datos[22][28]=0
    datos[22][29]=0
    datos[22][30]=0
    datos[22][31]=0
    datos[22][32]=0
    datos[22][33]=0
    datos[22][34]=0
    datos[22][35]=0
    datos[22][36]=0
    datos[22][37]=0
    datos[22][38]=0
    datos[22][39]=0
    datos[22][40]=0
    datos[22][41]=0

    # Fila 23
    datos[23][0]=0
    datos[23][1]=0
    datos[23][2]=0
    datos[23][3]=0
    datos[23][4]=0
    datos[23][5]=0
    datos[23][6]=0
    datos[23][7]=0
    datos[23][8]=0
    datos[23][9]=0
    datos[23][10]=0
    datos[23][11]=0
    datos[23][12]=0
    datos[23][13]=0
    datos[23][14]=0
    datos[23][15]=0
    datos[23][16]=0
    datos[23][17]=0
    datos[23][18]=10
    datos[23][19]=0
    datos[23][20]=0
    datos[23][21]=0
    datos[23][22]=7
    datos[23][23]=0
    datos[23][24]=0
    datos[23][25]=0
    datos[23][26]=0
    datos[23][27]=0
    datos[23][28]=0
    datos[23][29]=0
    datos[23][30]=0
    datos[23][31]=0
    datos[23][32]=0
    datos[23][33]=0
    datos[23][34]=0
    datos[23][35]=0
    datos[23][36]=0
    datos[23][37]=0
    datos[23][38]=0
    datos[23][39]=0
    datos[23][40]=0
    datos[23][41]=0

    # Fila 24
    datos[24][0]=0
    datos[24][1]=0
    datos[24][2]=0
    datos[24][3]=0
    datos[24][4]=0
    datos[24][5]=0
    datos[24][6]=0
    datos[24][7]=0
    datos[24][8]=0
    datos[24][9]=0
    datos[24][10]=0
    datos[24][11]=0
    datos[24][12]=0
    datos[24][13]=0
    datos[24][14]=0
    datos[24][15]=0
    datos[24][16]=0
    datos[24][17]=0
    datos[24][18]=0
    datos[24][19]=7
    datos[24][20]=0
    datos[24][21]=0
    datos[24][22]=0
    datos[24][23]=9
    datos[24][24]=0
    datos[24][25]=0
    datos[24][26]=0
    datos[24][27]=0
    datos[24][28]=0
    datos[24][29]=10
    datos[24][30]=0
    datos[24][31]=0
    datos[24][32]=0
    datos[24][33]=0
    datos[24][34]=0
    datos[24][35]=0
    datos[24][36]=0
    datos[24][37]=0
    datos[24][38]=0
    datos[24][39]=0
    datos[24][40]=0
    datos[24][41]=0

    # Fila 25
    datos[25][0]=0
    datos[25][1]=0
    datos[25][2]=0
    datos[25][3]=0
    datos[25][4]=0
    datos[25][5]=0
    datos[25][6]=0
    datos[25][7]=0
    datos[25][8]=0
    datos[25][9]=0
    datos[25][10]=0
    datos[25][11]=0
    datos[25][12]=0
    datos[25][13]=0
    datos[25][14]=0
    datos[25][15]=0
    datos[25][16]=0
    datos[25][17]=0
    datos[25][18]=0
    datos[25][19]=0
    datos[25][20]=9
    datos[25][21]=0
    datos[25][22]=0
    datos[25][23]=0
    datos[25][24]=0
    datos[25][25]=0
    datos[25][26]=11
    datos[25][27]=0
    datos[25][28]=0
    datos[25][29]=0
    datos[25][30]=0
    datos[25][31]=0
    datos[25][32]=0
    datos[25][33]=0
    datos[25][34]=0
    datos[25][35]=0
    datos[25][36]=0
    datos[25][37]=0
    datos[25][38]=0
    datos[25][39]=0
    datos[25][40]=0
    datos[25][41]=0

    # Fila 26
    datos[26][0]=0
    datos[26][1]=0
    datos[26][2]=0
    datos[26][3]=0
    datos[26][4]=0
    datos[26][5]=0
    datos[26][6]=0
    datos[26][7]=0
    datos[26][8]=0
    datos[26][9]=0
    datos[26][10]=0
    datos[26][11]=0
    datos[15][12]=0
    datos[26][13]=0
    datos[26][14]=0
    datos[26][15]=0
    datos[26][16]=0
    datos[26][17]=0
    datos[26][18]=0
    datos[26][19]=0
    datos[26][20]=0
    datos[26][21]=14
    datos[26][22]=0
    datos[26][23]=0
    datos[26][24]=0
    datos[26][25]=0
    datos[26][26]=0
    datos[26][27]=8
    datos[26][28]=0
    datos[26][29]=0
    datos[26][30]=0
    datos[26][31]=16
    datos[26][32]=0
    datos[26][33]=0
    datos[26][34]=0
    datos[26][35]=0
    datos[26][36]=0
    datos[26][37]=0
    datos[26][38]=0
    datos[26][39]=0
    datos[26][40]=0
    datos[26][41]=0

    # Fila 27
    datos[27][0]=0
    datos[27][1]=0
    datos[27][2]=0
    datos[27][3]=0
    datos[27][4]=0
    datos[27][5]=0
    datos[27][6]=0
    datos[27][7]=0
    datos[27][8]=0
    datos[27][9]=0
    datos[27][10]=0
    datos[27][11]=0
    datos[27][12]=0
    datos[27][13]=0
    datos[27][14]=0
    datos[27][15]=0
    datos[27][16]=0
    datos[27][17]=0
    datos[27][18]=0
    datos[27][19]=0
    datos[27][20]=0
    datos[27][21]=0
    datos[27][22]=0
    datos[27][23]=0
    datos[27][24]=0
    datos[27][25]=0
    datos[27][26]=0
    datos[27][27]=0
    datos[27][28]=13
    datos[27][29]=0
    datos[27][30]=0
    datos[27][31]=0
    datos[27][32]=17
    datos[27][33]=0
    datos[27][34]=0
    datos[27][35]=0
    datos[27][36]=0
    datos[27][37]=0
    datos[27][38]=0
    datos[27][39]=0
    datos[27][40]=0
    datos[27][41]=0

    # Fila 28
    datos[28][0]=0
    datos[28][1]=0
    datos[28][2]=0
    datos[28][3]=0
    datos[28][4]=0
    datos[28][5]=0
    datos[28][6]=0
    datos[28][7]=0
    datos[28][8]=0
    datos[28][9]=0
    datos[28][10]=0
    datos[28][11]=0
    datos[28][12]=0
    datos[28][13]=0
    datos[28][14]=0
    datos[28][15]=0
    datos[28][16]=0
    datos[28][17]=0
    datos[28][18]=0
    datos[28][19]=0
    datos[28][20]=0
    datos[28][21]=0
    datos[28][22]=0
    datos[28][23]=12
    datos[28][24]=0
    datos[28][25]=0
    datos[28][26]=0
    datos[28][27]=0
    datos[28][28]=0
    datos[28][29]=9
    datos[28][30]=0
    datos[28][31]=0
    datos[28][32]=0
    datos[28][33]=0
    datos[28][34]=0
    datos[28][35]=0
    datos[28][36]=0
    datos[28][37]=0
    datos[28][38]=0
    datos[28][39]=0
    datos[28][40]=0
    datos[28][41]=0

    # Fila 29
    datos[29][0]=0
    datos[29][1]=0
    datos[29][2]=0
    datos[29][3]=0
    datos[29][4]=0
    datos[29][5]=0
    datos[29][6]=0
    datos[29][7]=0
    datos[29][8]=0
    datos[29][9]=0
    datos[29][10]=0
    datos[29][11]=0
    datos[29][12]=0
    datos[29][13]=0
    datos[29][14]=0
    datos[29][15]=0
    datos[29][16]=0
    datos[29][17]=0
    datos[29][18]=0
    datos[29][19]=0
    datos[29][20]=0
    datos[29][21]=0
    datos[29][22]=0
    datos[29][23]=0
    datos[29][24]=15
    datos[29][25]=0
    datos[29][26]=0
    datos[29][27]=0
    datos[29][28]=0
    datos[29][29]=0
    datos[29][30]=0
    datos[29][31]=0
    datos[29][32]=0
    datos[29][33]=0
    datos[29][34]=12
    datos[29][35]=0
    datos[29][36]=0
    datos[29][37]=0
    datos[29][38]=0
    datos[29][39]=0
    datos[29][40]=9
    datos[29][41]=0

    # Fila 30
    datos[30][0]=0
    datos[30][1]=0
    datos[30][2]=0
    datos[30][3]=0
    datos[30][4]=0
    datos[30][5]=0
    datos[30][6]=0
    datos[30][7]=0
    datos[30][8]=0
    datos[30][9]=0
    datos[30][10]=0
    datos[30][11]=0
    datos[30][12]=0
    datos[30][13]=0
    datos[30][14]=0
    datos[30][15]=0
    datos[30][16]=0
    datos[30][17]=0
    datos[30][18]=0
    datos[30][19]=0
    datos[30][20]=0
    datos[30][21]=0
    datos[30][22]=0
    datos[30][23]=0
    datos[30][24]=0
    datos[30][25]=10
    datos[30][26]=0
    datos[30][27]=0
    datos[30][28]=0
    datos[30][29]=0
    datos[30][30]=0
    datos[30][31]=0
    datos[30][32]=0
    datos[30][33]=0
    datos[30][34]=0
    datos[30][35]=0
    datos[30][36]=0
    datos[30][37]=0
    datos[30][38]=0
    datos[30][39]=0
    datos[30][40]=0
    datos[30][41]=0

    # Fila 31
    datos[31][0]=0
    datos[31][1]=0
    datos[31][2]=0
    datos[31][3]=0
    datos[31][4]=0
    datos[31][5]=0
    datos[31][6]=0
    datos[31][7]=0
    datos[31][8]=0
    datos[31][9]=0
    datos[31][10]=0
    datos[31][11]=0
    datos[31][12]=0
    datos[31][13]=0
    datos[31][14]=0
    datos[31][15]=0
    datos[31][16]=0
    datos[31][17]=0
    datos[31][18]=0
    datos[31][19]=0
    datos[31][20]=0
    datos[31][21]=0
    datos[31][22]=0
    datos[31][23]=0
    datos[31][24]=0
    datos[31][25]=0
    datos[31][26]=17
    datos[31][27]=0
    datos[31][28]=0
    datos[31][29]=0
    datos[31][30]=12
    datos[31][31]=0
    datos[31][32]=0
    datos[31][33]=0
    datos[31][34]=0
    datos[31][35]=0
    datos[31][36]=0
    datos[31][37]=0
    datos[31][38]=0
    datos[31][39]=0
    datos[31][40]=0
    datos[31][41]=0

    # Fila 32
    datos[32][0]=0
    datos[32][1]=0
    datos[32][2]=0
    datos[32][3]=0
    datos[32][4]=0
    datos[32][5]=0
    datos[32][6]=0
    datos[32][7]=0
    datos[32][8]=0
    datos[32][9]=0
    datos[32][10]=0
    datos[32][11]=0
    datos[32][12]=0
    datos[32][13]=0
    datos[32][14]=0
    datos[32][15]=0
    datos[32][16]=0
    datos[32][17]=0
    datos[32][18]=0
    datos[32][19]=0
    datos[32][20]=0
    datos[32][21]=0
    datos[32][22]=0
    datos[32][23]=0
    datos[32][24]=0
    datos[32][25]=0
    datos[32][26]=0
    datos[32][27]=0
    datos[32][28]=0
    datos[32][29]=0
    datos[32][30]=0
    datos[32][31]=15
    datos[32][32]=0
    datos[32][33]=0
    datos[32][34]=0
    datos[32][35]=0
    datos[32][36]=0
    datos[32][37]=0
    datos[32][38]=0
    datos[32][39]=0
    datos[32][40]=0
    datos[32][41]=0

    # Fila 33
    datos[33][0]=0
    datos[33][1]=0
    datos[33][2]=0
    datos[33][3]=0
    datos[33][4]=0
    datos[33][5]=0
    datos[33][6]=0
    datos[33][7]=0
    datos[33][8]=0
    datos[33][9]=0
    datos[33][10]=0
    datos[33][11]=0
    datos[33][12]=0
    datos[33][13]=0
    datos[33][14]=0
    datos[33][15]=0
    datos[33][16]=0
    datos[33][17]=0
    datos[33][18]=0
    datos[33][19]=0
    datos[33][20]=0
    datos[33][21]=0
    datos[33][22]=0
    datos[33][23]=0
    datos[33][24]=0
    datos[33][25]=0
    datos[33][26]=0
    datos[33][27]=0
    datos[33][28]=8
    datos[33][29]=0
    datos[33][30]=0
    datos[33][31]=0
    datos[33][32]=11
    datos[33][33]=0
    datos[33][34]=0
    datos[33][35]=0
    datos[1][36]=0
    datos[1][37]=0
    datos[1][38]=0
    datos[1][39]=0
    datos[1][40]=0
    datos[1][41]=0

    # Fila 34
    datos[34][0]=0
    datos[34][1]=0
    datos[34][2]=0
    datos[34][3]=0
    datos[34][4]=0
    datos[34][5]=0
    datos[34][6]=0
    datos[34][7]=0
    datos[34][8]=0
    datos[34][9]=0
    datos[34][10]=0
    datos[34][11]=0
    datos[34][12]=0
    datos[34][13]=0
    datos[34][14]=0
    datos[34][15]=0
    datos[34][16]=0
    datos[34][17]=0
    datos[34][18]=0
    datos[34][19]=0
    datos[34][20]=0
    datos[34][21]=0
    datos[34][22]=0
    datos[34][23]=0
    datos[34][24]=0
    datos[34][25]=0
    datos[34][26]=0
    datos[34][27]=0
    datos[34][28]=0
    datos[34][29]=15
    datos[34][30]=0
    datos[34][31]=0
    datos[34][32]=0
    datos[34][33]=12
    datos[34][34]=0
    datos[34][35]=0
    datos[34][36]=0
    datos[34][37]=0
    datos[34][38]=0
    datos[34][39]=0
    datos[34][40]=0
    datos[34][41]=0

    # Fila 35
    datos[35][0]=0
    datos[35][1]=0
    datos[35][2]=0
    datos[35][3]=0
    datos[35][4]=0
    datos[35][5]=0
    datos[35][6]=0
    datos[35][7]=0
    datos[35][8]=0
    datos[35][9]=0
    datos[35][10]=0
    datos[35][11]=0
    datos[35][12]=0
    datos[35][13]=0
    datos[35][14]=0
    datos[35][15]=0
    datos[35][16]=0
    datos[35][17]=0
    datos[35][18]=0
    datos[35][19]=0
    datos[35][20]=0
    datos[35][21]=0
    datos[35][22]=0
    datos[35][23]=0
    datos[35][24]=0
    datos[35][25]=0
    datos[35][26]=0
    datos[35][27]=0
    datos[35][28]=0
    datos[35][29]=0
    datos[35][30]=0
    datos[35][31]=0
    datos[35][32]=0
    datos[35][33]=0
    datos[35][34]=0
    datos[35][35]=0
    datos[35][36]=7
    datos[35][37]=0
    datos[35][38]=0
    datos[35][39]=0
    datos[35][40]=0
    datos[35][41]=0

    # Fila 36
    datos[36][0]=0
    datos[36][1]=0
    datos[36][2]=0
    datos[36][3]=0
    datos[36][4]=0
    datos[36][5]=0
    datos[36][6]=0
    datos[36][7]=0
    datos[36][8]=0
    datos[36][9]=10
    datos[36][10]=0
    datos[36][11]=0
    datos[36][12]=0
    datos[36][13]=0
    datos[36][14]=0
    datos[36][15]=0
    datos[36][16]=0
    datos[36][17]=0
    datos[36][18]=0
    datos[36][19]=0
    datos[36][20]=0
    datos[36][21]=0
    datos[36][22]=0
    datos[36][23]=0
    datos[36][24]=0
    datos[36][25]=0
    datos[36][26]=0
    datos[36][27]=0
    datos[36][28]=0
    datos[36][29]=0
    datos[36][30]=0
    datos[36][31]=0
    datos[36][32]=0
    datos[36][33]=0
    datos[36][34]=0
    datos[36][35]=0
    datos[36][36]=0
    datos[36][37]=9
    datos[36][38]=0
    datos[36][39]=0
    datos[36][40]=0
    datos[36][41]=0

    # Fila 37
    datos[37][0]=0
    datos[37][1]=0
    datos[37][2]=0
    datos[37][3]=0
    datos[37][4]=0
    datos[37][5]=0
    datos[37][6]=0
    datos[37][7]=0
    datos[37][8]=0
    datos[37][9]=0
    datos[37][10]=0
    datos[37][11]=0
    datos[37][12]=0
    datos[37][13]=0
    datos[37][14]=0
    datos[37][15]=0
    datos[37][16]=0
    datos[37][17]=0
    datos[37][18]=0
    datos[37][19]=0
    datos[37][20]=0
    datos[37][21]=0
    datos[37][22]=0
    datos[37][23]=0
    datos[37][24]=0
    datos[37][25]=0
    datos[37][26]=0
    datos[37][27]=0
    datos[37][28]=0
    datos[37][29]=0
    datos[37][30]=0
    datos[37][31]=0
    datos[37][32]=0
    datos[37][33]=0
    datos[37][34]=0
    datos[37][35]=0
    datos[37][36]=0
    datos[37][37]=0
    datos[37][38]=11
    datos[37][39]=0
    datos[37][40]=0
    datos[37][41]=0

    # Fila 38
    datos[38][0]=0
    datos[38][1]=0
    datos[38][2]=0
    datos[38][3]=0
    datos[38][4]=0
    datos[38][5]=0
    datos[38][6]=0
    datos[38][7]=0
    datos[38][8]=0
    datos[38][9]=0
    datos[38][10]=0
    datos[38][11]=0
    datos[38][12]=0
    datos[38][13]=0
    datos[38][14]=0
    datos[38][15]=0
    datos[38][16]=0
    datos[38][17]=0
    datos[38][18]=0
    datos[38][19]=10
    datos[38][20]=0
    datos[38][21]=0
    datos[38][22]=0
    datos[38][23]=0
    datos[38][24]=0
    datos[38][25]=0
    datos[38][26]=0
    datos[38][27]=0
    datos[38][28]=0
    datos[38][29]=0
    datos[38][30]=0
    datos[38][31]=0
    datos[38][32]=0
    datos[38][33]=0
    datos[38][34]=0
    datos[38][35]=0
    datos[38][36]=0
    datos[38][37]=0
    datos[38][38]=0
    datos[38][39]=8
    datos[38][40]=0
    datos[38][41]=0

    # Fila 39
    datos[39][0]=0
    datos[39][1]=0
    datos[39][2]=0
    datos[39][3]=0
    datos[39][4]=0
    datos[39][5]=0
    datos[39][6]=0
    datos[39][7]=0
    datos[39][8]=0
    datos[39][9]=0
    datos[39][10]=0
    datos[39][11]=0
    datos[39][12]=0
    datos[39][13]=0
    datos[39][14]=0
    datos[39][15]=0
    datos[39][16]=0
    datos[39][17]=0
    datos[39][18]=0
    datos[39][19]=0
    datos[39][20]=0
    datos[39][21]=0
    datos[39][22]=0
    datos[39][23]=0
    datos[39][24]=13
    datos[39][25]=0
    datos[39][26]=0
    datos[39][27]=0
    datos[39][28]=0
    datos[39][29]=0
    datos[39][30]=0
    datos[39][31]=0
    datos[39][32]=0
    datos[39][33]=0
    datos[39][34]=0
    datos[39][35]=0
    datos[39][36]=0
    datos[39][37]=0
    datos[39][38]=0
    datos[39][39]=0
    datos[39][40]=15
    datos[39][41]=0

    # Fila 40
    datos[40][0]=0
    datos[40][1]=0
    datos[40][2]=0
    datos[40][3]=0
    datos[40][4]=0
    datos[40][5]=0
    datos[40][6]=0
    datos[40][7]=0
    datos[40][8]=0
    datos[40][9]=0
    datos[40][10]=0
    datos[40][11]=0
    datos[40][12]=0
    datos[40][13]=0
    datos[40][14]=0
    datos[40][15]=0
    datos[40][16]=0
    datos[40][17]=0
    datos[40][18]=0
    datos[40][19]=0
    datos[40][20]=0
    datos[40][21]=0
    datos[40][22]=0
    datos[40][23]=0
    datos[40][24]=0
    datos[40][25]=0
    datos[40][26]=0
    datos[40][27]=0
    datos[40][28]=0
    datos[40][29]=0
    datos[40][30]=0
    datos[40][31]=0
    datos[40][32]=0
    datos[40][33]=0
    datos[40][34]=0
    datos[40][35]=0
    datos[40][36]=0
    datos[40][37]=0
    datos[40][38]=0
    datos[40][39]=0
    datos[40][40]=0
    datos[40][41]=7

    # Fila 41
    datos[41][0]=0
    datos[41][1]=0
    datos[41][2]=0
    datos[41][3]=0
    datos[41][4]=0
    datos[41][5]=0
    datos[41][6]=0
    datos[41][7]=0
    datos[41][8]=0
    datos[41][9]=0
    datos[41][10]=0
    datos[41][11]=0
    datos[41][12]=0
    datos[41][13]=0
    datos[41][14]=0
    datos[41][15]=0
    datos[41][16]=0
    datos[41][17]=0
    datos[41][18]=0
    datos[41][19]=0
    datos[41][20]=0
    datos[41][21]=0
    datos[41][22]=0
    datos[41][23]=0
    datos[41][24]=0
    datos[41][25]=0
    datos[41][26]=0
    datos[41][27]=0
    datos[41][28]=0
    datos[41][29]=0
    datos[41][30]=0
    datos[41][31]=0
    datos[41][32]=0
    datos[41][33]=0
    datos[41][34]=17
    datos[41][35]=0
    datos[41][36]=0
    datos[41][37]=0
    datos[41][38]=0
    datos[41][39]=0
    datos[41][40]=0
    datos[41][41]=0
    return datos
