def opciones():
    print('Bienvenido(a) a la Guía de TV')
    print('version 0.1')
    print('Elige la opción que deseas realizar')
    print('1 - Listar todos los canales.')
    print('2 - Agregar un nuevo canal')
    print('3 - buscar un canal')
def listar(final):
    print('La opción seleccionada permite listar todos los canales.')
    bdguia = open('bdguia.csv','a')
    inicio = 0
    for i in range(1,final):
        leer = bd-guia.readline()
        print(leer.replace(',','\t\t\t'))
        inicio = inicio + 1
    print ('Se han listados todos los canales')
    bgguia.close()
def agregar():
    print('la opción seleccionada permite agregar un canal a la lista')
    bdguia = open('bdguia.csv','a')
    canal = input('ingresa el nombre del canal: ')
    tag = input('ingresa un tag (ej. cine): ')
    orden = input('ingresa la posición del canal en la lista: ')
    print('los datos ingresados, se han guardado con éxito. El detalle es el siguiente, nombre del canal:',canal,'tag:',tag,'en la posición:',orden)
    bdguia.write(canal)
    bdguia.write(',')
    bdguia.write(tag)
    bdguia.write(',')
    bdguia.write(orden)
    bdguia.write(',')
    bdguia.write('\n')
    bdguia.close()
def supererror():
    print('la opción seleccionada no existe, favor intenta ingresar nuevamente una opción válida')
