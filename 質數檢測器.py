import time

# ============= 運算 ================
def is_prime(num):
    test = []
    n = 1
    while n < num/2:
        if num % n == 0:
            test.append(int(n))
            test.append(int(num / n))
        n += 1
        if n in test or len(test) > 2:
            break
    return True if len(test) == 2 else False
# ============= 運算 ================
print("檢測質數的機器")
print("不要繼續請輸入除了數字以外的字")
while True:
    try:
        user = int(input("請輸入一整數: "))
        if user >= 5:
            t = is_prime(user)
            if t == True:
                print("%s 是質數" % user)
            else:
                print("%s 不是質數" % user)
        else:
            if user == 0 or user == 4:
                print("%s 不是質數" % user)
            else:
                print("%s 是質數" % user)
    except:
        print("作者: 王宥傑")
        time.sleep(1.5)
        break
