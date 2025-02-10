n = int(input())
points = []

# Read the segments
for _ in range(n):
    l, r = map(int, input().split())
    points.append((l, -1))
    points.append((r,1))
points.sort()
# print(points)

# Initialize variables
active_segments = 0
last_start = 0
total_length = 0
 # Sweep through the sorted endpoints
for point, kind in points:
    if active_segments == 0 and kind == -1:
        # Start of a new covered region
        last_start = point
    active_segments -= kind
    if active_segments == 0:
        # End of a covered region
        total_length += point - last_start

# Calculate and print the total covered length
print(total_length)