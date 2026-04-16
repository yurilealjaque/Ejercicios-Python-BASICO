class Persona:
    def __init__(self, nombre, apellido, tamagotchi):
        self.nombre = nombre
        self.apellido = apellido
        self.tamagotchi = tamagotchi # Asociación

    def jugar_con_tamagotchi(self):
        print(f"{self.nombre} está invitando a jugar a su mascota...")
        self.tamagotchi.jugar()
        return self

    def darle_comida(self):
        print(f"{self.nombre} le prepara algo rico a su mascota...")
        self.tamagotchi.comer()
        return self

    def curarlo(self):
        print(f"{self.nombre} está llevando al doctor a su mascota...")
        self.tamagotchi.curar()
        return self