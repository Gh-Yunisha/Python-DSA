'''Task: Implement frequency_counter(items) that receives a list of items
(e.g., characters or strings) and returns a frequency dictionary
containing the item counts without using external modules like "collections.Counter".
def frequency_counter(items):
    dict1 = {}
    for k in items:
        k = k.lower()
        dict1[k] = dict1.get(k, 0) + 1
    return dict1
item = ["apple", "Banana", "coconut", "banana", "Apple", "Apple"]
print(frequency_counter(item))'''

'''Problem 1: Duplicate Detection
Given an integer array nums, return True if any value appears at least twice 
in the array, and False if every element is distinct.[Use a set to track unique numbers observed during iteration.]
Target Complexity: Time: O(N), Space: O(N).
#Dictionary-based
def frequency_counter(items):
    dict1 = {}
    for k in items:
        if dict1.get(k, 0) >= 1:
            return True
        else:
            dict1[k] = dict1.get(k, 0) + 1
    return False
num1 = [45, 2, 20, 19, 32, 0]
num2 = [45, 2, 20, 19, 32, 2]
print(frequency_counter(num1))
print()
print(frequency_counter(num2))

#Set-based
def duplicate_with_set(num):
    seen = set()
    for k in num:
        if k in seen:
            return True
        seen.add(k)
    return False
num1 = [45, 2, 20, 19, 32, 0]
num2 = [45, 2, 20, 19, 32, 2]
print(duplicate_with_set(num1))
print()
print(duplicate_with_set(num2))'''
