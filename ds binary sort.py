def BInarySearch(a, value):
    left = 0
    right = len(a) - 1
    count = 0
    while True:
        count += 1
        mid = (left + right) // 2
        print(mid, count, a[mid], value, a[left:mid + 1], a[mid + 1:right + 1])
        if a[mid] == value:
            return mid, count
        if value < a[mid]:
            right = mid - 1
        else:
            left = mid + 1
        if left > right:
            return -1, count

a = [x for x in range(1,101)]
result = BInarySearch(a, 56)
print(result)




"""
left = 0
mid = 0
right = len(a) - 1
find = int(input("Enter Value to chek in array: "))
count = 0
if a[left] == find:
    count += 1
    result = left
elif a[right] == find:
    count += 1
    result = right
else:
    for i in a:
        mid = int((left + right)/2)
        if a[mid] == find:
            result = mid
            break
        elif a[mid] < find:
            count += 1
            left = mid + 1
        else:
            count += 1
            right = mid - 1
print("Array Index", result, "and number of Attempt is ", count)
"""
