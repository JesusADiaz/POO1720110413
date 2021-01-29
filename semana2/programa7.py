class Coche():
    
    '''
    Atributos
    '''
    color  = None
    marca   = None
    número_de_serie = None
    máxima_velocidad = None
    motor = None
    frenos  = None
    transmisión = None
    tipo_de_combustible = None
    kilometraje = None
    electrico = None

    def __init__(self):
        print("clase Coche")
    
    '''
    Metodos
    '''
    
    def encender(self):
        print("Metodo encender")

    def acelerar(self):
        print("Metodo acelerar")

    def transportar(self):
        print("Metodo transportar")    

    def frenar(self):
        print("Metodo frenar")
  
    def apagar(self):
        print("Metodo apagar")    
   

# Creacion de un objeto basado en una clase
Ferrari  = Coche()

# Asiganacion de valores a las propiedades
Ferrari .color = "rojo"
Ferrari .marca = "Ferrari F430"
Ferrari .numero_de_serie = "ZFFEW59A180163993"
Ferrari .maxima_velocidad = "315km/h"
Ferrari .motor = "motor V8"
Ferrari .frenos = "si"
Ferrari .transmision = " manual y una semiautomática secuencial tipo F1"
Ferrari .tipo_de_combustible= "Gasolina"
Ferrari .kilometraje = "si"
Ferrari .electrico = "no"


# Imprimir valores de las propiedades
print(Ferrari .color)
print(Ferrari .marca)
print(Ferrari .numero_de_serie)
print(Ferrari .maxima_velocidad)
print(Ferrari .motor)
print(Ferrari .frenos)
print(Ferrari .transmision)
print(Ferrari .tipo_de_combustible)
print(Ferrari .kilometraje)
print(Ferrari .electrico )

# Invocar metodos de la clase
Ferrari .encender ()
Ferrari .acelerar()
Ferrari .transportar()
Ferrari .frenar ()
Ferrari .apagar()



