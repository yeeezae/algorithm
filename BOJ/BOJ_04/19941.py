#19941. 햄버거분배
#!/usr/bin/env python3
import sys
if __name__ == "__main__":
    N,K = map(int,input().split())
    hamburger = input().rstrip()
    eat_list = list(hamburger) #입력해준 햄버거,사람을 리스트로 저장
    cnt = 0
    for i in range(len(eat_list)):
        if eat_list[i] == "P": #P 만나면 주변 탐색
        	#P 주변 K기준으로 전 후만큼 거리에 H가 있는지 확인
            for j in range (i-K, i+K+1): 
            	#사람이 만약 맨 처음에 나온다면 j가 -1이 될 수 있으므로 조건 추가
                if 0<=j<N and eat_list[j] == "H": 
                    cnt += 1
                    eat_list[j] ="0" #이미 먹은 햄버거는 다른 문자로 표시
                    break
    print(cnt)