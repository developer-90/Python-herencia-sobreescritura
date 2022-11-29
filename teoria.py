from datetime import date, datetime
from dateutil.relativedelta import relativedelta


print("POO en Python")
#https://ellibrodepython.com/programacion-orientada-a-objetos-python

#crear una clase
class Cliente:
    #propiedades de clase. comunes para todas las clase
    mensaje="un mensaje de buenos días"
    #constructor
    def __init__(self,nombre,facturacion,activo): #propiedades de instancia:cambia para cada instancia
        self.nombre=nombre
        self.facturacion=facturacion
        self.activo=activo
    def infoCliente(self):#utiliza las propiedades de instancia
        print(f'Datos del cliente {self.nombre} - {self.facturacion} - {self.activo}')

#crear un objeto Cliente
cliente1=Cliente('empresaA',995.94,True) #llamar al constructor
#mostrar el nombre del cliente1
print(cliente1.nombre) #consultar la info del cliente con sus propiedaes, atributos...
print(cliente1.mensaje)#llamar a un atributo de clase. NO tiene self
cliente1.infoCliente() #muestra todos los datos del cliente.

#herencia.
class Animal:
    def __init__(self):
        self.nombre=input('dime el nombre ')
        fecha=input('dime fecha yyyy-mm-dd ')
        self.dob=datetime.strptime(fecha,'%Y-%m-%d')
    def calculoEdad(self):
        #tienes que sacar la fecha de hoy
        #muestra por consola la edad de tu mascota
        #muestra la fecha actual
        fecha_hoy=datetime.now()
        print(f'la fecha actual es {fecha_hoy}')
        print(f'la fecha de nacimiento es {self.dob}')
        edad=relativedelta(fecha_hoy,self.dob)
        print(f'mi mascota tiene {edad} años')

class Perro(Animal):
    def ladrar(self):
        print('el perro ladra')
class Gato(Animal):
    def maullar(self):
        print('el gato maúlla')
#adoptamos un gatito llamado mizifú con dob 08/06/2020
gatito1=Gato()
gatito1.calculoEdad()
print(gatito1.nombre)












