def solution(keyinput, board):
    answer = [0, 0]
    x_limit = board[0] // 2
    y_limit = board[1] // 2
    
    for cmd in keyinput:
        if cmd == 'up':
            if answer[1] < y_limit:
                answer[1] += 1
        elif cmd == 'down':
            if answer[1] > -y_limit:
                answer[1] -= 1
        elif cmd == 'left':
            if answer[0] > -x_limit:
                answer[0] -= 1
        elif cmd == 'right':
            if answer[0] < x_limit:
                answer[0] += 1

    return answer