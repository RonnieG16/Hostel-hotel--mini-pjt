class Player:
    def __init__(self, name, attack_power, health=100):
        self.name = name
        self.attack_power = attack_power
        self.health = health

    def attack(self, other):
        other.health -= self.attack_power
        if other.health < 0:
            other.health = 0
        print(f"{self.name} attacks {other.name} for {self.attack_power} damage.")

    def heal(self, amount):
        self.health += amount
        print(f"{self.name} heals by {amount}. New health: {self.health}")

    def is_alive(self):
        return self.health > 0

# Create 2 players
player1 = Player("Mike Tyson", 30)
player2 = Player("Jake Paul", 12)

round_num = 1
print("🏁 Battle Start!\n")

# Fight until one player dies
while player1.is_alive() and player2.is_alive():
    print(f"--- Round {round_num} ---")
    player1.attack(player2)
    print(f"{player2.name}'s health: {player2.health}")

    if not player2.is_alive():
        print(f"☠ {player2.name} has fallen! {player1.name} wins!")
        break

    player2.attack(player1)
    print(f"{player1.name}'s health: {player1.health}")

    if not player1.is_alive():
        print(f"☠ {player1.name} has fallen! {player2.name} wins!")
        break

    round_num += 1

print("\n🏆 Battle Over!")