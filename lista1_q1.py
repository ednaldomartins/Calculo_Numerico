'''
Seja S = somatório de i=1 até n, para (i*(i+1))/2
Usando computação numérica, calcule S considerando n = 1000.
'''

n = 1000
resultado = 0
for i in range (n):
    resultado += (i*(i+1))/2
print ( resultado )