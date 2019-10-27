def selection_sort(alist):
    for i in range(0,len(alist)-1):
        min_value = min(alist[i:])
        min_index = alist.index(min_value)
        alist[i],alist[min_index] = min_value, alist[i]
        print(alist)
        print("_________")

if __name__ == "__main__":
   print(selection_sort([6,1,7,8,9,3,5,4,2]))
