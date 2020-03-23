import sys

#打开并读取文件里的字符串
res = ""
with open(sys.argv[1]) as fd:
    for line in fd:
        print(line)
        for i in line:
            if i.isdigit():
                res += i
print(res)
