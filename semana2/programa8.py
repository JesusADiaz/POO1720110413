class Calculadora():
    
    '''
    Atributos
    '''
    marca  = None
    color   = None
    normal = None
    tamano = None
    cientifica= None
    material  = None
    tipo_de_botones = None
    fabricacion = None
    uso = None
    lenguaje = None
    
    

    def __init__(self):
        print("clase calculadora")
    
    '''
    Metodos
    '''
    
    def cotizar(self):
        print("Metodo cotizar")
    
    def prender(self):
        print("Metodo prender")

    def calcular(self):
        print("Metodo calcular")

    def resultar(self):
        print("Metodo resultar")

    def apagar(self):
        print("Metodo apagar")
   

# Creacion de un objeto basado en una clase
Casio_FX82MS = Calculadora()

# Asiganacion de valores a las propiedades
Casio_FX82MS.marca = "Casio"
Casio_FX82MS.color = "Gris"
Casio_FX82MS.normal = "No"
Casio_FX82MS.tamano = "Mediana"
Casio_FX82MS.cientifica = "si"
Casio_FX82MS.material = "Plastico"
Casio_FX82MS.tipo_de_botones = "redondos de goma"
Casio_FX82MS.fabricacion = "Casio"
Casio_FX82MS.uso = "Escuela"
Casio_FX82MS.lenjuage = "Basic-Clasico"

# Imprimir valores de las propiedades
print(Casio_FX82MS.marca)
print(Casio_FX82MS.color)
print(Casio_FX82MS.normal)
print(Casio_FX82MS.tamano)
print(Casio_FX82MS.cientifica)
print(Casio_FX82MS.material)
print(Casio_FX82MS.tipo_de_botones)
print(Casio_FX82MS.fabricacion)
print(Casio_FX82MS.uso)
print(Casio_FX82MS.lenjuage)

# Invocar metodos de la clase
Casio_FX82MS.cotizar ()
Casio_FX82MS.prender ()
Casio_FX82MS.calcular ()
Casio_FX82MS.resultar ()
Casio_FX82MS.apagar ()


