# Write a Python function that takes a list of intervals (e.g., [[1, 3], [2, 4], [5, 7]]) and merges overlapping intervals.
# Example: Input: [[1, 3], [2, 4], [5, 7]] → Output: [[1, 4], [5, 7]].

# All Possible Overlaps
def mergeOverlap(arr):
    n = len(arr)
    arr.sort()
    res = []
    # Checking for all possible overlaps
    for i in range(n):
        start = arr[i][0]
        end = arr[i][1]
        # Skipping already merged intervals
        if res and res[-1][1] >= end:
            continue
        # Find the end of the merged range
        for j in range(i + 1, n):
            if arr[j][0] <= end:
                end = max(end, arr[j][1])
        res.append([start, end])
    return res
arr = [[1, 3], [2, 4], [5, 7]]
res = mergeOverlap(arr)
lis=[]
for interval in res:
    lis.append(interval)
print(lis)