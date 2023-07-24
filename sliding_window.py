# sliding window maximum

def find_sliding_windows_max(arr, size):
    left = 0
    right = size
    result_list = []
    i = 0
    while i < len(arr)-(size-1):
        window_element = arr[left:right]
        print(window_element)
        maxVal = max(window_element)
        result_list.append(maxVal)
        right+=1
        left +=1
        i+=1
    return result_list

print(find_sliding_windows_max([2,4,-3,4,6,3,-9,5], 3))

