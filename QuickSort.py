# a = [5,3,2,81,-7]
#
# pivot=a[0]
# l=0
# r=len(a)-1
# fp=l
# for i in range(l+1,r+1):
#     if a[i]>=pivot:
#         continue
#     fp+=1
#     a[fp],a[i]=a[i],a[fp]
# a[l],a[fp]=a[fp],a[l]
# print(a)

def quickSort(a, l, r):
    if l >= r:
        return
    pivot = a[l]
    fp = l
    for i in range(l + 1, r + 1):
        if a[i] >= pivot:
            continue
        fp += 1
        a[fp], a[i] = a[i], a[fp]
    a[l], a[fp] = a[fp], a[l]
    quickSort(a, l, fp - 1)
    quickSort(a, fp + 1, r)
a = [2, 1, 33, 4, -5, -89, 5]
print(a)
quickSort(a, 0, len(a) - 1)
print(a)
