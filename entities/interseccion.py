# interseccion es como city o Ciudad
from dataclasses import dataclass
import math

@dataclass(eq=True, frozen=True)
class Interseccion:
    name: str   #con esto vamos a nombrar un nodo interseccion.
    x: int      #Aqui le damos una ubicacion X, lo mismo q podria luego ser longitud.
    y: int      #Aqui le damos una ubicacion Y, lo mismo que podria luego ser latitud.
    distancia: int
        