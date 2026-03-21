'''def print_contact(contact):
    if contact['мобільний'] != None: print(f"мобільний: {contact['мобільний']}")
    if contact['робочий'] != None: print(f"робочий: {contact['робочий']}")

contacts = {
    'Настя' : {
        'мобільний': '0506985764',
        'робочий' : '0890989584'
    },
    'Антон СТО' : {
        'мобільний': None,
        'робочий' : '0500598473'
    },
    'Тимофій Карпати' : {
        'мобільний': '0506985764',
        'робочий' : None
    }
}

while True:
    print('1. Знайти контакт\n2. Вивести всі контакти\n0. Вихід')
    action = int(input('Оберіть дію: '))

    match action:
        case 1:
            name = input('Введіть ім\'я контакту:')
            if name in contacts:
                print_contact(contacts[name])
            else:
                print('Немає такого контакту!')
        case 2:
            for contact in contacts:
                print(contact)
                print_contact(contacts[contact])
        case 0: break
        case _: print("Нема такого варіанту!")
'''
def print_greeting(name: str = "guest"):
    print("=================")
    print(f"===Hello,{name.upper()}!==")
    print("=================")

def my_sum(num1: float, num2: float) -> int:
    print(type(num1) == type(float))
    return num1 + num2

my_sum(3.1,2.5)

def print_full_name(last_name, first_name):
    print("Повне ім'я:", last_name, first_name)


print_full_name('Ковальчук', 'Антон')
print_full_name(last_name='Ковальчук', first_name='Антон')

def my_animal(type, name, age):
    print(f'У мене є {type} на ім\'я {name}. Вік: {age}')


my_animal('собака', age=10, name='Патрон')

def only_positional(param, /):
    print(param)

only_positional("hello!")

def only_key_wrod(*,param):
    print(param)

def my_sum(*numbers):
    result = 0
    for i in numbers:
        result += i
    return result


print(my_sum(10,12, 34))
print(my_sum(10))
print(my_sum(10,10,10,10,10,10,10,10,10,10,10))

#ДОПИСАТИ ПРО KWARGS

def unpack_positional(a, b, c):
    print(a, b, c, sep=', ')


fruits = ['apple', 'orange', 'banana']
unpack_positional(*fruits)


def unpack_kw_args(blue, red, green, yellow):
    print(red, green, blue)


fruits = {
    'red': 'apple',
    'green': 'pear',
    'yellow': 'banana',
    'blue': 'grapefruit'
}

unpack_kw_args(**fruits)

global_var = 12

def local_func(local_param):
    global global_var
    global_var = 50
    local_var = 10 # локальна область видимості
    print(local_var)
    print(global_var)

local_func(10)
print(global_var)

#ENCLOSING VS LOCAL

#?????? імперативий?
def get_discounted_prices(prices: list):
    discounted_prices = []

    for price in prices:
        if price > 100:
            discounted_prices.append(price * 0.8)
    
    return discounted_prices

original_prices = [50, 120, 80, 200, 300]
result = get_discounted_prices(original_prices)
print(result)

#####

def say_hello():
    print("Hello!")
func_var = say_hello

def some_function(callback):
    print("some_func calls its callback")
    callback()

#some_function(say_hello)

sum3 = lambda a, b: a+b

print(sum3(10,12))

operations = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b,
}

'''num1 = float(input())
num2 = float(input())
action = input("+ - * /")

if action in operations:
    print(operations[action](num1,num2))
'''
##NOT PURE FUNCTION:

tax_rate = 0.2

def calculate_tax_impure(amount):
    return amount*tax_rate

print(calculate_tax_impure(10000))

#PURE FUNTCION
def calculate_tax_pure(amount, tax_rate):
    return amount * tax_rate

print(calculate_tax_pure(1000, 0.3))

def add_product(cart : list, product : str): #IMPURE
    cart.apped(product)
    return cart

def add_product_pure(cart : list, product : str): #PURE
    new_cart = cart.copy()
    new_cart.append(product)
    return new_cart

my_cart = ['apple', 'banana']
my_cart = add_product_pure(my_cart, 'orange')

print(my_cart)

###

'''def create_multiplier(factor):
    def multiplier(number)'''

def changeupper(func):
    def inner():
        return func().upper()

