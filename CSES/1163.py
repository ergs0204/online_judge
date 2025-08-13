import bisect

x, n = map(int, input().split())
positions = list(map(int, input().split()))

lights = [0, x]  # initially lights at both ends
intervals = [x]  # initially one interval of length x

# Sort lights list maintained
# Intervals list maintained sorted (largest interval is intervals[-1])

for p in positions:
    # Insert new light position in order
    i = bisect.bisect_left(lights, p)
    left = lights[i-1]
    right = lights[i]

    # Remove old interval
    old_length = right - left
    # Remove from intervals
    remove_idx = bisect.bisect_left(intervals, old_length)
    intervals.pop(remove_idx)

    # Insert two new intervals
    bisect.insort(intervals, p - left)
    bisect.insort(intervals, right - p)

    # Insert p into lights
    lights.insert(i, p)

    print(intervals[-1], end=' ')
