from random import randint

class Die:

    def __init__(self, sides: int) -> None:
        self.sides = sides

    def roll_die(self):
        self.sides = randint(1, 20)

        return self.sides

die = Die(6)

for i in range(11):
    print(f'Qtd de vezes jogados: {i}')
    print(f'Resultado: {die.roll_die()}\n')