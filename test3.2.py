a_text = input()
b_text = input()
s1 = set(a_text.split())
s2 = set(b_text.split())
jiaoji = s1&s2
bingji = s1|s2
cha1 = s1 - s2
cha2 = s2 - s1
print(jiaoji)
print(bingji)
print(cha1)
print(cha2)