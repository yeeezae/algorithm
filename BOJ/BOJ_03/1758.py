#1758. 알바생 강호
#!/usr/bin/env python3
import sys
readl = sys.stdin.readline
sys.stdin= open("input.txt", "r")
if __name__ == "__main__":
    N = int(input())
    tip = []
    res = 0
    for i in range(N):
        tip.append(int(readl().strip()))
    tip.sort(reverse=True)

    for i in range(N):
        value = tip[i] - ((i+1) -1)
        if value > 0:
            res += value
    print(res)