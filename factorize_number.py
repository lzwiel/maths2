def factorize_number(num):
    factors = []
    divisor = 2

    while num > 1:
        if num % divisor == 0:
            factors.append(divisor)
            num /= divisor
        else:
            divisor += 1

    return factors

# 获取用户输入
number = int(input("请输入一个数字: "))

# 分解因式并输出结果
result = factorize_number(number)
print(f"{number} 的因式分解结果为: {result}")
