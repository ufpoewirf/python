#提示用户输入用户姓名，并保存到变量当中
name = input("请输入用户姓名：")
#提示用户输入用户年龄，并保存到变量当中，并切换成整数
age = int(input("请输入用户年龄："))
#提示用户输入用户年身高，并保存到变量当中，并切换成浮点数
height = float(input("请输入身高："))
#在控制台输出用户姓名、年龄、身高对应变量的数据类型
print(type(name),type(age),type(height))
#按照以下格式输出用户信息：“姓名：xxx年龄：xxx 身高：xxx"
print(f"姓名：{name} 年龄：{age} 身高：{height}")
#在控制台输出该用户5年之后的年龄，格式：”张三 5 年之后的是 25
age =age + 5
print(f"{name}5 年之后的身高是{age+5}")
#在控制台输出该用户现在是否成年，格式：“张三是否成年：True"
print(f"{name}是否成年：{age>=18}")
#提示在用户台输入一个天数，然后把天数折算为秒数，并且在控制台输出。要求输出格式为：xx天等于多少秒
day = int(input("请输入一个天数："))
second = day*24*3600
print(f"{day}天等于多少{second}秒")
#Ctrl d 快速复制黏贴一行 shift enter 快速新建一行 Ctrl Alt l 格式化
