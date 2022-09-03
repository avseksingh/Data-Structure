a = [1,3,2,1,7]
for i in range(len(a)-1):
    if (a[i] <= a[i+1]):
        continue
    # print(a[i+1])
    j = i + 1
    t = a[j]
    while j >= 1 and a[j-1] > t:
        a[j] = a[j-1]
        j = j-1
    a[j] = t
    print("Array after ", i + 1, " iterations ", a)
print(a)

