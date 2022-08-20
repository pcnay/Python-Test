# Cuantos numero se tiene en un rango de números.

num_inic = int(input("Ingresa el Primer numero "))
num_final = int (input("Ingresa el Segundo numero "))
contador = num_inic+1 # Se suma 1 para que inicie el conteo apartir del siguiente numero
rango_num = 0
while contador <= num_final:
	contador+= 1
	rango_num += 1

print(f"Este rango de numeros contiene {rango_num} ")



	