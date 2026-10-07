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













