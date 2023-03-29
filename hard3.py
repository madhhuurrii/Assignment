#  Hard 3: Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.
# Python Solution 
n=int(input())
c=0
for i in range(0,n+1):
    # print(i)
    temp=str(i)
    for j in temp:
        if int(j)==1:
            c=c+1
print(c)