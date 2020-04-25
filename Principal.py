from Email import Email
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
    otroEmail = Email()
    varVerificadora = otroEmail.crearCuenta(nuevaCuenta)
    if varVerificadora:
        print('El mail creado es: ' + otroEmail.retornaEmail())
    else:
        del otroEmail

    dom = input('Ingrese el dominio a contar: ')
    archivo = open('ejemplo.csv')
    reader = csv.reader(archivo, delimiter = ',')
    cont = 0
    mailCSV = Email()
    for list in reader:
        prueba = mailCSV.crearCuenta(list[0])
        if prueba:
            if mailCSV.getDominio() == dom:
                cont +=1
    print('La cantidad de veces que aparece el dominio ' + dom + ' es de: ' + str(cont))
    archivo.close()
