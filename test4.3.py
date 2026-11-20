lst = list(map(int,input().split()))
product = 1
for num in lst:
    product *= num
print(product)