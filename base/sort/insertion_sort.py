def insertion_sort(alist):
    t = 1
    while t < len(alist):
        insert(alist, t)
        t = t + 1
        print(alist)
        print("_____")
    return alist


def insert(alist, t):
    while alist[t] < alist[t - 1] and t > 0:
        alist[t], alist[t - 1] = alist[t - 1], alist[t]
        t = t - 1
    return alist


if __name__ == "__main__":
    print(insertion_sort([5, 3, 4, 7, 2, 8, 6, 9, 1]))
