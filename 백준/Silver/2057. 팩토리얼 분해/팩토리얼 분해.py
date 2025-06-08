def fact(n):
    answer = 1
    for i in range(1, n + 1):
        answer *= i
    return answer
        
n = int(input())
fact_values = []

i = 0 
while True:
    f = fact(i)
    if f > n:
        break
    fact_values.append(f)
    i += 1

fact_values.reverse()

def dfs(idx, total, count):
    if total == n:
        return count >= 1
    if total > n or idx == len(fact_values):
        return False

    if dfs(idx + 1, total + fact_values[idx], count + 1):
        return True
    if dfs(idx + 1, total, count):
        return True

    return False

if dfs(0, 0, 0):
    print("YES")
else:
    print("NO")