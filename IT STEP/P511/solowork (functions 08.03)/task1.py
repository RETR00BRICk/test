def get_biggest_common_divider(a, b):
    if b == 0:
        return a
    return get_biggest_common_divider(b, a % b)


print(get_biggest_common_divider(48, 18)) 