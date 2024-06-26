def count_divisible_pairs(arr, k):
    count = 0  # Start with no good pairs
    n = len(arr)  # Count how many numbers are in the list

    # Look at each number in the list
    for i in range(n):
        # For each number, look at all the numbers that come after it
        for j in range(i + 1, n):
            # If the sum of the two numbers is divisible by k
            if (arr[i] + arr[j]) % k == 0:
                count += 1  # We've found a good pair, so we count it
    
    return count  # After checking all pairs, return the count of good pairs

# Example usage:
arr = [1, 2, 3, 4, 5]  # List of numbers
k = 3  # Special number

result = count_divisible_pairs(arr, k)
print(result)  # This should print 4, which is the number of good pairs
