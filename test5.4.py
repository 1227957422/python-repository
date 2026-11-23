s = input("请输入任意长的字符串: ")
freq = {}
for ch in s:
    if ch.isalnum():
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
print("字母和数字的频次字典:")
print(freq)