import math

nums=input().split(',')
n=len(nums)
c=math.floor(n/3)
l=[]
for i in nums:
    if nums.count(i)>c and i not in l:
        l.append(i)
        
print(l)