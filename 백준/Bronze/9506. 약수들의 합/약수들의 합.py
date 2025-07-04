import sys
input = sys.stdin.readline

def check_perfect(n : int) -> None:
    divisors = [i for i in range(1, n) if n % i == 0]

    if sum(divisors) == n:
        print(f"{n} = " + " + ".join(map(str, divisors)))
    else:
        print(f"{n} is NOT perfect.")

while True:
    num = int(input())
    if num == -1:
        break
    check_perfect(num)