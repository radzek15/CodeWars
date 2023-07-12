"""
Something is wrong with our Warrior class. The strike method does not work correctly. The following shows an example of this code being used:

ninja = Warrior('Ninja')
samurai = Warrior('Samurai')

samurai.strike(ninja, 3)
# ninja.health should == 70

"""


class Warrior:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def strike(self, enemy, swings):
        enemy.health = max([0, enemy.health - (swings * 10)])
