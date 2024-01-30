import time

def swap(a, b):
    a, b = b, a

def copy_array(source, destination):
    for i in range(len(source)):
        destination[i] = source[i]

def bubble_sort(arr):
    start_time = time.time_ns()
    flag = 0
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = 1

        if flag == 0:
            break
    stop_time = time.time_ns()
    duration = stop_time - start_time  # nanoseconds
    print("Execution Time inside function:", duration, "nanoseconds")

def selection_sort(arr):
    start_time = time.time_ns()
    for i in range(len(arr) - 1):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[min_index], arr[i] = arr[i], arr[min_index]
        stop_time = time.time_ns()
    duration = stop_time - start_time  # nanoseconds
    print("Execution Time inside function:", duration, "nanoseconds")
    
    
def merge_sort(arr):
    start_time = time.time_ns()
    def merge(left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    stop_time = time.time_ns()
    duration = stop_time - start_time  # nanoseconds
    print("Execution Time inside function:", duration, "nanoseconds")
    return merge(left, right)

def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

def quick_sort(array, low, high):
    start_time = time.time_ns()
    if low < high:
        pi = partition(array, low, high)
        quick_sort(array, low, pi - 1)
        quick_sort(array, pi + 1, high)
    stop_time = time.time_ns()
    duration = stop_time - start_time  # nanoseconds
    print("Execution Time inside function:", duration, "nanoseconds")

a  = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
a1 = [30,29,28,27,26,25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0]
a2 = [0,1,3,2,6,4,30,29,28,27,26,18,19,20,21,22,23,24,25,7,8,9,10,11,12,13,14,15,16,17,5]
'''
arr = a.copy()
start_time = time.time_ns()
bubble_sort(arr)
stop_time = time.time_ns()
duration = stop_time - start_time  # nanoseconds
print("Execution BUBBLE SORT Time 1:", duration, "nanoseconds")

arr = a2.copy()
start_time2 = time.time_ns()
bubble_sort(arr)
stop_time2 = time.time_ns()
duration2 = stop_time2 - start_time2  # nanoseconds
print("Execution Time BUBBLE SORT 2:", duration2, "nanoseconds")

arr = a1.copy()
start_time1 = time.time_ns()
bubble_sort(arr)
stop_time1 = time.time_ns()
duration1 = stop_time1 - start_time1  # nanoseconds
print("Execution Time BUBBLE SORT 3:", duration1, "nanoseconds")
###########################################################################

arr = a.copy()
start_time = time.time_ns()
selection_sort(arr)
stop_time = time.time_ns()
duration = stop_time - start_time  # nanoseconds
print("Execution selection_sort Time 1:", duration, "nanoseconds")

arr = a2.copy()
start_time2 = time.time_ns()
selection_sort(arr)
stop_time2 = time.time_ns()
duration2 = stop_time2 - start_time2  # nanoseconds
print("Execution Time selection_sort 2:", duration2, "nanoseconds")

arr = a1.copy()
start_time1 = time.time_ns()
selection_sort(arr)
stop_time1 = time.time_ns()
duration1 = stop_time1 - start_time1  # nanoseconds
print("Execution Time selection_sort 3:", duration1, "nanoseconds")
'''
##################################################################################
arr = a.copy()
start_time = time.time_ns()
merge_sort(arr)
stop_time = time.time_ns()
duration = stop_time - start_time  # nanoseconds
print("Execution MERGE SORT Time 1:", duration, "nanoseconds")

arr = a2.copy()
start_time2 = time.time_ns()
merge_sort(arr)
stop_time2 = time.time_ns()
duration2 = stop_time2 - start_time2  # nanoseconds
print("Execution Time MERGE SORT 2:", duration2, "nanoseconds")

arr = a1.copy()
start_time1 = time.time_ns()
merge_sort(arr)
stop_time1 = time.time_ns()
duration1 = stop_time1 - start_time1  # nanoseconds
print("Execution Time MERGE SORT 3:", duration1, "nanoseconds")
'''
#################################################################################
arr = a.copy()
start_time = time.time_ns()
quick_sort(arr,0,29)
stop_time = time.time_ns()
duration = stop_time - start_time  # nanoseconds
print("Execution Quick SORT Time 1:", duration, "nanoseconds")

arr = a2.copy()
start_time2 = time.time_ns()
quick_sort(arr,0,29)
stop_time2 = time.time_ns()
duration2 = stop_time2 - start_time2  # nanoseconds
print("Execution Time Quick SORT 2:", duration2, "nanoseconds")

arr = a1.copy()
start_time1 = time.time_ns()
quick_sort(arr,0,29)
stop_time1 = time.time_ns()
duration1 = stop_time1 - start_time1  # nanoseconds
print("Execution Time Quick SORT 3:", duration1, "nanoseconds")
##########################################################################
'''