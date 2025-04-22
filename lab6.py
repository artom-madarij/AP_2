
n = int(input())

graph = {}
for _ in range(n):
    a, b = map(int, input().split())
    if a not in graph:
        graph[a] = []
    if b not in graph:
        graph[b] = []
    graph[a].append(b)
    graph[b].append(a)

visited = set()
tribes = []

def dfs(node, current_tribe):
    visited.add(node)
    current_tribe.append(node)
    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            dfs(neighbor, current_tribe)

for person in graph:
    if person not in visited:
        tribe = []
        dfs(person, tribe)
        tribes.append(tribe)

total_boys = 0
total_girls = 0
all = 0

for tribe in tribes:
    boys = sum(1 for person in tribe if person % 2 == 1)
    girls = sum(1 for person in tribe if person % 2 == 0)
    total_boys += boys
    total_girls += girls
    all += boys * girls

result = total_boys * total_girls - all
print(result)