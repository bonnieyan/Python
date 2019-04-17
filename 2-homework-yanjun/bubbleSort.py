#冒泡排序
def bubbleSort(A):
    for i in range(len(A)-1):
        for j in range(len(A)-i-1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
    print(A)



if __name__ == '__main__':
    bubbleSort([1,15,2,5,3,18,6])

#ok