from Email import Email
import re

class Manejador:
    __mail = ''

    def __init__ (self, mail):
        self.__mail = mail

    def crearCuenta (self):
        if re.match('[a-z0-9\_\-\.]+@[a-zA-Z0-9\_\-\.]+\.[a-z]{1,10}',self.__mail) != None:
            contra=input('Ingrese la contraseña para el nuevo objeto:')
            nuevoEmail = Email(self.__mail[:self.__mail.find("@")],self.__mail[self.__mail.find("@") + 1:self.__mail.rfind(".")],self.__mail[self.__mail.rfind(".") + 1:],contra)
            print('El objeto de tipo Email fue creado correctamente.')
            return nuevoEmail
        print('ERROR: el formato del mail es invalido')

# Esta forma del método va sin el módulo re
#    def crearCuenta (self):
#            if self.__mail.find('@') != -1 :
#                if self.__mail.find('.', self.__mail.find('@')+1) != -1:
#                    if (self.__mail[:self.__mail.find("@")] != '') & (self.__mail[self.__mail.find("@") + 1:self.__mail.rfind(".")] != '') & (self.__mail[self.__mail.rfind(".") + 1:] != ''):
#                        contra=input('Ingrese la contraseña para el nuevo objeto:')
#                        nuevoEmail = Email(self.__mail[:self.__mail.find("@")],self.__mail[self.__mail.find("@") + 1:self.__mail.rfind(".")],self.__mail[self.__mail.rfind(".") + 1:],contra)
#                        print('El objeto de tipo Email fue creado correctamente.')
#                    else:
#                        print ('ERROR: el formato del mail es invalido')
#                        nuevoEmail = None
#                    return nuevoEmail
#            print('ERROR: el formato del mail es invalido')
