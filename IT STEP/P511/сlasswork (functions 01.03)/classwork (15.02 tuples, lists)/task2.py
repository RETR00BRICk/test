import random
list1 = [random.randint(1, 10) for i in range(5)]
list2 = [random.randint(1, 10) for i in range(5)]

s1 = set(list1)
s2 = set(list2)

res1 = list1 + list2

res2 = list(s1.union(s2))

res3 = list(s1.intersection(s2))

res4 = list(s1.symmetric_difference(s2))

res5 = [min(list1), max(list1)]
res6 = [min(list2), max(list2)]
print("1. ALL:", res1)
print("2. Union:", res2)
print("3. Intersection:", res3)
print("4. Difference:", res4)
print("5. MIN1:", res5)
print("5. MIN2:", res6)