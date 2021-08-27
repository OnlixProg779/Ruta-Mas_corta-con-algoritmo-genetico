# from utils import genera_poblacion, generate_intersecciones, selecciona_padres, cruza, muta

from algoritmos import crearRutas, iniciarMatriz, selecciona_padres, cruza
from ruta import Ruta

matriz = iniciarMatriz()
poblacion = []
iteracionPoblacion = 10000
puntoInicial = 'b'
puntoFinal = 's'
seleccion = 10
generaciones = 20

#Genera Poblacion
for _ in range(iteracionPoblacion):
    aux = (crearRutas(matriz, puntoInicial, puntoFinal))
    if(aux not in poblacion and aux[len(aux)-1].name == puntoFinal):
        poblacion.append(Ruta(aux)) #aqui se crea una ruta q pase por todas las intersecciones y se agrega a ruta, hace esto segun el tamaño de la poblacion que especificamos

        #poblacion.append(aux)

print("POBLACION")
# generar_poblacion(matriz, poblacion, 10, 'g', 's')
for i in range(len(poblacion)):
    print(poblacion[i].intersecciones)
    print('DistanciaTotal = ' +str(poblacion[i].distancia))
    print()

for generacion_id in range(generaciones):
    # mejor_ruta = sorted(poblacion, key=lambda ruta: ruta.distancia)[0]
    # print(f"{generacion_id}: {mejor_ruta.distancia:.3f}")
    print()
    print("SELECCION")
    if(len(poblacion)>seleccion):
        padres_seleccionados = selecciona_padres(poblacion,seleccion) #se le indica que devuelva los 10 mejores en funcion a la distancia.
    print(len(padres_seleccionados))
    for i in range(len(padres_seleccionados)):
        if(i == 0):
            print(padres_seleccionados[i].intersecciones)
            print('Generacion: '+str(generacion_id +1)+' DistanciaTotal = ' +str(padres_seleccionados[i].distancia))
            print()

    print("CRUCE y MUTACION")
    nuevos_hijos = cruza(padres_seleccionados, 20)#enviamos las mejores rutas
    print(len(nuevos_hijos))


    # print("SELECCION")
    # if(len(nuevos_hijos)>seleccion):
    #     ver_optimos = selecciona_padres(nuevos_hijos,30) #se le indica que devuelva los 10 mejores en funcion a la distancia.
    # print(len(ver_optimos))
    # for i in range(len(ver_optimos)):
    #     if(i == 0):
    #         print(ver_optimos[i].intersecciones)
    #         print('Generacion: '+str(generacion_id)+' DistanciaTotal = ' +str(ver_optimos[i].distancia))
    #         print()

    print("NUEVA POBLACION")
    poblacion = nuevos_hijos










# todas_intersecciones = generate_intersecciones(50, 0 ,0 , 100, 100)





# #Generacion de poblacion
# poblacion = genera_poblacion(todas_intersecciones, 50)
# print(len(poblacion))


# for generacion_id in range(1000):
#     mejor_ruta = sorted(poblacion, key=lambda ruta: ruta.distancia)[0]
#     print(f"{generacion_id}: {mejor_ruta.distancia:.3f}")
#     
#     #Seleccion
#     padres_seleccionados = selecciona_padres(poblacion,10) #se le indica que devuelva los 10 mejores en funcion a la distancia.
#     #print(len(padres_seleccionados))

#     #Cruce
#     nuevos_hijos = cruza(padres_seleccionados, 50)
#     #print(len(nuevos_hijos))

#     #Mutacion
#     hijos_mutados = muta(nuevos_hijos)

#     #Nueva Poblacion
#     poblacion = padres_seleccionados + hijos_mutados
#     #print(len(poblacion))

