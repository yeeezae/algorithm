#2217. 로프
#!/usr/bin/env python3
import sys
if __name__ == "__main__":
    N =int(input())
    ropes =[]
    cnt = 0
    max = 0
    for i in range(N):
        ropes.append(int(input()))
    ropes.sort(reverse=True) #역순 정렬
    for i in range(len(ropes)):
        rope = ropes[i]
        val = rope * (i+1)
        if val > max:
            max = val
    print(max)