def soln(a, k):
    mod_count = [0] * k
    count = 0
    
    # Populate the count of occurrences for each remainder
    for num in a:
        remainder = num % k
        mod_count[remainder] += 1

    # Handle the pairs for remainder 0 separately
    count += (mod_count[0] * (mod_count[0] - 1)) // 2
    
    # For the remaining numbers, pair i with k-i
    for i in range(1, (k + 1) // 2):
        count += mod_count[i] * mod_count[k - i]

    # If k is even, handle the exact middle case separately
    if k % 2 == 0:
        count += (mod_count[k//2] * (mod_count[k//2] - 1)) // 2

    return count



print(soln([1,2,3,4,5, 6, 7, 8, 9, 10], 5))

 # (k - a[i]) % k

# n % k == x
# m % k == y

# x + y % k == 0