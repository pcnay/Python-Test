num_mes = int(input("Ingresa un numero de mes : "))
estacion = ""

if ((num_mes == 1) or (num_mes == 2) or (num_mes == 3)):
	estacion = "Verano"
elif ((num_mes == 4) or (num_mes == 5) or (num_mes == 6)):
	estacion = "Otono"
elif ((num_mes == 7) or (num_mes == 8) or (num_mes == 9)):
	estacion = "Invierno"
elif ((num_mes == 10) or (num_mes == 11) or (num_mes == 12)):
	estacion = "Primavera"
else:
	estacion = "Desconocido"

print (f"Numero de Mes {num_mes} la estacion es : {estacion} ")
