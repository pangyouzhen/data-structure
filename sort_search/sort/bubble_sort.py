def bubble_sort(alist):
    for j in range(len(alist)-1,0,-1):
        for i in range(j):
            if alist[i] > alist[i+1]:
                alist[i],alist[i+1] = alist[i+1],alist[i]
        print(alist)
        print("_________")


if __name__ == '__main__':
    li = [5,9,3,1,2,8,4,7,6]
    bubble_sort(li)
    print(li)
