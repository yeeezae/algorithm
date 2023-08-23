#곱하기 혹은 더하기
#!/usr/bin/env python3
import sys

if __name__ == '__main__':
    data = input()
    #첫번째 문자를 숫자로 변경하며 대입
    result = int(data[0])
    # 두 수중에서 하나라도 '0' 혹인 '1'인 경우, 곱하기 보다는 더하기 수행
    for i in range(1, len(data)):
        num = int(data[i])
        if num <= 1 or result <=1:
            result += num
        else:
            result *= num
    print(result)