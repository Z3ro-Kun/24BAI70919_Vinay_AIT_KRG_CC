import sys
 
input = sys.stdin.readline
 
 
def solve():
    n = int(input())
    a = list(map(int, input().split()))
 
    k = 0
    while k < n and a[k] == 1:
        k += 1
 
    if k == n:
        if k % 2 == 1:
            print("First")
        else:
            print("Second")
    else:
        if k % 2 == 0:
            print("First")
        else:
            print("Second")
 
 
 
 
def main():
    t = int(input())
    for _ in range(t):
        solve()
 
if __name__ == "__main__":
    main()
