from collections import deque

def BFS(adj, s):
    visited = [False]*len(adj)
    q=deque()
    q.append(s)
    visited[s]=True
    while q:
        s=q.popleft()
        print(s, end="")
        for u in adj[s]:
            if visited[u]==False:
                q.append(u)
                visited[u]=True

adj=[[1,2], [0,2,3], [0,1,3,4], [1,2,4], [2,3]]
s = 0

BFS(adj, s)