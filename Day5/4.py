"""
《百钱百鸡》问题

Version: 0.1
Author: 骆昊
"""

for x in range(0, 20):
    for y in range(0, 33):
        z = 100 - x - y
        if 5 * x + 3 * y + z / 3 == 100:
            print('gongji: %d,muji: %d,xiaoji: %d' % (x, y, z))
