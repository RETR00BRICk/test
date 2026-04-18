from characters import *
from enemies import *

# players
anna = Fighter('Anna', 15, 60)
boris = Healer('Boris', 20, 30)

# enemies
goblin = Goblin('Grog', 10, 45)
dracula = Vampire('Dracula', 15, 35)

print('=== Stats before fight ===')
print(anna, boris, goblin, dracula, sep='\n')

goblin.attack(anna)
dracula.attack(anna)

anna.attack(dracula)
boris.heal(anna)

dracula.life_steal(boris)

print('=== Stats after fight ===')
print(anna, boris, goblin, dracula, sep='\n')