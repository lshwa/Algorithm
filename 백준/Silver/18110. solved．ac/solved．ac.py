import sys
input = sys.stdin.readline

N = int(input())
if N == 0:
    print(0)
    sys.exit()

scores = [int(input()) for _ in range(N)]
scores.sort()

cut = int(N * 0.15 + 0.5)

remain_sum = sum(scores[cut : N - cut])
remain_cnt = N - 2 * cut

print(int(remain_sum / remain_cnt + 0.5))