print ("Dado un rango de numero determinar cuantos pares tiene ")
ni = int(input("Ingresa el rango del numero inicial : "))
nf = int(input("Ingresa el rango del numero final : "))
rango_final = nf 
contador = ni
cant_pares = 0
while contador <= rango_final:
	
	if (contador % 2 == 0):
		cant_pares += 1

	contador+=1

print (f"En el rango de numeros de {ni} hasta {nf} contiene una cantidad de numeros pares de {cant_pares}")


