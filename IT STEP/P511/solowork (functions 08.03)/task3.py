def is_symmetric(target_list):
    if len(target_list) <= 1: #если длина 1 то он точно симметричный
        return True
    
    if target_list[0] != target_list[-1]: # если длинна больше 1 мы проверяем элементы в начале и конце массива
        return False
    
    return is_symmetric(target_list[1:-1]) #убираем 2 крайних элемента

input_list = [1, 2, 3, 2, 2]
print(is_symmetric(input_list))
input_list = [1, 2, 3, 2, 1]
print(is_symmetric(input_list))
