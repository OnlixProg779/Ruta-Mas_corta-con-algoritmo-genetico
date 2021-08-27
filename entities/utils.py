#Este archivo debe permitir leer la data proveniente de el archivo csv 
import csv
import random
from interseccion import Interseccion
from ruta import Ruta
from copy import deepcopy
from typing import List, Sequence, Set, Tuple


#El archivo CSV debe contener nodos, que indica los nodos q tiene a disposicion, y la distancia entre cada unos de ellos
def generate_intersecciones(
    interseccion_count: int, minx:int, miny:int, maxx:int, maxy:int
):
    intersecciones = set()
    with open("data.csv", encoding="utf8") as readable:
        reader = csv.reader(readable)
        for raw_data in reader:
             x = random.randint(minx,maxx)
             y = random.randint(miny,maxy)
             intersecciones.add(Interseccion(name=raw_data[0], x=x, y=y))
    return set(random.sample(intersecciones, interseccion_count))

#Este metodo genera una poblacion a partir de las intersecciones.
def genera_poblacion(intersecciones, pop_size): #pop_siz es el tamaño de la poblacion
    poblacion = []
    for _ in range(pop_size):
        poblacion.append(
            Ruta(random.sample(intersecciones, len(intersecciones))) #aqui se crea una ruta q pase por todas las intersecciones y se agrega a ruta, hace esto segun el tamaño de la poblacion que especificamos
        )
    return poblacion

#Ordena la poblacion en funcion a la distancia y devuelve los n_padres q se le indique
def selecciona_padres(poblacion, n_padres):
    ordenados_por_distancia = sorted(poblacion, key=lambda ruta: ruta.distancia)
    return ordenados_por_distancia[:n_padres]


#Metodo privado
def _cruza_dos_padres(padre1, padre2):#Aqui se especifica el tratamiento de cruce exclusivo para el problema de optimizacion de ruta
     hijo = deepcopy(padre2); #genera una copia del padre2
     
     elementos = 3
     
     for posicion_p1, valor_p1 in enumerate(padre1):
         posicion_p2 = hijo.index(valor_p1)
         hijo[posicion_p2] = hijo[posicion_p1]
         hijo[posicion_p1] = valor_p1
         
     return hijo    
    
     

def cruza(mejores_padres, pop_size): #Recibe los padres y se define el tamaño de la poblacion
    hijos_faltantes = pop_size - len(mejores_padres)
    nuevos_hijos = []
    for _ in range(hijos_faltantes):
        padre1, padre2 = random.sample(mejores_padres, 2) #Aqui se define como se podria generar los nuevos hijos
        nuevo_hijo = Ruta(_cruza_dos_padres(padre1.intersecciones, padre2.intersecciones))
        
        nuevos_hijos.append(nuevo_hijo)
    return nuevos_hijos

def _swap(route: Sequence, to: int, frm: int):
    aux = route[to]
    route[to] = route[frm]
    route[frm] = aux
    
    
def muta(nuevos_hijos):
    hijos_mutados = []
    for hijo in nuevos_hijos:
        nuevas_intersecciones = deepcopy(hijo.intersecciones)
        
        if 0.6 > random.random(): #si obtenemos una probabilidad menor a 0.5 se realiza la mutacion
            swap_from = random.randint(0, len(nuevas_intersecciones) - 1)
            swap_to = random.randint(0, len(nuevas_intersecciones) - 1)
            while swap_to == swap_from:
                swap_to = random.randint(0, len(nuevas_intersecciones) - 1)
            _swap(nuevas_intersecciones, swap_to, swap_from)
        hijos_mutados.append(Ruta(nuevas_intersecciones))
    return hijos_mutados

