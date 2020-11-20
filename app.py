# -*- coding: utf-8 -*-

####################################################
# CLASSES

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentation(self):
        print(f"Hola! Soy {self.nombre} y tengo {self.edad} años")


class Trabajador(Persona):
    def __init__(self, nombre, edad, departamento, puesto):
        super().__init__(nombre, edad)
        self.departamento = departamento
        self.puesto = puesto

        
####################################################
# MAIN

nombre = 'Alberto'
persona_1 = Persona(nombre, 20)
persona_1.presentation()
