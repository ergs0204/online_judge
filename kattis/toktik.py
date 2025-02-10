n = int(input())
views = {}
for i in range(n):
    tikker, views = input().split()
    views = int(views)
    views[tikker] = views.get(tikker, 0) + views

m = max(views, key=views.get)
print(m)
