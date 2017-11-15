1.
#while 循环语句
    count = 0
while (count < 9):
    print("The count is :", format(count))
    count = count + 1
print("Good Bye!")


2.
# continue 和 break 用法
i = 0
while i < 10:
    i = i + 1
    if (i % 2 == 0):
        continue
    print("this is :", format(i))

i=0
while i<10:
    i=i+1
    if(i%2==0):
        break
    print("this is :",format(i))





