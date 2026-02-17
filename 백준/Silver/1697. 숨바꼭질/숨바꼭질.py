from collections import deque

def bfs(n, k):
    MAX = 100001
    visited = [False] * MAX
    queue = deque()

    queue.append((n, 0))
    visited[n] = True

    while queue:
        x, time = queue.popleft()

        if x == k:
            return time
        
        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx < MAX and not visited[nx]:
                visited[nx] = True
                queue.append((nx, time + 1))

N, K = map(int, input().split())
print(bfs(N, K))