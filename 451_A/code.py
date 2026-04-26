import sys

input = sys.stdin.readline



def main():
    n, m=map(int, input().split())
    if (min(n,m))%2==1:
        print("Akshat")
    else:
        print("Malvika")

if __name__ == "__main__":
    main()
