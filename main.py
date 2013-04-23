import guiatv

import guiatv
guiatv.opciones()
numero = input('')
print('elegiste la opción',numero)
if numero == '1':
    print('¿cuantos canales deseas listar?')
    cantidad = input('')
    aenterocantidad = int(cantidadentero)
    guiatv.listar((cantidadentero+1))
    
elif numero == '2':
    guiatv.agregar()
elif numero == '3':
    guiatv.buscar()
else:
    guiatv.supererror()

#THE-END
