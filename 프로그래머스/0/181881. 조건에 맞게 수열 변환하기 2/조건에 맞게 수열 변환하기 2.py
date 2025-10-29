def solution(arr):
    x = 0 
    while True:
        new_arr = []
        for n in arr:
            if n >= 50 and n % 2 == 0:
                new_arr.append(n // 2)
            elif n < 50 and n % 2 == 1:
                new_arr.append(n * 2 + 1)
            else:
                new_arr.append(n)
        
        if new_arr == arr:  # 변화 없음 → 안정 상태
            return x
        
        arr = new_arr  # 다음 반복을 위해 갱신
        x += 1