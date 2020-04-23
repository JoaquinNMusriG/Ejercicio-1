class Email:
    __idCuenta = ''
    __Dominio = ''
    __tipoDominio = ''
    __Contrasena = ''

    def __init__ (self, id, dom, tipo, contra):
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
