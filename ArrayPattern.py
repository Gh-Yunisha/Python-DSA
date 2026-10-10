'''Problem 1 (Two Sum II - Sorted Input): Given an array of integers sorted
in non-decreasing order and a target value, find two numbers such that they
add up to the target. Return their 1-based indices.'''
l = [2, 4, 6, 8, 10, 12]
tar = int(input("Enter the target for the list [2, 4, 6, 8, 10, 12]:"))
def two_Sum(l1, target):
    left = 0
    right = len(l1)-1
    while left < right:
        current_sum = l1[left] + l1[right]
        if current_sum == target:
            return [left + 1, right + 1]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []
print(two_Sum(l, tar))

