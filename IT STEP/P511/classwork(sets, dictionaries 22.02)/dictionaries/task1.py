import os
#эта функция очищает экран
def clear():
    os.system('cls' if os.name == 'nt' else 'clear') # Это не ИИ, это мне скинули на уроке команду, чтобы очищать экран
#nt это проверка на виндовс. clear на линуксе

running = True
contacts = dict()
while running:
    clear()
    print("---------------------")
    print("&&&Menu functions:&&&")
    print("rm - remove cntact")
    print("add - add contact")
    print("md - modify contact")
    print("all - see all contacts")
    print("e - exit the programm")
    command = input("####ENTER THE COMMAND>>>")
    clear()
    match command:
        case "all":
            print("All contacts:")
            for contact in contacts:              
                print(f"{contact} - {contacts[contact]}")          
        case "e": 
            print("Stopping...")
            break
        case "rm":
            target = input("Enter the name of the contact>>>")
            try: #POP нам выдаст ошибку если значение введено неправильно
                contacts.pop(target) #try позволяет попробовать выполнить команду
                print(f"### REMOVED {target}")
            except: # а exept выполнится если произошла ошибка, но программу это не положит
                print("!!!This name is not in contacts!")
            #ЭТО НЕ ИИ! Я сам писал честно
        case "add":
            target = input("Enter the name of the contact to add>>>")
            if target in contacts:
                print("!!!This contact already exist!")
            else:
                number = input("Enter the number of the contact>>>")
                contacts[target] = number
                print(f"###'{target}' ADDED TO CONTACTS!")
        case "md":
            target = input("Enter the name of the contact to modify>>>")
            if target in contacts:
                number = input("Enter new number>>>")
                contacts[target] = number
                print(f"### NUMBER CHANGED TO '{number}'")
            else:
                print("!!!This contact does not exist!")
        case _: print("!!!INVALID COMMAND!")
    var = input("###Press enter to return to menu!>>>")