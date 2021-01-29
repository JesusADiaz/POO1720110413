class Futbolista():
    
    '''
    Atributos
    '''
    idi = None
    edad  = None
    estatura = None
    numero_del_dorsal = None
    tiempo_de_juego = None
    equipo = None
    uniforme = None
    posicion_que_juega = None
    origen = None
    matricula = None

    def __init__(self):
        print("clase Futbolista")
    
    '''
    Metodos
    '''
    
    def comer(self):
        print("Metodo comer")
    
    def respirar(self):
        print("Metodo respirar")

    def jugar(self):
        print("Metodo jugar")

    def descansar(self):
        print("Metodo descansar")

    def dormir(self):
        print("Metodo dormir")
   

# Creacion de un objeto basado en una clase
Jesus_Corona  = Futbolista()

# Asiganacion de valores a las propiedades
Jesus_Corona.idi = "8415"
Jesus_Corona.edad = "40 años"
Jesus_Corona.estatura= "1.84m"
Jesus_Corona.numero_del_dorsal= "1"
Jesus_Corona.tiempo_de_juego = "17 años"
Jesus_Corona.equipo = "Cruz Azul"
Jesus_Corona.uniforme = "si"
Jesus_Corona.posicion_que_juega = "Portero"
Jesus_Corona.origen = "Guadalajara.Mexico"
Jesus_Corona.matricula= "2054189742"

# Imprimir valores de las propiedades
print(Jesus_Corona.idi )
print(Jesus_Corona.edad)
print(Jesus_Corona.estatura)
print(Jesus_Corona.numero_del_dorsal)
print(Jesus_Corona.tiempo_de_juego)
print(Jesus_Corona.equipo )
print(Jesus_Corona.uniforme)
print(Jesus_Corona.posicion_que_juega)
print(Jesus_Corona.origen)
print(Jesus_Corona.matricula )

# Invocar metodos de la clase
Jesus_Corona.comer ()
Jesus_Corona.respirar()
Jesus_Corona.jugar()
Jesus_Corona.descansar ()
Jesus_Corona.dormir()
