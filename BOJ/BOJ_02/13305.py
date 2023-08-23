#13305. 주유소
#!/usr/bin/env python3
import sys
readl = sys.stdin.readline
sys.stdin= open("input.txt", "r")
if __name__ == "__main__":
    k = int(readl())
    dist = list(map(int, readl().split()))
    cost = list(map(int, readl().split()))
    res =0 
    c = cost[0]

    for i in range(k-1):
        if c > cost[i]:
            c = cost[i]
        res += c * dist[i]
    print(res)