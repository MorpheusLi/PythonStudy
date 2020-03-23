name = input("Enter the file name:")
fp = open(name)
print(fp.read())
fp.close()
