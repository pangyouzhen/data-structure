def quick_sort(array):
    if len(array) < 2:
        return array
    privot = array[0]
    # 快排最后采用的递归，而merge 在切分的时候就在递归
    lesser = [i for i in array[1:] if i <= privot]
    greater = [i for i in array[1:] if i > privot]
    return quick_sort(lesser) + [privot] + quick_sort(greater)


# O(nlogn) 最坏的情况下
# 快速排序的算法思想，分而治之+递归
if __name__ == '__main__':
    a = [5, 3, 1, 7, 7]
    print(quick_sort(a))

#  注意快速排序和merge排序一定要熟