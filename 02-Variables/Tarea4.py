"""
print ("Determinar la suma de N primeros numeros enteros positivos ")
numero = int(input("Ingresa un número Entero Positivo"))
tiempo = int(input("Ingresa cuanto tiempo (dias)"))
suma = (numero*(numero+1))/2

print ("suma : ",suma)
"""

"""
print ("Interes Compuesto Del Capital")
capital = float(input ("Ingrese el capital = "))
tasa_interes = float(input("Ingrese la tasa de interes = "))
t = int(input("Ingresa cuanto tiempo (dias) = "))
m = ((1+((tasa_interes/100)))**t)*capital
print ("m \n :",m)
interes = m - capital
print ("Interes compuesto = ",interes)
"""

"""
print ("Area de un circulo ")
radio = int(input("Ingresa el valor del Radio del Circulo : "))
area = 3.14159*radio**2

print (f"Area del circulo con el radio {radio} es {area}")
"""

print ("Convertir de Segundos a Minutos, Horas")
segundos = int(input("Ingrese los Segundos que desea Convertir = "))
minutos = segundos/60
horas = minutos/60

print (f"Los {segundos} Segundos capturados son {minutos} Minutos y {horas} Horas ")
