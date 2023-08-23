#거스름돈
import sys
import os
if __name__ == '__main__':
    money = [500, 100, 50, 10]
    amount =[0, 0, 0, 0]
    cnt = 0

    N = int(sys.stdin.readline())

    for i in range(len(money)) : 
        val = N // money[i]
        N = N % money[i]
        amount[i] = val
        cnt = cnt + amount[i]

    print(cnt)