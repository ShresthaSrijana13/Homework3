# Srijana Shrestha
# 1918305

num1 = input()  # user input
num2 = num1.split()  # converting num1 into list
list1 = []  # assigning empty list

for i in num2:  # for loop
    if int(i) >= 0:  # if condition to check whether the value is greater or qual to zero
        list1.append(int(i))  # adding the value into list

list1.sort()  # sorting the list1
for i in list1:  # for loop iterate in list1
    print(i, end=' ')  # printing the value with space
