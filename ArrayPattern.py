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

'''Problem 3 (Maximum Sum Subarray of Size K):
Given an array of integers and a number k,
find the maximum sum of any contiguous subarray of 
size k.'''
k = 4
l1 = [40, 2, 4, 15, 34, 1, 9, 7, 45, 12]
left = 0
right = 0
current_window = l1[0] + l1[1] + l1[2] + l1[3]
max_sum = current_window
for right in range(k, len(l1)):
    current_window += l1[right]
    current_window -= l1[left]
    if current_window > max_sum:
        max_sum = current_window
    #print(f"left={left},right={right},current_window={current_window}, max={max_sum}")
    left += 1
print("Maximum sum subarray:", max_sum)

'''Problem 4 (Smallest Subarray with a Given Sum): 
Given an array of positive numbers and a positive number S, 
find the length of the smallest contiguous subarray whose sum 
is greater than or equal to S.'''
l1 = [40, 2, 4, 15, 34, 1, 9, 7, 45, 12]
left = 0
right = 0
current_sum = 0
min_length = len(l1) + 1
s = int(input("Enter the target number:"))
for right in range(len(l1)):
    current_sum += l1[right]
    while current_sum >= s:
        current_length = right - left + 1
        if min_length > current_length:
            min_length = current_length
        current_sum -= l1[left]
        left += 1

print("Sum =", min_length)

'''Problem 5 (Range Sum Query - Immutable): Given an 
integer array nums, handle multiple queries asking for 
the sum of elements between indices left and right inclusive.'''

def sum_range(left, right, num):
    #Solution1
    try:
        current_sum = sum(num[left:right+1])
        return current_sum
    except IndexError:
        return -1
    #Solution 2
    #try:
    #    list_sum = 0
    #    for index in range(left, right + 1):
    #        list_sum += num[index]
    #    return list_sum
    #except IndexError:
    #    return -1


list1 = [3, -5, 2, -1]
print("Sum =", sum_range(2, 5, list1))
print("Sum =", sum_range(0, 2, list1))
print("Sum =", sum_range(1, 2, list1))

'''Problem 6 (Best Time to Buy and Sell Stock): 
Given an array prices where prices[i] is the price of
a given stock on the i-th day, find the maximum profit
you can achieve by buying on one day and selling on a 
future day.'''

def max_profit(prices):
    if not prices:
        return -1
    min_price = prices[0]
    max_p = 0
    for price in prices:
        if price < min_price:
            min_price = price
        profit = price - min_price
        if profit > max_p:
            max_p = profit
    return max_p
prices = [7, 1, 5, 3, 6, 8]
print("Profit:", max_profit(prices))

