#Создайте простую текстовую боевую игру, где игрок и компьютер управляют героями с различными характеристиками.
# Игра состоит из раундов, в каждом раунде игроки по очереди наносят урон друг другу,
# пока у одного из героев не закончится здоровье.

#Требования:

#1. Используйте ООП (Объектно-Ориентированное Программирование) для создания классов героев.

#2. Игра должна быть реализована как консольное приложение.

#Классы:

#Класс `Hero`:

#- Атрибуты:

#- Имя (`name`)

#- Здоровье (`health`), начальное значение 100

#- Сила удара (`attack_power`), начальное значение 20

#- Методы:

#- `attack(other)`: атакует другого героя (`other`), отнимая здоровье в размере своей силы удара

#- `is_alive()`: возвращает `True`, если здоровье героя больше 0, иначе `False`

#Класс `Game`:

#- Атрибуты:

#- Игрок (`player`), экземпляр класса `Hero`

#- Компьютер (`computer`), экземпляр класса `Hero`

#- Методы:

#- `start()`: начинает игру, чередует ходы игрока и компьютера, пока один из героев не умрет.
# Выводит информацию о каждом ходе (кто атаковал и сколько здоровья осталось у противника) и объявляет победителя.

class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        other.health -= self.attack_power
        print(f"{self.name} атакует {other.name} отнимая у него  {self.attack_power} здоровья.")

    def is_alive(self):
        return self.health > 0


class Game:
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer

    def start(self):
        turn = 0  # 0 for player, 1 for computer
        while self.player.is_alive() and self.computer.is_alive():
            if turn == 0:
                self.player.attack(self.computer)
                turn = 1
            else:
                self.computer.attack(self.player)
                turn = 0

            # Show remaining health
            print(f"У {self.player.name} осталось {self.player.health} здоровья.")
            print(f"У {self.computer.name} осталось {self.computer.health} здоровья.")

        if self.player.is_alive():
            print(f"{self.player.name} побеждает!")
        else:
            print(f"{self.computer.name} побеждает!")


# Example of creating game characters and starting the game
player_hero = Hero("Игрок")
computer_hero = Hero("Компьютер")
game = Game(player_hero, computer_hero)
game.start()
