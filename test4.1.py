lstA = list(map(int,input().split()))
lstB = list(map(int,input().split()))
n = min(len(lstA), len(lstB))
result_dict = {}
for i in range(n):
    result_dict[lstA[i]] = lstB[i]
print(result_dict)