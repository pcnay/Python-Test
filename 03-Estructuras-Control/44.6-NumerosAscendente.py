num1 = int(input("Ingresa el Primer numero : "))
num2 = int(input("Ingresa el Segundo numero : "))
num3 = int(input("Ingresa el Tercer numero : "))

# Encontrar el numero mayor de los tres.
if (num1 > num2 and num1 > num3):
	mayor = num1
elif (num2 > num1 and num2 > num3):
	mayor = num2
elif (num3 > num1 and num3 > num2):
	mayor = num3

# Encontrando el número Menor
if (num1 < num2 and num1 < num3):
	menor = num1
elif (num2 < num1 and num2 < num3):
	menor = num2
elif (num3 < num1 and num3 < num2):
	menor = num3

intermedio = (num1+num2+num3)-(mayor+menor)

print (f"Numero menor {menor} Numero Intermedio : {intermedio} Numero Mayor : {mayor}")



