# m = 조카의 수
# n = 과자의 수
# time taken: 20 min
m,n = map(int,input().split())
l = list(map(int,input().split()))
left,right = 1, max(l)
res = 0
while left<= right:
    mid = (left+right)//2
    count = 0
    for i in l:
        count +=  i//mid
    if count >= m:
        # 늘려보자
        if mid > res:
            res = mid
        left = mid + 1
    else:
        # 줄여보자
        right = mid -1


print(res)
        
    




