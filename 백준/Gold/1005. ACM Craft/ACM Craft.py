import sys
from collections import deque

input = sys.stdin.readline

def solve():
    T = int(input())
    for _ in range(T):
        N, K = map(int, input().split())
        t = [0] + list(map(int, input().split()))  

        graph = [[] for _ in range(N + 1)]
        indeg = [0] * (N + 1)

        for _ in range(K):
            x, y = map(int, input().split())
            graph[x].append(y)
            indeg[y] += 1

        W = int(input())

        dp = t[:]  # dp[i] = i 완성 최소 시간 (초기: 자기 짓는 시간)

        q = deque()
        for i in range(1, N + 1):
            if indeg[i] == 0:
                q.append(i)

        while q:
            u = q.popleft()
            for v in graph[u]:
                # u를 끝낸 뒤 v를 지을 수 있으므로, v의 후보 시간 갱신
                if dp[v] < dp[u] + t[v]:
                    dp[v] = dp[u] + t[v]

                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        print(dp[W])

if __name__ == "__main__":
    solve()