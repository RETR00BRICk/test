from random import randint
num_set1 = set()
num_set2 = set()

while len(num_set1) < 10: #Генеруэмо числа поки довжина множини не стане 10
    num_set1.add(randint(1,20))

while len(num_set2) < 10: #Генеруэмо числа поки довжина множини не стане 10
    num_set2.add(randint(1,20))

print(num_set1.intersection(num_set2))
print(num_set1.difference(num_set2))
print(num_set1.union(num_set2))