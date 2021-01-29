class Cajero_Automatico():
    
    '''
    Atributos
    '''
    marca  = None
    establecimiento   = None
    compania = None
    color = None
    tamano = None
    funcionamiento  = None
    tiempo_de_funcionamiento = None
    modelo = None
    pantalla_tactil = None
    botones = None
    
    

    def __init__(self):
        print("clase Cajero_Automatico")
    
    '''
    Metodos
    '''
    
    def cotizar(self):
        print("Metodo cotizar")
    
    def prender(self):
        print("Metodo prender")

    def recibir(self):
        print("Metodo recibir")

    def dar_dinero(self):
        print("Metodo dar_dinero")

    def apagar(self):
        print("Metodo apagar")
   

# Creacion de un objeto basado en una clase
cajero_banamex = Cajero_Automatico()

# Asiganacion de valores a las propiedades
cajero_banamex.marca = "Banamex"
cajero_banamex.establecimiento = "Tulancingo centro"
cajero_banamex.compania = "BBVA"
cajero_banamex.color = "Gris"
cajero_banamex.tamano = "Grande"
cajero_banamex.funcionamiento = "si funciona"
cajero_banamex.tiempo_de_funcionamiento = "20/7"
cajero_banamex.modelo = "normal"
cajero_banamex.pantalla_tactil = "si"
cajero_banamex.botones = "si"


# Imprimir valores de las propiedades
print(cajero_banamex.marca)
print(cajero_banamex.establecimiento)
print(cajero_banamex.compania)
print(cajero_banamex.color)
print(cajero_banamex.tamano)
print(cajero_banamex.funcionamiento)
print(cajero_banamex.tiempo_de_funcionamiento)
print(cajero_banamex.modelo)
print(cajero_banamex.pantalla_tactil)
print(cajero_banamex.botones)

# Invocar metodos de la clase
cajero_banamex.cotizar()
cajero_banamex.prender ()
cajero_banamex.recibir ()
cajero_banamex.dar_dinero ()
cajero_banamex.apagar ()
