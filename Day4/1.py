"""
for循环实现1到100的求和
vserion 0.1
Author: Morpheus
"""
"""
sum = 0
for x in range(101):
    sum += x
print(sum)

"""

"""
猜数字游戏
计算机出一个1~100之间的随机数由人来猜
计算机根据人猜的数字分别给出提示大一点/小一点/猜对了

Version: 0.1
Author: Morpheus
"""
"""
import random

answer = random.randint(1, 100)
counter = 0
while True:
    counter += 1
    number = int(input('请输入：'))
    if number < answer:
        print('小一点')
    elif number > answer:
        print('大一点')
    else:
        print("恭喜你猜对了！")
        break;
print('你总共猜了%d次' % counter)
if counter > 10:
    print("你的智商余额明显不足")

"""

"""
for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d*%d=%d' % (i, j, i * j), end='\t')
    print()
    
"""

"""
from math import sqrt

num = int(input('请输入一个正整数: '))
end = int(sqrt(num))
print('end = %d' % (end))
is_prime = True
for x in range(2, end + 1):
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print('%d是素数' % num)
else:
    print('%d不是素数' % num)
"""


