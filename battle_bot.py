import random


class BattleBot:
    def __init__(self, name):
        self.name = name
        self.health = 100.0
        self.base_armor = 10.0
        self.base_damage = 10.0
        self.speed = 10.0

    def attack(self, opponent):
        damage_dealt = self.base_damage - (self.base_damage * opponent.base_armor / 100)
        opponent.take_damage(damage_dealt)

    def take_damage(self, damage_dealt):
        self.health -= damage_dealt

    def build_attack(self):
        self.base_armor -= 1
        self.base_damage += 2
        self.speed -= 1

    def build_base_armor(self):
        self.base_armor += 2
        self.base_damage -= 1
        self.speed -= 1

    def build_speed(self):
        self.speed += 2
        self.base_armor -= 1
        self.base_damage -= 1

    def is_alive(self):
        if self.health <= 0:
            return False
        else:
            return True

    def get_stats(self):
        print(self.name)
        print("Speed: " + str(self.speed))
        print("Base Damage (attack): " + str(self.base_damage))
        print("Base Armor (defense): " + str(self.base_armor))
        print("Health: " + str(self.health))

    def action(self, opponent):
        random_number = random.randint(1, 100)
        if random_number <= 20:
            self.build_base_armor()
        elif random_number <= 50:
            self.build_attack()
        elif random_number <= 80:
            self.build_speed()
        else:
            self.attack(opponent)

    def battle(self, opponent):
        while self.is_alive() and opponent.is_alive():
            self.action(opponent)
            opponent.action(self)
        if self.is_alive():
            print(self.name + " won.")
        else:
            print(self.name + " lost. Bot 2 won.")
        print("Bot1 health: " + str(self.health))
        print("Bot2 health: " + str(opponent.health))


bot1 = BattleBot("Walter")
bot2 = BattleBot("Aloe")
bot1.attack(bot2)
bot1.get_stats()
bot2.get_stats()
bot1.battle(bot2)