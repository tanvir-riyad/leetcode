#  each rotation finds the right place of each element of the given array
arr = [23, 3, 31, 24, 5, 3]
def cycleSort(arr):
    for cycle_start in range(0, len(arr)-1):
        item = arr[cycle_start]
        pos = cycle_start 
        for i in range(cycle_start+1, len(arr)):   
            if arr[i] < item:
                pos +=1

        if pos == cycle_start:
            continue

        while item == arr[pos]:
            pos += 1
        arr[pos], item = item, arr[pos]
        
        while pos != cycle_start:
            pos = cycle_start
            for i in range(cycle_start+1, len(arr)):
                if arr[i] < item:
                    pos +=1
    
            while item == arr[pos]:
                pos += 1
            arr[pos], item = item, arr[pos]
            
    return arr



            

print(cycleSort(arr))