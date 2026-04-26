import sys

input = sys.stdin.readline





def main():
    n = int(input())
    a = list(map(int, input().split()))

    initial_ones = sum(a)

    gain = [1 if x == 0 else -1 for x in a]
    max_gain = gain[0]
    current = gain[0]

    for i in range(1, n):
        current = max(gain[i], current + gain[i])
        max_gain = max(max_gain, current)
    if max_gain <= 0:
        print(n - 1)
    else:
        print(initial_ones + max_gain)


if __name__ == "__main__":
    main()
