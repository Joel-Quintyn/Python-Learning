"""
SYNOPSIS: This Program Was Written For A Project; RPG Adventure Game In Python, As The Fighting System For The Game.
            It Was Never Used, But It Is A Neat Program.
"""

import random
import time

player_health = 100


class Enemy:

    def __init__(self, name, strength, defense, health):
        self.name = name
        self.strength = strength
        self.defense = defense
        self.health = health

    def attack_enemy(self):
        time.sleep(1)
        print("what move would you like to make? (punch, kick or headbutt?")
        print("")
        answer = input().lower()

        if answer == "punch":
            self.health = self.health - (random.randint(1, 100) / (random.uniform(0, 1) * self.defense))
            self.health = int(self.health)
        elif answer == "kick":
            self.health = self.health - (random.randint(1, 100) / (random.uniform(0, 1) * self.defense))
            self.health = int(self.health)
        elif answer == "headbutt":
            self.health = self.health - (random.randint(1, 100) / (random.uniform(0, 1) * self.defense))
            self.health = int(self.health)
        else:
            print("you stumble...")

        time.sleep(1)

        print(self.name + "'s health is now: " + str(int(self.health)))
        print("")

        return int(self.health)

    def enemy_attack(self):
        global player_health
        time.sleep(1)
        print("The enemy " + self.name + " " + "attacks...")
        print("")
        player_health = player_health - (self.strength * random.uniform(0.1, 1.4))
        player_health = int(player_health)
        time.sleep(1)
        print("Your health is now " + str(int(player_health)))
        print("")
        return int(player_health)

    def battle_script(self):
        global player_health
        print("An enemy " + self.name + " appears...")
        print("")
        time.sleep(1)
        while player_health > 0 and self.health > 0:
            self.attack_enemy()
            if self.health <= 0:
                break
            self.enemy_attack()
            if player_health <= 0:
                break
        if self.health <= 0:
            time.sleep(1)
            print("You have killed the " + self.name)

        if player_health <= 0:
            time.sleep(1)
            print("Sorry, you are dead")


enemies = [Enemy("Boar", 10, 5, 100), Enemy("Wolf", 20, 10, 100), Enemy("Lion", 30, 20, 100),
           Enemy("Dragon", 40, 30, 130)]

random_enemy = random.choice(enemies)
random_enemy.battle_script()
