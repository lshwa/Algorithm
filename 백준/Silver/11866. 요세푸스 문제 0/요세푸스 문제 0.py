from collections import deque
def yosaa(n,k):
    people = deque(range(1, n + 1))
    result = []

    while people:
        people.rotate(-(k - 1))  
        result.append(people.popleft()) 

    print("<" + ", ".join(map(str, result)) + ">")

n, k = map(int,input().split())
yosaa(n, k)

