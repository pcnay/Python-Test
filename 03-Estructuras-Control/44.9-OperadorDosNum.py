# Operaciones basicas con dos numeros.
num1 = int(input("Ingresa el primer numero : "))
num2 = int(input("Ingresa el segundo número : "))
op = input ("Ingresa un operador : +, -, /, * ")
if op == "/" and num2 == 0:
	resultado = 0
elif op == "+":
	resultado = num1+num2
elif op == "-":
	resultado = num1-num2
elif op == "/":
	resultado = num1/num2
elif op == "*":
	resultado = num1*num2

print (f"El resultado de la operacion { op } es {resultado}")

