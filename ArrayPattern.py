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

'''Problem 2 (Valid Palindrome): Given a string or list of
characters, determine if it reads the same forward
and backward (ignore punctuation and case).'''

def palindrome(text):
    left = 0
    right = len(text)-1
    while left < right:
        while left < right and not text[left].isalnum():
            left += 1
        while left < right and not text[right].isalnum():
            right -= 1
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1
    return True

str1 = input("Enter the string: ").lower()
if palindrome(str1):
    print("Palindrome")
else:
    print("Not palindrome")

