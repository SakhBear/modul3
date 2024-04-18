from itertools import permutations


def largest_number(nums):

    nums = list(map(str, nums))
    perms = permutations(nums)
    max_num = max([''.join(i) for i in perms])

    return max_num


nums = [18, 70, 38, 1, 12]
result = largest_number(nums)
print("The largest number that can be formed is:", result)
