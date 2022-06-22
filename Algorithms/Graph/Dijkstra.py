
from cmath import inf


def Dijkstra(graph, node1):
    s = node1
    n = len(graph)
    d = [inf]*n
    used = [False]*n
    p = [None]*n
    d[s] = 0

    for i in range(n):
        v = -1
        for j in range(n):
            if not used[j] and (v == -1 or not d[j]):
                v = j

        if d[v] == None:
            break

        used[v] = True

        for j in range(len(graph[v])):
            to = graph[v][j][0]
            lenn = graph[v][j][1]
            if d[to] > d[v] + lenn:
                d[to] = d[v] + lenn
                p[to] = v

    return d, p


d, p = Dijkstra([[[1, 3]], [[0, 2]]], 0)

print(d)
print(p)
