import math

r = float (input ('digite o tamanho do raio de uma esfera para calcular o tamanho do raio para uma esfera com o volume 40% maior:'))
volume = ( 4 / 3 ) * ( math.pi*r**3 )
raio = ( volume * 0.4 * 3 ) / (math.pi * 4 ) 
print ( raio )