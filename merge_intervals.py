#  merge overlapping intervals to produce new list that contains only non-overlapping intervals

def merge_intervals(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])  
    merged = [intervals[0]]

    for interval in intervals[1:]:
        if interval[0] > merged[-1][1]:  
            merged.append(interval)
        else:  
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged


intervals = [[4, 3], [2, 6], [8, 10], [15, 18]]
print(merge_intervals(intervals))  