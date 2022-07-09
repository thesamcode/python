

class Ninja:
    def __init__(self, first_name , last_name , treats , pet_food , pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treat = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        print("Let's go for a walk")
        pet1.play()
        return self

    def feed(self):
        print("Here, have some food")
        pet1.eat()
        return self

    def bathe(self):
        print("Bath time")
        pet1.noise()
        return self

    def view_pet_health(self, pet1):
        self.pet.indicate_health_energy()

class Pet:
    all_pets = []
    def __init__(self, name, type, tricks, sound, health=20, energy=20):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.sound = sound
        self.health = health
        self.energy = energy
        Pet.all_pets.append(self)

    def sleep(self):
        self.energy += 25
        print("zzz")
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        print("chomp chomp")
        return self

    def play(self):
        self.health += 5
        print("walks are my favorite")
        return self

    def noise(self):
        print(self.sound)
        return self

    def indicate_health_energy(self):
        print("My health is:",self.health)
        print("My energy is:",self.energy)

pet1 = Pet("Sparky", "dog", "jumps", "woof", 21, 21)
ninja1 = Ninja("John", "Smith", "dog treats", "dog food", pet1)

ninja1.feed().walk().bathe().view_pet_health(pet1)
