list_of_nums = list(map(int, input('Enter integers separated by spaces: ').split()))

def find_max_and_min(list_of_nums):
    maxnum = list_of_nums[0]
    minnum = list_of_nums[0]
    for a in list_of_nums:
        if a > maxnum:
            maxnum = a
        elif a < minnum:
            minnum = a
    return maxnum - minnum 

print(find_max_and_min(list_of_nums))