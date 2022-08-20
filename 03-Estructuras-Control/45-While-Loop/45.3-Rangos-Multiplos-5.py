print ("Dado un numeros determinar cuales son multiplos de 5")
numero = int(input("Ingresa el numero "))
numero_actual = 0
multiplo_5 = 0
while numero_actual < numero:
	if numero_actual %  5 == 0:
		print (f"numero {numero_actual} es multiplo de 5 ")
		multiplo_5 += 1

	numero_actual += 1

	
print (f"Del numero ingresado {numero} tiene {multiplo_5} multiplos de 5 ")

