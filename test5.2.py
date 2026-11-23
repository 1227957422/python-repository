a = int(input("首项: "))
q = int(input("公比: "))
n = int(input("项数: "))
S = 0
term = a
for i in range(n):
    S += term
    term = term * q
S = int(S)
print(S)