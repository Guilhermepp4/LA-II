def complete(graph, candidate):
    if len(candidate) < 2:
        return False
    if candidate[0] in graph[candidate[-1]] and candidate[-1] in graph[candidate[0]]:
        return True
    return False

def extensions(graph, candidate, nodes):
    ext = []
    if not candidate:
        for nxt in nodes:
            ext.append(nxt)
    else:
        for nxt in graph[candidate[-1]]:
            if nxt not in candidate:
                ext.append(nxt)
    return ext

def valid(graph, candidate):
    for key in graph:
        if key not in candidate:
            return False
    return True

def search(graph, candidate):

    if complete(graph, candidate):
        print(candidate)
        if valid(graph, candidate):
            return candidate
    for ext in extensions(graph, candidate, [x for x in graph]):
        new_candidate = candidate.copy()
        new_candidate.append(ext) 
        result = search(graph, new_candidate)
        if result:
            return result
    return None

def mkgraph(arestas, graph):

    for aresta in arestas:
        if aresta[0] not in graph:
            graph[aresta[0]] = []
        graph[aresta[0]].append(aresta[1])
        if aresta[1] not in graph:
            graph[aresta[1]] = []
        graph[aresta[1]].append(aresta[0])
    return graph

def hamilton(arestas):
    if not arestas:
        return None
    graph = mkgraph(arestas, {})
    return search(graph, [])

# 90 %