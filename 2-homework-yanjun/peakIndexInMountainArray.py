# 山脉数组
# 遍历了2次  时间复杂度是O(n^2)
def peakIndexInMountainArray(A):
    index = 0
    for i in range(1, len(A)):
        if A[i - 1] < A[i] > A[i + 1]:
            index = i
            # break  这里加上break 跳出语句减少循环次数
    print(index)


if __name__ == '__main__':
    peakIndexInMountainArray([0, 1, 0])
    peakIndexInMountainArray([0, 2, 1, 0])


# 通过二分查找实现 O(log2n)
def peakIndexInMountainArray(mountain):
    height = len(mountain)
    low = 0
    while low <= height:
        mid = (height + low) // 2
        if array[mid] > array[mid - 1] and array[mid] > array[mid + 1]:
            print(mid)
            break
        elif array[mid] > array[mid + 1]:
            height = mid - 1
        else:
            low = mid + 1


array = [0, 1, 0]
peakIndexInMountainArray(array)
array = [0, 2, 1, 0]
peakIndexInMountainArray(array)
array = [0, 1, 2, 3, 7, 6, 5, 4, 2, 1, 0]
peakIndexInMountainArray(array)
array = [0, 1, 2, 7, 6, 5, 4, 0]
peakIndexInMountainArray(array)
