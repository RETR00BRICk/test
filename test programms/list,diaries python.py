my_set = set()
my_set = set(['apple','cherry','mango'])
my_set = {'apple','cherry','mango','mango'}

print(my_set)
print(type(my_set))

#my_set[0] - ERROR

print(len(my_set))

new_set = {0, True, 1} # print(new_set) = {0, True}
print(new_set) #True = 1, 1 = True | False = 0, 0 = Falses

for i in my_set:
    print(i)

print('apple' in my_set) #True
print('banana' not in my_set) #True

#-----
my_set.add("pamelo")
print(my_set)
my_set.update(['kiwi','orange'])
print(my_set)
#--
