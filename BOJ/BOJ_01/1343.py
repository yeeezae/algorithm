#1343. 폴리오미노
#!/usr/bin/env python3
import sys
#sys.stdin=open('input.txt', 'r')
readl =sys.stdin.readline

if __name__ == '__main__':
    arr = readl() #불러올 XX..XXX..배열
    result = "" #AAAABB..BB.BB.. 저장할 배열"
    cnt = 0
    arr += ' '
    for i in range(len(arr)-1): #arr 끝 바로 전까지 탐색
        if arr[i] == 'X' : #arr의 i번째가 X면 cnt+1
            cnt += 1
        if arr[i] == '.': #arr의 i번째가 .면 result에 .저장
            result += '.'
            if cnt % 2 != 0: #cnt가 홀수면 못넣어줌으로 break
                break
            else:
                cnt = 0
        if cnt == 2 and arr[i+1] != 'X': #cnt가 2고 뒤에 더이상 X가 없으면 result에 "BB" 저장
            result += "BB"
        elif cnt == 4: #cnt가 4면 result에 "AAAA" 저장
            result += "AAAA"
            cnt = 0

    if cnt % 2 == 1:
        print(-1)
    else:
        print(result)