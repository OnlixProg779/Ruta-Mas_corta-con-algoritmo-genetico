# from utils import genera_poblacion, generate_intersecciones, selecciona_padres, cruza, muta

from algoritmos import crearRutas, iniciarMatriz, selecciona_padres, cruza
from ruta import Ruta

matriz = iniciarMatriz()
poblacion = []
iteracionPoblacion = 1000
puntoInicial = 'g'
puntoFinal = 'x'
seleccion = 30
generaciones = 20

#Genera Poblacion
for _ in range(iteracionPoblacion):
    aux = (crearRutas(matriz, puntoInicial, puntoFinal))
    if(aux not in poblacion and aux[len(aux)-1].name == puntoFinal):
        poblacion.append(Ruta(aux)) #aqui se crea una ruta q pase por todas las intersecciones y se agrega a ruta, hace esto segun el tamaño de la poblacion que especificamos

        #poblacion.append(aux)

print("------------------------------------------------INICIO DE PRIMERA GENERACION POBLACION----------------------------------------")
# generar_poblacion(matriz, poblacion, 10, 'g', 's')
for i in range(len(poblacion)):
    print(poblacion[i].intersecciones)
    print('DistanciaTotal = ' +str(poblacion[i].distancia))
    print()
print("------------------------------------------------FIN DE PRIMERA GENERACION POBLACION----------------------------------------")

print()
print("SELECCION DE GENERACION 1")
if(len(poblacion)>seleccion):
    padres_seleccionados = selecciona_padres(poblacion,seleccion) #se le indica que devuelva los 10 mejores en funcion a la distancia.

for generacion_id in range(generaciones):
    # mejor_ruta = sorted(poblacion, key=lambda ruta: ruta.distancia)[0]
    # print(f"{generacion_id}: {mejor_ruta.distancia:.3f}")
   # print(len(padres_seleccionados))
    print()
    print("MEJOR DE LA GENERACION "+str(generacion_id +1))

    for i in range(len(padres_seleccionados)):
        if(i == 0):
            print(padres_seleccionados[i].intersecciones)
            print('Generacion: '+str(generacion_id +1)+' DistanciaTotal = ' +str(padres_seleccionados[i].distancia))


    print("REALIZANDO CRUCE y MUTACION =======> ")
    nuevos_hijos = cruza(padres_seleccionados, 20)#enviamos las mejores rutas
    print(len(nuevos_hijos))


    print("RECOPILANDO NUEVOS SELECCIONADOS =========>")
    if(len(nuevos_hijos)>=seleccion):
        padres_seleccionados = selecciona_padres(nuevos_hijos,seleccion) #se le indica que devuelva los 10 mejores en funcion a la distancia.
        # print(len(ver_optimos))
        # for i in range(len(ver_optimos)):
        #     if(i == 0):
        #         print(ver_optimos[i].intersecciones)
        #         print('Generacion: '+str(generacion_id)+' DistanciaTotal = ' +str(ver_optimos[i].distancia))
        #         print()

    print(">>>>>>>>>>>>>> POBLACION PARA LA SIGUIENTE GENERACION GERERADA <<<<<<<<<<<<<<<")
    # poblacion = nuevos_hijos
    # print(len(poblacion))
print(">>>>>>>>>>>>>> SOLUCION FINAL <<<<<<<<<<<<<<<")
for i in range(len(padres_seleccionados)):
        if(i == 0):
            print(padres_seleccionados[i].intersecciones)
            print('Generacion: '+str(generaciones)+' DistanciaTotal = ' +str(padres_seleccionados[i].distancia))




