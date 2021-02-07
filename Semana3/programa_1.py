from math import sqrt
class Punto:
  
 def distancia(x1,y1,x2,y2):
  resultado = sqrt((x2-x1)**2+(y2-y1)**2)
  print (round(resultado,2)) 
  
 distancia(88.7,118.3,295.3,18.4) 
objeto_Punto = Punto()
resultado = objeto_Punto.distancia
