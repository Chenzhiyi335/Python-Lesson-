#访问字典里的值
dict = {'Name':'陈二萌','age':18,'birthday':950801}
print("dict['Name']",dict['Name'])
print("dict['birthday]",dict['birthday'])

#修改字典
dict = {'Name':'陈二萌','age':18,'birthday':950823}
dict['age']=23
dict['address'] = "guangzhou"
print(dict)

#删除字典元素
dict = {'Name':'陈二萌','age':18,'birthday':950801}
del dict['Name']
print(dict)