#모험가 길드
#!/usr/bin/env python3
import sys

if __name__ == '__main__':
    n = int(input())
    data = list(map(int, input().split()))
    data.sort() #정렬

    result = 0 #총 그룸의 수
    count = 0 #현재 그룸에 포함된 모험가의 수

    for i in data: #공포도를 낮은 것부터 하나씩 확인하며
        count += 1 #현재 그룹에 해당 모헙가를 포함
        if count >= i: #현재 그룹애 포함된 모험가의 수 가 현재의 공포도 이상이라면, 그룸 결성
            result += 1 #총 그룸수 증가
            count = 0 #현재 그룹에 포함된 모험가의 수 초기화
    print(result) #총 그룹수 출력