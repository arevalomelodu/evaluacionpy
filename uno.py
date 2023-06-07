class Animal:
    def hablar(self):
        pass

class Perro(Animal):
    def hablar(self):
        return "Guau"

class Gato(Animal):
    def hablar(self):
        return "Miau"

class Vaca(Animal):
    def hablar(self):
        return "Muu"

class Pollito(Animal):
    def hablar(self):
        return "Pio Pio"
#creo el llamado a la nueva funcion
def hacer_hablar(animal):
    print(animal.hablar())

# creo las instancias para llamar a la clase del objeto 
perro = Perro()
gato = Gato()
vaca = Vaca()
pollito = Pollito()

# imprimo el llamdo al a funcion 
hacer_hablar(perro)
hacer_hablar(gato)
hacer_hablar(vaca)
hacer_hablar(pollito)