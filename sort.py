import random

class Character:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.level = 1
        self.exp = 0

    def display_stats(self):
        print(f"{self.name} (Level {self.level}) - Health: {self.health}, Attack: {self.attack}, Defense: {self.defense}, Exp: {self.exp}")

    def level_up(self):
        self.level += 1
        self.health += random.randint(5, 10)
        self.attack += random.randint(1, 3)
        self.defense += random.randint(1, 3)
        print(f"{self.name} leveled up to Level {self.level}!")

class Enemy:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def display_stats(self):
        print(f"{self.name} - Health: {self.health}, Attack: {self.attack}, Defense: {self.defense}")

def battle(player, enemy):
    print(f"A wild {enemy.name} appeared!")

    while player.health > 0 and enemy.health > 0:
        print("\nPlayer's Turn:")
        print("1. Attack")
        print("2. Run")
        choice = input("Choose an action (1 or 2): ")

        if choice == '1':
            damage_to_enemy = max(0, player.attack - enemy.defense)
            enemy.health -= damage_to_enemy
            print(f"You dealt {damage_to_enemy} damage to {enemy.name}!")

            if enemy.health <= 0:
                print(f"You defeated {enemy.name}!")
                player.exp += 10
                player.display_stats()
                player.level_up()
                break

            print(f"{enemy.name}'s Turn:")
            damage_to_player = max(0, enemy.attack - player.defense)
            player.health -= damage_to_player
            print(f"{enemy.name} dealt {damage_to_player} damage to you!")

            player.display_stats()

        elif choice == '2':
            print("You managed to escape from the battle.")
            break

        else:
            print("Invalid choice. Try again.")

    if player.health <= 0:
        print("Game over. You were defeated.")

def main():
    print("Welcome to the Text-Based RPG!")

    player_name = input("Enter your character's name: ")
    player_class = input("Choose your character class (Warrior, Mage, Archer): ")

    if player_class.lower() == 'warrior':
        player = Character(player_name, health=50, attack=10, defense=5)
    elif player_class.lower() == 'mage':
        player = Character(player_name, health=40, attack=12, defense=3)
    elif player_class.lower() == 'archer':
        player = Character(player_name, health=45, attack=8, defense=7)
    else:
        print("Invalid class. Defaulting to Warrior.")
        player = Character(player_name, health=50, attack=10, defense=5)

    player.display_stats()

    enemy = Enemy(name="Goblin", health=20, attack=6, defense=2)

    battle(player, enemy)

if __name__ == "__main__":
    main()
