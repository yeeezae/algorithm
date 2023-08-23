#20115. 에너지 드링크
#!/usr/bin/env python3
import sys
readl = sys.stdin.readline
if __name__ == "__main__":
    N = int(input())
    energy_drink =list(map(int, input().split()))
    res = 0
    
    energy_drink.sort()
    res = energy_drink[N-1] #마지막 인덱스가 최대
    for i in range(N-1): #마지막 인덱스의 전까지 돌기
        res += energy_drink[i] / 2
    
    print(res)