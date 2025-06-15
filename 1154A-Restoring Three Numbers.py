# Input: four integers
nums = list(map(int, input().split()))

# Sort the list to easily identify the largest value (a + b + c)
nums.sort()

# The largest number is the total sum: a + b + c
total = nums[3]

# The remaining values are pairwise sums
# We can get the original numbers:
a = total - nums[2]
b = total - nums[1]
c = total - nums[0]

# Print the result (can be in any order)
print(a, b, c)
