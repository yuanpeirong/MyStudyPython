#求和 1-2+3-4+……+99-100
sum=0
a=1
b=2
while a<=99: #当a小于等于99时，执行缩进的程序段
    sum=sum+a-b
    a=a+2
    b=b+2
print(sum)