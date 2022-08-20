num1 = int(input("Ingresa el Primer numero = "))
num2 = int(input("Ingresa el Segundo numero = "))
num3 = int(input("Ingresa el Tercer numero = "))

if num1 > num2:
	mayor = num1
elif num2 > num1:
	mayor = num2
else:
	mayor = num3

print (f" Numero mayor es : {mayor}" )
