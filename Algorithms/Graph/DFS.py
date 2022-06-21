graph = [[1, 2], [2], [0]]
used = [False]*len(graph)


def depthFirstSearch(graph, s, e, path=[]):
    path = path + [s]
    used[s] = True
    if s == e:
        return path
    for node in graph[s]:
        if not used[node]:
            used[node] = True
            new_path = depthFirstSearch(graph, node, e, path)
            if new_path:
                return new_path
    return None


print(depthFirstSearch(graph, 0, 2))
