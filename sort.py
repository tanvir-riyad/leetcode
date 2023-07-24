# bubble sort copmares adjacent elements and swaps them if they are in wrong order

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped  = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
       

print(bubble_sort([23, 45, 65, 35, 54, 76, 17, 1]))