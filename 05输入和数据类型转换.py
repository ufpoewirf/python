# 需求 从键盘输入你的姓名
age = input("请输入你的年龄：")
print(type(age),age)   #打印类型和变量的值
new_age = int(age)#需求 将字符串的18转换为int类型的18
print(type(age),age)#<class 'str'> 18数据类型转换不会改变age的类型，生成一个新的数据保存到new_age
print(type(new_age),new_age)#<class 'int'> 18
#我的名字是xx，年龄xx岁，性别为xx.
name = "小明"
sex = "男"
age = 18
print("我的名字是' + name + ',年龄 ’ + str(age) + '岁，性别为‘ + sex +’.")
print("我的名字是{},年龄 {}岁，性别为{}.". format(name,age,sex )) #格式化输出
#练习题目
#提示用户输入两个数字 input-->str
numbers1 = int(input('请输入数字1：'))
numbers2 = int(input('请输入数字2：'))
#使用获取的数据进行加法运算
numbers = numbers1 + numbers2
#在控制台输出计算结果，格式要求：xx+xx=xx
print(f"{numbers1} + {numbers2} = {numbers}")
#转义字符 \n 换行 \t 制表符，tab健
print("hello world",end=' ')
print("hello\nworld")
print("hellopythpn")
print("hello\tpython")