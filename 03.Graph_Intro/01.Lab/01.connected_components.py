def dfs(node, graph, visited, component):
    if visited[node]:
        return
    visited[node] = True

    for child in graph[node]:
        dfs(child, graph, visited, component)

    component.append(node)


nodes_count = int(input())
graph = []

for node in range(nodes_count):
    line = input()
    children = [] if line == '' else [int(x) for x in line.split()]
    graph.append(children)

visited = [False] * nodes_count

for node in range(nodes_count):
    if visited[node]:
        continue
    component = []
    dfs(node, graph, visited, component)

    print(f'Connected component: {" ".join([str(c) for c in component])}')
