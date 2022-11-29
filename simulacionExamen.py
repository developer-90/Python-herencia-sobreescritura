#primer ejercicio.
#Por consola pide la fecha de alta, email y curso en donde se matricula un alumno.
#Una vez matriculado, muestra un mensaje indicando sus datos de confirmación de matrícula.

#segundo ejercicio
#enlace de referencia
# https://pythones.net/polimorfismo-sobrecarga-metodos/
#tienes una clase llamada Facturar
#tienes un método que te pide como argumentos unidades y precio. muestra el total
#tienes otro método con el mismo nombre que el anterior y pide unidades, precio e iva. muestra total
#cómo se llama esta característica? python la soporta?
#NO es sobreescritura. Sería si fuera clase padre y clase hija con el mismo método.
#en este caso, es sobrecarga. *** en python no existe la sobrecarga como tal
class Facturar:
    def total(self,unidades,precio,iva): #NO es sobrecarga, pero lo emula en Python
        if type(iva)==int:
            print(f'el total es {unidades*precio*iva}')
        else:
            print(f'el total es {unidades * precio}')


factura=Facturar() #instanciar una clase
factura.total(100,9.95,21)

#ejemplo de sobreescritura. (se da en herencia)

class Persona:
    def pasear(self):
        print('la persona pasea')
class Niño(Persona): #herencia
    def pasear(self): #sobreescritura
        print('el niño pasea')
class Niña(Persona): #herencia
    def pasear(self): #sobreescritura : la clase derivada sobreescribe el método de la clase Padre
        print('la niña pasea')
class Adulto(Persona): #herencia
   pass

niña=Niña()
niña.pasear()
