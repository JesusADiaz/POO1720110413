class Avion():
    
    '''
    Atributos
    '''
    usos_especiales = None
    marca = None
    tamaño = None
    vuela_alto = None
    velocidad = None
    numero_de_motores = None
    tamano_de_alas = None
    tipo_de_conbustible = None
    capacidad_de_personas = None
    trayectos_largos_en_menos_tiempo = None

    def __init__(self):
        print("clase Avion")
    
    '''
    Metodos
    '''
    
    def encender(self):
        print("Metodo Encender")
    
    def acelerar(self):
        print("Metodo acelerar")

    def volar(self):
        print("Metodo volar")

    def frenar(self):
        print("Metodo frenar")

    def apagar(self):
        print("Metodo apagar")
   

# Creacion de un objeto basado en una clase
comercial = Avion()

# Asiganacion de valores a las propiedades
comercial.usos_especiales = "no"
comercial.marca = "Boeing 747-400. "
comercial.tamano = "Grande"
comercial.vuela_alto = "si"
comercial.velocidad = "900k/h"
comercial.numero_de_motores = 1
comercial.tamano_de_alas = "70,77"
comercial.tipo_de_combustible = "queroseno"
comercial.capacidad_de_personas = " 568 pasajeros"
comercial.trayectos_largos_en_mayor_tiempo= "si"


# Imprimir valores de las propiedades
print(comercial.usos_especiales )
print(comercial.marca)
print(comercial.tamano)
print(comercial.vuela_alto)
print(comercial.velocidad)
print(comercial.numero_de_motores)
print(comercial.tamano_de_alas)
print(comercial.tipo_de_combustible)
print(comercial.capacidad_de_personas)
print(comercial.trayectos_largos_en_mayor_tiempo)

# Invocar metodos de la clase
comercial.encender()
comercial.acelerar()
comercial.volar()
comercial.frenar()
comercial.apagar()
