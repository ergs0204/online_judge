n = int(input())  # Read number of days
revenues = []
dp = []  # dp[i] will store the minimum revenue seen up to day i

# Read daily revenues
for _ in range(n):
    revenues.append(int(input()))

# First day's fluctuation is equal to its revenue
total_fluctuation = revenues[0]

# For each subsequent day
for i in range(1, n):
    # Find minimum fluctuation by comparing with all previous days
    min_fluctuation = abs(revenues[i] - revenues[0])
    for j in range(1, i):
        current_fluctuation = abs(revenues[i] - revenues[j])
        min_fluctuation = min(min_fluctuation, current_fluctuation)
    total_fluctuation += min_fluctuation

print(total_fluctuation)