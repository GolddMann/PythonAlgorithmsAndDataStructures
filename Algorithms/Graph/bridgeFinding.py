
graph = []
used = [False]*len(graph)
tin = [None]*len(graph)
fup = [None]*len(graph)
bridges = []
timer = 0


def dfs(v, p=-1):
    used[v] = True
    tin[v] = fup[v] = timer
    timer += 1
    for i in range(len(graph[v])):
        to = graph[v][i]
        if to == p:
            continue
        if used[to]:
            fup[v] = min(fup[v], tin[to])
        else:
            dfs(to, v)
            fup[v] = min(fup[v], fup[to])
            if(fup[to] > tin[v]):
                bridges.append([v, to])


if __name__ == "__main__":
    pass
