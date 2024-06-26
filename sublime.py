def find_segments(arr, m, d):
    count = 0
    n = len(arr)

    # Iterate over all possible starting points of the segments
    for i in range(n - m + 1):
        # Sum the segment of length m starting at index i
        if sum(arr[i:i + m]) == d:
            count += 1
    
    return count

# Example usage:
arr = [2, 2, 1, 3, 2]
m = 2  # Raju's birth month
d = 4  # Raju's birth day

result = find_segments(arr, m, d)
print(result)  # Output should be 2
