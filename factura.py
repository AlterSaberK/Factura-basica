import sys
def factura():
		print("Factura")
		non = str (input("ingrese nombre del cliente:"))
		producto = str (input("producto:"))
		cantidad  = int(input("cantidad:"))
		precio = float(input("precio:"))
		D_E = int and float(input("D_E:"))
        
        

		
		print("producto selecconado",producto)
		print("cantidad de porductos",cantidad)
		print("precio establecido",precio)

		if D_E >=precio:
			print("ejecutando")
		else:
			print("el programa se cerrara datos invalidos")
			sys.exit()			
			
        
		total = D_E - precio
        
	
		print("total de factura")
		print(total)
        

factura()
	
print ("ingresar datos nuevos")

factura()
