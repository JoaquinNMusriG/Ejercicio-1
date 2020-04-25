import re

class Email:
    __idCuenta = 'NO'
    __Dominio = 'HAY'
    __tipoDominio = 'EMAIL'
    __Contrasena = ''

    def __init__ (self, id = 'ejemplo', dom = 'ejemplo', tipo = 'eje', contra = 'vacio'):
        if (id != '') and (dom != '') and (tipo != '') and (contra != ''):
            self.__idCuenta = id
            self.__Dominio = dom
            self.__tipoDominio = tipo
            self.__Contrasena = contra
        else:
            print ('Falta información para crear un email.')

    def retornaEmail (self):
        return self.__idCuenta + '@' + self.getDominio() + '.' + self.__tipoDominio

    def getDominio (self):
        return self.__Dominio

    def cambiaContra (self, passw):
        if self.__Contrasena == passw:
            self.__Contrasena = input('Ingrese la nueva contraseña: ')
            print('Contraseña cambiada con exito')
        else:
            print('Contraseña Incorrecta, no es posible cambiar.')

    def crearCuenta (self, nuevaCuenta):
        if re.match('[a-zA-Z0-9\_\-\.]+@[a-zA-Z0-9\_\-\.]+\.[a-z]{1,10}', nuevaCuenta) != None:
            self.__idCuenta = nuevaCuenta[:nuevaCuenta.find("@")]
            self.__Dominio = nuevaCuenta[nuevaCuenta.find("@") + 1:nuevaCuenta.rfind(".")]
            self.__tipoDominio = nuevaCuenta[nuevaCuenta.rfind(".") + 1:]
            cont = input('Ingrese la contraseña para el nuevo objeto:')
            if cont != '':
                self.__Contrasena = cont
            else:
                print('Contraseña invalida, proceda a cambiar la contraseña usando 1234')
                self.__Contrasena = '1234'
            print('El objeto de tipo Email fue creado.')
            return 1
        else:
            print('ERROR: el formato del mail es invalido')
            return 0
