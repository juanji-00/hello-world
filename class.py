# Creación de una clase

#Esto es una modificación que se ha hecho del fichero

class Dog:

    species = "Canis lupus familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"
    
    def speak(self, sound):
        return f"{self.name} says {sound}"
    

perro = Dog("Pepe", 12)

print(perro.speak("Woou!"))

# Herencia de una clase

class GoldenRetriever(Dog):
    # Valor por defecto en .speak(), definimos sound y utilizamos super().
    def speak(self, sound="Bark"):
        return super().speak(sound)
    

buddy = GoldenRetriever("Pepi", 45)

print(buddy.speak())


