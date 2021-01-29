class Estudiante():
    
    '''
    Atributos
    '''
    nombre = None
    edad = None
    numero_cel = None
    entrega_trabajos = None
    direccion = None
    juega = None
    lee = None
    estatura = None
    analiza = None
    tez = None

    def __init__(self):
        print("clase Estudiante")
    
    '''
    Metodos
    '''
    
    def comer(self):
        print("Metodo comer")
    
    def estudiar(self):
        print("Metodo estudiar")

    def dormir(self):
        print("Metodo dormir")

    def despertar(self):
        print("Metodo Despertar")

    def caminar(self):
        print("Metodo caminar")
   

# Creacion de un objeto basado en una clase
Alumno = Estudiante()

# Asiganacion de valores a las propiedades
Alumno.nombre = "Jesus Antonio Diaz Cruz"
Alumno.edad = "19 años"
Alumno.numero_cel = "7752061755"
Alumno.entrega_trabajos = "si"
Alumno.direccion = "Santa Maria el chico Mpo. Tulancingo"
Alumno.juega= "si"
Alumno.lee = "si"
Alumno.estatura = "1.76"
Alumno.analiza = "si"
Alumno.tez = "guero"

# Imprimir valore de las propiedades
print(Alumno.nombre )
print(Alumno.edad)
print(Alumno.numero_cel )
print(Alumno.entrega_trabajos)
print(Alumno.direccion)
print(Alumno.juega)
print(Alumno.lee)
print(Alumno.estatura)
print(Alumno.analiza)
print(Alumno.tez)

# Invocar metodos de la clase
Alumno.comer()
Alumno.estudiar()
Alumno.dormir()
Alumno.despertar()
Alumno.caminar()

