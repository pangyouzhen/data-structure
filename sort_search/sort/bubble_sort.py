def bubble_sort(alist):
    for i  in range(1,len(alist)):
        for j in range(0,len(alist)-i):
            if alist[j] > alist[j+1]:
                alist[j],alist[j+1] = alist[j+1],alist[j]
        print(alist)
        print("_________")


if __name__ == '__main__':
    li = [5,9,3,1,2,8,4,7,6]
    bubble_sort(li)
    print(li)
