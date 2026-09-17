import random

class Character:
    def __init__(self, name: str, hp: int, atk: int):
        self.name = name
        self.hp = hp
        self.atk = atk

    def attack(self, target: "Character"):
        dmg = random.randint(self.atk - 3, self.atk + 3)
        target.hp = max(0, target.hp - dmg)
        print(f"{self.name}의 공격! {target.name}에게 {dmg} 데미지 (남은 HP: {target.hp})")

    def is_alive(self) -> bool:
        return self.hp > 0

player = Character("용사", 45, 10)
monster = Character("슬라임", 35, 7)

turn = 1
while player.is_alive() and monster.is_alive():
    print(f"\n[Turn {turn}]")
    player.attack(monster)
    if monster.is_alive():
        monster.attack(player)
    turn += 1

winner = player.name if player.is_alive() else monster.name
print(f"\n전투 종료! 승자: {winner}")