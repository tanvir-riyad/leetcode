# it works for sorted array. find unique pairs of elements with the given difference

def find_pairs_with_difference(arr, k):
    arr.sort()
    result_list = []
    left = 0
    right = 1
    while right < len(arr):
        diff = arr[right] - arr[left]
        
        if diff == k:
            result_list.append((arr[left], arr[right] ))
            right += 1
            left += 1
        elif diff < k:
            right += 1
        else:
            left += 1

        while left < right and arr[left]==arr[left-1]:
            left +=1
        while right< len(arr)-1 and arr[right] == arr[right+1]:
            right +=1

    return result_list



print(find_pairs_with_difference(arr=arr, k =32))
    