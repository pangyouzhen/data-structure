import bisect

li = [21, 4, 5, 61, 45, 100]
li.sort()
print(li)
print(bisect.bisect(li, 200))
print(bisect.bisect(li, 45))
print(bisect.bisect_left(li, 45))
print(li)
bisect.insort_right(li, 5)
print(li)
