from pet import Pet
class Dog(Pet):

    def __init__(self, name, volume, age):
        super().__init__(name, age)
        self.volume = volume

    def bark(self):
        if self.volume > 3:
            print("Woof woof woof")
        elif self.volume < 3:
            print("Yip yip yip")

small_dog = Dog("Pup", 2, 8)
big_dog = Dog("Coco", 5, 10)

small_dog.bark()
big_dog.bark()
print(small_dog.age)