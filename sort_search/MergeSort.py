# TODO  2019
def mergeSort(arr):
    if len(arr) > 1:
        # divide
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        mergeSort(L)
        # when L = 12,mergeSort pass,So mergeSort(11) pass ,so go to while i < len()
        mergeSort(R)

        i = j = k = 0
        # merge
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


#
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7,78,3]
    print("given array is ", end="\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is ", end="\n")
    printList(arr)
