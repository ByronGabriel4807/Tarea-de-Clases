#  clase: es una plantilla para crear objetos que define un conjunto de atributos y métodos
# objeto: es una instancia de una clase y contiene datos y puede ejecutar metodos definifos en la clase
# atributos: son las caracteristicas de un objeto representadas como variables de una clase 
# metodos: son funciones definidas en una clase que describen el comportamiento de un objeto
# carros, personas, padres,aves y vacas
class Perro:
    def __init__(self,nombre,raza):
        self.nombre = nombre
        self.tipo = raza

    def ladrar(self):
        return f"Guau {self.nombre} esta ladrando"
    

class carros:
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo

    def acelerar(self):
        return f"El carro {self.marca} {self.modelo} esta acelerando"


class personas:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        return f"Hola soy {self.nombre} y tengo {self.edad} años"
    
class aves:
    def __init__(self,nombre,especie):
        self.nombre = nombre
        self.especie = especie

    def volar(self):
        return f"{self.nombre} de la especie {self.especie} esta volando"
    
class vacas:
    def __init__(self,nombre,raza):
        self.nombre = nombre
        self.raza = raza

    def mugir(self):
        return f"{self.nombre} de la raza {self.raza} esta mugiendo"
    
class padres:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def regañar(self):
        return f"el papa se llamda {self.nombre} y tiene {self.edad} años"
    
    
class hijo():
    def __init__(self, NombreH, nombre, edad):
        self.NombreH = NombreH
        self.nombre = nombre
        self.edad = edad
        
    def llamar_a_papa(self, NombreH, nombre, edad):
        return(f"Hola, soy {self.NombreH} y mi padre se llama {self.nombre} y tiene {self.edad} años.")

persona1 = personas("Juan",25)
print(persona1.saludar())

carro1 = carros("Toyota","Corolla")
print(carro1.acelerar())

perro1 = Perro("Firulais","Pastor Aleman")
print(perro1.ladrar())

ave1 = aves("Aguila","Calva")
print(ave1.volar())

vaca1 = vacas("Margarita","Holstein")
print(vaca1.mugir())

padre1 = padres("Pedro",45)
print(padre1.regañar())

Hijo = hijo("Juanito","Pedro",45)
print(Hijo.llamar_a_papa("Juanito","Pedro",45))