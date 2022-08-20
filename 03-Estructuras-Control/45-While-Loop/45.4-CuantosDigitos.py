print ("Determinar cuantos digitos contiene un numero ")
numero = int(input("Ingresa un numero : "))
cuantos_dig = 0


while numero > 0:
	numero = numero // 10 # Obtener el conciente, la parte Entera
	cuantos_dig += 1
	print (f"Valor de numero - Cociente - : {numero} \n ")

print (f"Numero de digitos {cuantos_dig} ")
