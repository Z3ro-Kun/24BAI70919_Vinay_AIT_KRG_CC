import sys

input = sys.stdin.readline


def main():
    n = int(input())
    edges = []
    adj = [[] for _ in range(n)]

    for i in range(n - 1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        edges.append((u, v))
        adj[u].append((v, i))
        adj[v].append((u, i))

    center = -1
    for i in range(n):
        if len(adj[i]) >= 3:
            center = i
            break

    labels = [-1] * (n - 1)

    if center == -1:
        for i in range(n - 1):
            labels[i] = i
    else:
        cur = 0
        for (to, idx) in adj[center]:
            if cur < 3:
                labels[idx] = cur
                cur += 1
        cur = 3
        for i in range(n - 1):
            if labels[i] == -1:
                labels[i] = cur
                cur += 1
    for label in labels:
        print(label)

if __name__ == "__main__":
    main()
