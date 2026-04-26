import sys

input = sys.stdin.readline


def solve():
    n = int(input())
    if n == 2:
        print(-1)
        return
    nums = []
    for i in range(1, n * n + 1, 2):
        nums.append(i)
    for i in range(2, n * n + 1, 2):
        nums.append(i)
    for i in range(n):
        row = nums[i * n:(i + 1) * n]
        print(*row)


def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
