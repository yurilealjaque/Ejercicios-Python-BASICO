class Tamagotchi:
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color
        # Valores por defecto
        self.salud = 100
        self.felicidad = 50
        self.energia = 100

    def jugar(self):
        self.felicidad += 10
        self.salud -= 5
        print(f"¡{self.nombre} está jugando! Felicidad: {self.felicidad}, Salud: {self.salud}")
        return self

    def comer(self):
        self.felicidad += 5
        self.salud += 10
        print(f"¡{self.nombre} está comiendo! Felicidad: {self.felicidad}, Salud: {self.salud}")
        return self

    def curar(self):
        self.salud += 20
        self.felicidad -= 5
        print(f"¡{self.nombre} ha sido curado! Salud: {self.salud}, Felicidad: {self.felicidad}")
        return self

# BONUS SENSEI: Herencia
class Mametchi(Tamagotchi):
    def __init__(self, nombre, color="Amarillo"):
        super().__init__(nombre, color)
        self.inteligencia = 100 # Atributo único de esta subclase