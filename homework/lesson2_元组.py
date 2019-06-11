#元组
student = (1001,'xiaoming',20)
print(student)

#可以不带小括号
student = 1001,'xiaoming',20
print(student)

#创建单个元素的元组
t = (50,)
print(t)

#元组也支持索引和切片操作
a = ('a','b',1,2,3)
print(a[0])
print(a[2:4])

#元组拼接
tup1 = (1,2,3)
tup2 = (4,5,6)
tup3 = (tup1+tup2)
print(tup3)

#遍历元组
for i in tup3:
    print(i)
