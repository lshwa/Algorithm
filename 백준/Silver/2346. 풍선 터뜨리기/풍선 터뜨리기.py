from collections import deque

def solution(n, papers):
    dq = deque((i + 1, papers[i]) for i in range(n))
    result = []

    while dq:
        idx, move = dq.popleft()
        result.append(idx)

        if not dq:
            break

        if move > 0:
            dq.rotate(-(move - 1))

        else:
            dq.rotate(-move)

    return result

n = int(input())
papers = list(map(int, input().split()))

print(*solution(n, papers))