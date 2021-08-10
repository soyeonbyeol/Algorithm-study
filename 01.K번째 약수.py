import sys
#sys.stdin=open("input.txt", "rt")



n, k = map(int, input().split())
#list = []
#for i in range(1,n):
#    if n%i != 0:
#        list.append(i)
#if len(list) < k:
#        print(-1)
#elif len(list) >= k:
#        print(list[k-1])



cnt = 0
for i in range(1, n+1):
    if n%i == 0:
        cnt += 1
    if cnt == k:
        print(i)
        break
else:
    print(-1)