import random

def get_minimal_sequience_start(num_list, best_index, best_summ, start_index):
    if start_index > 90:
        return best_index
    
    summ = 0
    for index in range(start_index, start_index + 10):
        summ += num_list[index]

    if best_index == None or summ < best_summ:
        best_index = start_index
        best_summ = summ
    
    return get_minimal_sequience_start(num_list, best_index, best_summ, start_index + 1)


num_list = [random.randint(0,100) for i in range(100)]
print(num_list)
print(get_minimal_sequience_start(num_list, None, None, 0))
