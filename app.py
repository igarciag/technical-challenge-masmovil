# -*- coding: utf-8 -*-

####################################################
# CLASSES

class Persona:
    def __init__(self, nombre, edad):
        # 3) La diferencia entre nombre y self.nombre es que nombre es la variable (local) que recibe en 
        # el constructor de la clase y self.nombre es el atributo de la clase (que permancera
        # accesible desdel el propio objeto de la clase)
        self.nombre = nombre
        self.edad = edad

    def presentation(self):
        print(f"Hola! Soy {self.nombre} y tengo {self.edad} años")


class Trabajador(Persona):
    def __init__(self, nombre, edad, departamento, puesto):
        super().__init__(nombre, edad)
        self.departamento = departamento
        self.puesto = puesto

    def presentation(self):
        super().presentation()
        print(f"Trabajo en el departamento de {self.departamento} como {self.puesto}")

        
####################################################
# MAIN

nombre = 'Alberto'
persona_1 = Persona(nombre, 20)
persona_1.presentation()

trabajador_1 = Trabajador('Ivan', 27, 'Data', 'Data Engineer')
trabajador_1.presentation()