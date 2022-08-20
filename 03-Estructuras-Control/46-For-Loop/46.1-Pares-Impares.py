print ("Obtener los numeros Pares e Impares de una valor entero Ingresado ")
numero = int(input("Ingresa el numero entero "))
for n in range (1,numero):
	if n % 2 == 0:
		print (f"numero par {n} ")
	else:
		print (f"numero Impar {n}")

