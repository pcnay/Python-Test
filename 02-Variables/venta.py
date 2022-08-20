"""
Practica 2 : Calcular precio de venta

Dado el valor de la venta de producto, hallar el IGV (18%) y el precio de venta.

Analisis:
Se requiere que el usuario ingrese el valor de venta del producto y el sistema realice el cálculo respectivo para hallar el IGV y el precio de venta, para esto usuar la siguiente expresion:
	igv = vv * 0.18
	pv = vv + igv

"""
print ('Calcular el Precio De Venta')
vv = float(input ("Ingresa el precio de venta del producto = "))

# Obtener el "igv"
igv = vv*0.18
pv = vv+igv

# Imprimiendo el precio de venta.
print ("="*50)
print ("------------------ FACTURA DE VENTA ----------------------")
print ("="*50)
print (f"Valor de Venta {vv} Valor de IVA {igv} El precio de venta : {pv}")
print ("="*50)
