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
    def __init__(self, nombre, edad, departamento='Data', puesto='Analyst'):
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

trabajador_1b = Trabajador('Ivan', 27)
trabajador_1b.presentation()

my_var_list = [ 'Andrea', '42', 'Ventas', 'Manager' ]
trabajador_2 = Trabajador(*my_var_list)
trabajador_2.presentation()

my_var_dict = { 'nombre': 'Andrea', 'edad': '42', 'departamento': 'Ventas', 'puesto': 'Manager' }
trabajador_3 = Trabajador(**my_var_dict)
trabajador_3.presentation()