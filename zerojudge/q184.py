n,k=map(int,input().split())
x=sorted(list(map(int,input().split())))

# Calculate cost for each interval of length k using sliding window
d = []
# Calculate first interval cost
i = k-1
med = (i + i-k+1) // 2
cost = 0
for j in range(i-k+1, i+1):
    cost += abs(x[j] - x[med])
d.append(cost)

# Use sliding window for remaining intervals
for i in range(k, n):
    left = i-k+1
    right = i
    prev_med = (i-1 + i-k) // 2
    med = (i + i-k+1) // 2
    
    # Calculate cost difference using the formula:
    # (x[right]-x[med]) - (x[prev_med]-x[left-1]) + 
    # (x[med]-x[prev_med])*(med+med-left-right)
    cost_diff = (x[right]-x[med]) - (x[prev_med]-x[left-1]) + \
                (x[med]-x[prev_med])*(med+med-left-right)
    
    cost = d[-1] + cost_diff
    d.append(cost)
# Calculate prefix minimums
pmin = []
curr_min = float('inf')
for i in range(len(d)):
    curr_min = min(curr_min, d[i])
    pmin.append(curr_min)

# Find best combination of two non-overlapping intervals
best = float('inf')
for i in range(k, len(d)):  # starting from k to ensure non-overlap
    total_cost = d[i]
    if i-k >= 0:
        total_cost += pmin[i-k]
    best = min(best, total_cost)

print(best)

