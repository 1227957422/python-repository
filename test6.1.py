import random
secret = random.randint(1,100)
max_times = 5
for i in range(max_times):
    try:
        guess = int(input(f"第{i+1}次猜测，请输入数字："))
    except ValueError:
        continue
    if guess == secret:
        print("猜对了!")
        break
    if guess > secret:
        print("太大了")
    else:
        print("太小了")
else:
    print(f"次数用完，正确答案是：{secret}")