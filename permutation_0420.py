#!/usr/bin/env python3
d=[]
rec=[]
N=0
def dfs(idx, length):
    if idx >= length:
        print(res)
        return
    for i in range(len(arr)):
        if visited[i] ==0 and arr[i] > res[idx-1]:
            visited[i] =1
            res[idx] =arr[i]
            dfs(idx+1,length)
            visited[i] =0
if __name__ == "__main__":
    arr= [i+1 for i in range(6)]
    visited = [0 for i in range(6)]
    res = [0 for i in range(4)]

    for i in range(len(arr)):
        visited[i]=1
        res[0] = arr[i]
        dfs(1,4)
        visited[i]=0