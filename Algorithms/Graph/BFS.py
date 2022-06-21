
def breathFirstSearch(graph, s, e):
    queue = [s]
    prev = [s]*len(graph)
    used = [False]*len(graph)

    while len(queue) > 0:
        for node in graph[queue[0]]:
            if not used[node]:
                prev[node] = queue[0]
                if node == e:
                    cur = node
                    path = [node]
                    while cur != s:
                        cur = prev[cur]
                        path.insert(0, cur)
                    return path
                used[node] = True
                queue.append(node)

        queue = queue[1:]

    return None


graph = [[1, 2], [2, 4], [0, 3], [0, 4], [1]]
print(breathFirstSearch(graph, 0, 4))
