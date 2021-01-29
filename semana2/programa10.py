class Google_Classroom():
    
    '''
    Atributos
    '''
    logo  = None
    uso   = None
    publicaciones= None
    tareas= None
    comentarios = None
    mensajes  = None
    archivos = None
    links = None
    personas = None
    grupos = None
    
    def __init__(self):
        print("clase Google_Classroom")
    
    '''
    Metodos
    '''
    
    def almacenar(self):
        print("Metodo almacenar")
    
    def descargar(self):
        print("Metodo descargar")

    def aplicar(self):
        print("Metodo aplicar")

    def comentar(self):
        print("Metodo comentar")

    def subir_tareas(self):
        print("Metodosubir_tareas")
   

# Creacion de un objeto basado en una clase
classroom = Google_Classroom()

# Asiganacion de valores a las propiedades
classroom.logo = "si"
classroom.uso = "escolar y profesional"
classroom.publicaciones = "si"
classroom.tareas = "si"
classroom.comentarios = "si"
classroom.mensajes = "si"
classroom.archivos = "si"
classroom.links = "si"
classroom.personas= "si"
classroom.grupos= "si"


# Imprimir valores de las propiedades
print(classroom.logo)
print(classroom.uso)
print(classroom.publicaciones)
print(classroom.tareas)
print(classroom.comentarios)
print(classroom.mensajes)
print(classroom.archivos)
print(classroom.links)
print(classroom.personas)
print(classroom.grupos)


# Invocar metodos de la clase
classroom.almacenar()
classroom.descargar()
classroom.aplicar ()
classroom.comentar ()
classroom.subir_tareas ()
