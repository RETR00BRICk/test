nums = [int(x) for x in input("ENTER NUMBERS WITH SPACE BETWEEN THEM>>>").split()]
n = int(input("ENTER N>>>"))

if n != 0 and len(nums) != 0:
    moved_nums = [0] * len(nums)
    for i in range(len(nums)):
        new_index = i + n
        if new_index >= len(nums): new_index -= len(nums)
        moved_nums[new_index] = nums[i]
    print(moved_nums)