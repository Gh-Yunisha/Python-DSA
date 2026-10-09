arr = [50, 60, 80, 90]
#Indexing
def indexing(arr):
    print(len(arr),"\n", arr[0],"\n", arr[:1:-1])
indexing(arr)

#traversal
def traverse(a):
    for i in range(len(a)):
        print(a[i])
traverse(arr)

#Updating
def update(a):
    a[1:3] = ["Josh", "Manhattan"]
    print(a)
update(arr)

#insertion_append
arr.append("University of Texas")
print(arr)

#insertion at index
def insertion(arr, val, index):
    arr.append(None)
    for i in range(len(arr)-1, index, -1):
        arr[i] = arr[i-1]
    arr[index] = val
    return arr
print(insertion(arr, 70, 2))

#deletion
def deletion(a, index):
    val = a[index]
    for i in range(index, len(a)-1):
        a[i] = a[i+1]
    a.pop()
    return val
print(deletion(arr, 1))
print(arr)

#linear search
def linear_search(a, val):
    for i in range(len(a)):
        if a[i] == val:
            return i
    return -1
print(linear_search(arr, 90))

#reversal
def reversal(arr):
    l = len(arr)
    arr[:] = arr[-1:: -1]
    return arr
print(reversal(arr))

#Practice questions
arr = [10,20, 30, 0, 40, 50, 0, 0, 60, 70, 80, 90]
#Minimum and maximum in O(n)
def minimum(arr):
    smallest = arr[0]
    for i in arr:
        if i < smallest:
            smallest = i
    return smallest
def maximum(arr):
    largest = arr[0]
    for i in arr:
        if i > largest:
            largest = i
    return largest
print(arr)
print(minimum(arr))
print(maximum(arr))

#reversing the array in place without using the extra memory
def reversal(arr):
    l = len(arr)
    left = 0
    right = l-1
    mid = l // 2
    temp = 0
    for i in range(0, mid):
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp
        left += 1
        right -= 1
    print(arr)
print(arr)
reversal(arr)


#move zeros to end
def move_zeros(arr):
    pos = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[pos] = arr[i]
            pos += 1
    while pos < len(arr):
        arr[pos] = 0
        pos += 1
    print(arr)
print(arr)
move_zeros(arr)

#duplicate values, return true
def duplicate_check(a):
    dict1 ={}
    ans = True
    for i in arr:
        if i in dict1: # we can also use set(a)
            return True
            dict1[i] += 1
        else:
            dict1[i] = 1
            ans = False
    return ans
val = duplicate_check(arr)
print(val)

#rotate by k step
def rotate(arr, k):
    pos = 0
    arr1 = []
    for i in range(0, k): arr1.append(arr[i])
    for i in range(k, len(arr)):
        arr[pos] = arr[i]
        pos += 1
    i=0
    while pos < len(arr):
        arr[pos] = arr1[i]
        i += 1
        pos += 1
    print(arr)
rotate(arr, 3)












