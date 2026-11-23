s = input("请输入一个字符串: ")
count = {}
for ch in s:
    if ch in count:
        count[ch] += 1
    else:
        count[ch] = 1
max_char = None
max_count = 0
for ch, num in count.items():
    if num > max_count:
        max_char = ch
        max_count = num
print(f"出现次数最多的字符: '{max_char}'，出现次数: {max_count}")