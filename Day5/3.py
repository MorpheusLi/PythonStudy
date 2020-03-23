"""
寻找水仙花数
Author:Morpheus
"""
for num in range(100, 1000):
    low = num % 10
    mid = num // 10 % 10
    hight = num // 100
    if num == low ** 3 + mid ** 3 + hight ** 3:
        print(num)
