'''Problem 1: Valid Palindrome (Two Pointers)
Given a string s, return True if it is a palindrome, considering
only alphanumeric characters and ignoring cases. Otherwise, return False.
[Two Pointers (left starting at 0, right at len(s) - 1). Skip
non-alphanumeric characters using .isalnum() on the fly to achieve O(1) extra space.]
Target Complexity: Time: $O(N)$, Space: $O(1)$.
def valid_palindrome(a):
    left = 0
    right = len(a)-1
    while left < right:
        while left < right and not a[left].isalnum():
            left += 1
        while left < right and not a[right].isalnum():
            right -= 1
        if a[left] != a[right]:
            return False
        left += 1
        right -= 1
    return True
str1 = input("Enter the string to check palindrome:").lower()
if valid_palindrome(str1):
    print("Palindrome")
else:
    print("Not Palindrome")'''









