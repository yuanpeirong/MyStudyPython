#学习使用for语句
sum=0
for x in range(1,101,1):
    sum=sum+x*((-1)**(x-1))
print(sum)
