# n: 주전자의 개수
# k: 친구들의 수

n,k = map(int,input().split())
l = []

for _ in range(n):
    l.append(int(input()))

left, right = 1, max(l)
res = 0
while left <= right:
    mid = (left+right)//2
    num_pot = 0
    for i in l:
        num_pot += i//mid
    
    if num_pot >= k:
        # 더 늘려보자
        if mid > res:
            res = mid
        left = mid + 1
    else:
        right = mid - 1

print(res)
    
