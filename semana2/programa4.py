class Vacaciones():
    
    '''
    Atributos
    '''
    compras = None
    relajacion = None
    recuerdos = None
    lugar= None
    periodo_vacacional = None
    familiares = None
    ambiente = None
    juegos = None
    tiempo = None
    visitas = None

    def __init__(self):
        print("clase vacaciones")
    
    '''
    Metodos
    '''
    
    def planear(self):
        print("Metodo Planear")
    
    def ahorrar(self):
        print("Metodo ahorrar")

    def viajar(self):
        print("Metodo viajar")

    def disfrutar(self):
        print("Metodo disfrutar")

    def regresar(self):
        print("Metodo regresar")
   

# Creacion de un objeto basado en una clase
Nevada = Vacaciones()

# Asiganacion de valores a las propiedades
Nevada.compras = "muchas"
Nevada.relajacion = "si"
Nevada.recuerdos= "si"
Nevada.lugar = "Toluca"
Nevada.periodo_vacacional = "30-diciembre - 6-enero"
Nevada.familiar = "si"
Nevada.ambiente = "frio"
Nevada.juegos = "si"
Nevada.tiempo = "144hrs"
Nevada.visitas = "si"

# Imprimir valore de las propiedades
print(Nevada.compras )
print(Nevada.relajacion)
print(Nevada.recuerdos)
print(Nevada.lugar)
print(Nevada.periodo_vacacional)
print(Nevada.familiar)
print(Nevada.ambiente)
print(Nevada.juegos)
print(Nevada.tiempo)
print(Nevada.visitas)

# Invocar metodos de la clase
Nevada.planear()
Nevada.ahorrar()
Nevada.viajar()
Nevada.disfrutar()
Nevada.regresar()
