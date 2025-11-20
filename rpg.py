class Character:
    def __init__(self, name, hp, stamina):
        self.name = name
        self.hp = hp
        self.stamina = stamina
    
    def fight(self, enemy):
        if self.stamina > enemy.stamina:
            print(f"{self.name} won the fight")
        elif self.stamina == enemy.stamina:
            print("The fight was a tie")
        else:
            print(f"{self.name} lost the fight")

class Food:
    def __init__(self, kind, calories):
        self.kind = kind
        self.calories = calories

morris = Character("Morris", 100, 100)
