class Banco():
    
    '''
    Atributos
    '''
    compania = None
    color = None
    espacio = None
    tiempo_disponible = None
    servicios = None
    cajeros = None
    ventanillas = None
    lugar = None
    clientes = None
    personal = None

    def __init__(self):
        print("clase Banco")
    
    '''
    Metodos
    '''
    
    def abrir(self):
        print("Metodo abrir")
    
    def atender(self):
        print("Metodo atender")

    def entregar_dinero(self):
        print("Metodo entregar_dinero")

    def recibir_dinero(self):
        print("Metodo recibir_dinero")

    def cerrar(self):
        print("Metodo cerrar")
   

# Creacion de un objeto basado en una clase
Scotiabank = Banco()

# Asiganacion de valores a las propiedades
Scotiabank.compania = "Scotiabank"
Scotiabank.color = "rojo y blanco"
Scotiabank.espacio = "grande"
Scotiabank.tiempo_disponible = "lunes a viernes de 10am-9pm"
Scotiabank.servcicios = "Si"
Scotiabank.cajeros = "Si"
Scotiabank.ventanillas = "si"
Scotiabank.lugar = "Pachuca Hgo"
Scotiabank.clientes = "Si"
Scotiabank.personas = "Si"

# Imprimir valore de las propiedades
print(Scotiabank.compania)
print(Scotiabank.color)
print(Scotiabank.espacio)
print(Scotiabank.tiempo_disponible)
print(Scotiabank.servcicios)
print(Scotiabank.cajeros)
print(Scotiabank.ventanillas)
print(Scotiabank.lugar)
print(Scotiabank.clientes)
print(Scotiabank.personas)

# Invocar metodos de la clase
Scotiabank.abrir()
Scotiabank.atender()
Scotiabank.entregar_dinero()
Scotiabank.recibir_dinero()
Scotiabank.cerrar()
