import pandas as pd

class Persona:
    def __init__(self):
        self.documento = ''
        self.apellido = ''
        self.nombre = ''

    def __repr__(self):
        return f'Persona: {self.documento} - {self.apellido}, {self.nombre}'
    
    def input(self):
        self.documento = int(input('Ingrese documento: '))
        self.apellido = input('Ingrese apellido: ')
        self.nombre = input('Ingrese nombre: ')

class PersonaService:
    def lectura(self, archivo):
        arc = open(archivo, "r")
        arc.close()

    def escribir(self, texto, archivo):
        with open(archivo, 'w') as arc:
            arc.write(texto)
            arc.close()
        
    def add(self, documento, apellido, nombre, archivo, persona=Persona()):
        persona.documento = documento
        persona.apellido = apellido
        persona.nombre = nombre
        data = [persona.documento, persona.apellido, persona.nombre]
        with open(archivo, "a") as arc:
            arc.write(data)
            arc.close()


    def delete(self, documento, apellido, nombre, archivo, persona=Persona()):
        with open(archivo, "r+") as arc:
            with open("archivo_nuevo.txt", "w") as output:
                for line in arc:
                    if apellido and nombre and documento not in line.strip("\n"):
                        output.write(line)   
                        output.close()
                        arc.close()

    def findByDocumento():
        pass
    def findAll():
        pass