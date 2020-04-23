from Email import Email
from Manejador import Manejador
import csv

if __name__ == '__main__':

    print('Ingrese los siguientes datos para crear el objeto:')
    nombre = input('Nombre:')
    idCuenta = input('Id de la cuenta:')
    dominio = input('Dominio de la cuenta:')
    tipoDominio = input('Tipo de dominio de la cuenta:')
    contrasena = input('Contrasena:')
    mail = Email(idCuenta, dominio, tipoDominio, contrasena)
    print('Estimado ' + nombre + ' te enviaremos tus mensajes a la dirección ' + mail.retornaEmail())

    verificaContra = input('Ingrese la constraseña para cambiar: ')
    mail.cambiaContra(verificaContra)

    nuevaCuenta = input('Ingrese la direccion para crear el nuevo objeto email: ')
    nuevo = Manejador(nuevaCuenta)
    otroEmail = nuevo.crearCuenta()
    if type(otroEmail) == Email:
        print('El mail creado es : ' + otroEmail.retornaEmail())

    dom = input('Ingrese el dominio a contar: ')
    archivo = open('ejemplo.csv')
    reader = csv.reader(archivo, delimiter = ',')
    cont = 0
    for list in reader:
        if dom == list[0][list[0].find("@") + 1:list[0].rfind(".")]:
            cont+=1
    print('La cantidad de veces que aparece el dominio ' + dom + 'es de: ' + str(cont))
    archivo.close()
