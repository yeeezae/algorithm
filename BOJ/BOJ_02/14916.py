#1343. 거스름돈
#!/usr/bin/env python3
import sys
if __name__ == "__main__":
    cnt =0
    money=int(input())
    while money > 0:
        if money % 5 == 0: # 5의배수이면 or 2로만 거슬러주고 n이 0이된경우 
            cnt += money //5 #5로나눈 몫이 정답 
            break
        else:
            money -= 2 #5의배수가 아니면 2원씩 뺴면서 5로 나누어떨어지는것이 나오도록
            cnt += 1
        if money < 0:
            break
            
    if money<0:
        print(-1)			
    else:
        print(cnt) 