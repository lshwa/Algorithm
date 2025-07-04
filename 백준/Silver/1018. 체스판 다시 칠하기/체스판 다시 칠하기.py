import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [input().strip() for _ in range(N)]

answer = 64

for row in range(N - 7):
    for col in range(M - 7):
        mismatch = 0
        for i in range(8):
            for j in range(8):
                expected = 'W' if (i + j) % 2 == 0 else 'B'
                if board[row + i][col + j] != expected:
                    mismatch += 1
        repaint = min(mismatch, 64 - mismatch)
        answer = min(answer, repaint)
    
print(answer)
