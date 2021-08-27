from interseccion import Interseccion

class Ruta:     #este es un cromosoma
    
    def __init__(self, intersecciones): # cada ruta acepta una lista de intersecciones
        self.intersecciones = intersecciones
        self.distancia = 0
        for i in range(len(self.intersecciones)):
            self.distancia = self.distancia + self.intersecciones[i].distancia
        # pass
    
    