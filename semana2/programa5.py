class Serie_TV():
    
    '''
    Atributos
    '''
    tiempo_por_episodio = None
    Canal_de_transmisión  = None
    tiempo_de_duracion = None
    tiempo_de_serie = None
    numero_de_episodios = None
    numero_de_temporadas = None
    emociones= None
    a_quien_va_dirigida = None
    director = None
    personajes = None

    def __init__(self):
        print("clase Serie_TV")
    
    '''
    Metodos
    '''
    
    def planear(self):
        print("Metodo Planear")
    
    def cotizar(self):
        print("Metodo cotizar")

    def estacionar(self):
        print("Metodo estacionar")

    def transmitir(self):
        print("Metodo transmitir")

    def enfocar(self):
        print("Metodo enfocar")
   

# Creacion de un objeto basado en una clase
Caballeros_zodiaco  = Serie_TV()

# Asiganacion de valores a las propiedades
Caballeros_zodiaco .tiempo_por_episodio = "4945hrs"
Caballeros_zodiaco .canal_de_transmicion = "canal BitMe"
Caballeros_zodiaco .tiempo_de_duracion= "43hrs"
Caballeros_zodiaco.tiempo_de_serie = "20 años"
Caballeros_zodiaco.numero_de_episodios = 115
Caballeros_zodiaco.numero_de_temporadas = "7"
Caballeros_zodiaco.emociones = "accion"
Caballeros_zodiaco.director = "Sain Seiya"
Caballeros_zodiaco.personajes = "si"

# Imprimir valores de las propiedades
print(Caballeros_zodiaco .tiempo_por_episodio)
print(Caballeros_zodiaco .canal_de_transmicion)
print(Caballeros_zodiaco .tiempo_de_duracion)
print(Caballeros_zodiaco.tiempo_de_serie)
print(Caballeros_zodiaco.numero_de_episodios)
print(Caballeros_zodiaco.numero_de_temporadas)
print(Caballeros_zodiaco.emociones)
print(Caballeros_zodiaco.director)
print(Caballeros_zodiaco.personajes )

# Invocar metodos de la clase
Caballeros_zodiaco.planear ()
Caballeros_zodiaco.cotizar ()
Caballeros_zodiaco.estacionar ()
Caballeros_zodiaco.transmitir ()
Caballeros_zodiaco.enfocar ()
