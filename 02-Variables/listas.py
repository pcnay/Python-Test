"""
 Ingresar datos
numero = input('Número: ')

# Convertir 
numero = int(numero)

# Solución 

residuo = numero % 10
numero = numero // 10
numeroInverso = residuo * 10

residuo = numero % 10
numero = numero // 10 
numeroInverso = (numeroInverso + residuo) * 10

residuo = numero % 10
numero = numero // 10 
numeroInverso = (numeroInverso + residuo) * 10

residuo = numero % 10
numero = numero // 10
numeroInverso = (numeroInverso + residuo) * 10

numeroInverso = numeroInverso + numero

# Salida de datos
print('Inverso: ', numeroInverso)
"""




print ("	INVENTIR LAS POSICIONES DE UN NUMERO \n ")
# Una forma de realizarlo
lista = input ("Ingrea un numero de 5 digitos = ")
lista_invertida = lista[-1],lista[-2],lista[-3],lista[-4],lista[-5]
print (f"\n Numero invertido {lista[-1]}{lista[-2]}{lista[-3]}{lista[-4]}{lista[-5]}")

# Usando residuos:
bloque1 = int(lista)
residuo5 = bloque1 % 10

bloque2 = lista[0:4]
bloque2 = int(bloque2)
residuo4 = bloque2 % 10

bloque3 = lista[0:3]
bloque3 = int(bloque3)
residuo3 = bloque3 % 10

bloque4 = lista[0:2]
bloque4 = int(bloque4)
residuo2 = bloque4 % 10

bloque5 = lista[0:1]
bloque5 = int(bloque5)
residuo1 = bloque5 % 10

print (f"Numero invertido {residuo5}{residuo4}{residuo3}{residuo2}{residuo1}")

