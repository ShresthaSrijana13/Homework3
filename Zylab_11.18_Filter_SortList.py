# Srijana Shrestha
# 1918305
num1 = input()
num2 = num1.split()
list1 = []

for i in num2:
    if int(i) >= 0:
        list1.append(int(i))

list1.sort()
for i in list1:
    print(i, end=' ')
