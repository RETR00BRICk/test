'''
from random import randint #randint()
from random import * #randint()
import random #random.randint()
'''
import random as r #r.randint()


print(r.randint(10,15)) #11 - 15 включительно
print(r.randrange(10,19,2)) #10,12,14,16,18 ЧЕТНЫЕ
print(r.random()) #0 - 1 float
print(r.uniform(-10.5, 54)) #-10.5 - 54 float

fruits = ['apple', 'mango', 'banana', 'lemon', 'orange']
print(r.choice(fruits))
print(r.choice("hello"))
print(r.choices(fruits, k=3)) #mango, mango, apple
print(r.choices(fruits, weights=[0.5, 0.1, 0.2, 0.05, 0.15], k=3)) # 50% 10% 20% 5% 15% 
print(r.sample(fruits,k=5)) #без повторів

r.shuffle(fruits) #перемешать
print(fruits)