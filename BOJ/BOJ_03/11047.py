#11047. 동전 0
#!/usr/bin/env python3
import sys
readl = sys.stdin.readline
if __name__ == "__main__":
    N,K = map(int, input().split())
    coin =[]
    for i in range(N):
        coin.append(int(input()))
    coin.sort(reverse=True)

    res = 0
    for i in range(N):
        res += K // coin[i] #몫 카운트
        K %= coin[i]
    print(res)