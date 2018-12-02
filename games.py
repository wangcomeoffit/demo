import random
a=input("请输入您要猜的数:")
print(type(a))
#数字范围是[1,1000]
secret = random.randint(1, 1000)
guess = 0
while guess != secret:
    guess = int(input("Guess a number: "))
    if guess == 0:
        print("Sorry to see you go")
        break
    if guess > secret:
        print("too large")
    elif guess < secret:
        print("too small")
else:
    print("Congratulation!")