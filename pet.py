class Pet:
    def __init__(self, pet_name, pet_age):
        self.name = pet_name
        self.age = pet_age

    def play_fetch(self):
        print("Your pet " + self.name + " seemed to be happy to play fetch. Yay")
orange_cat = Pet("Miles", 8)
small_dog = Pet("Fido", 5)
print(orange_cat.name)
orange_cat.play_fetch()
