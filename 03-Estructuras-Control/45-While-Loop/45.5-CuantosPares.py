# Determinar cuantos números pares se tienen en un número tecleado.
numero = int(input("Ingresa el numero : "))
pares = 0
contador = 0
while contador < numero:
	if contador % 2 == 0:
		pares += 1
	contador += 1

print (f"Del numero tecleado {numero} tiene estos numeros pares {pares} ")
