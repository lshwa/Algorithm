from collections import deque

def solve(n, k):
    MAX = 100001
    dist = [-1] * MAX
    cnt = [0] * MAX 

    q = deque()
    q.append(n)         
    dist[n] = 0
    cnt[n] = 1 

    while q:
        x = q.popleft()

        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx < MAX:
                if dist[nx] == -1:
                    dist[nx] = dist[x] + 1
                    cnt[nx] = cnt[x]
                    q.append(nx)
                elif dist[nx] == dist[x] + 1:
                    cnt[nx] += cnt[x] 
    
    return dist[k], cnt[k]

N, K = map(int, input().split())
t, ways = solve(N, K)
print(t)
print(ways)