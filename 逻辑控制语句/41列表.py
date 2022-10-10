#使用类实例化的方式，定义空列表 变量=list（）
list1=list()
print(type(list1),list1)
#定义非空列表
list1=list('abcde')
print(list1)
#定义空列表
list3=[]
print(list3)
list4=[1,3.14,'he',False]
print(list4)
#列表支持下标和切片，获取列表第一个数据；获取列表最后一个数据；获取中间两个数据
print(list4[0])
print(list4[-1])
print(list4[1:3])
#列表查找方法 查找3.14下面出现的下标
numbers=list4.index(3.14)
print(numbers)
#统计数据1出现的次数 统计数据20出现的次数
numbers1=list4.count(1)
print(numbers1)
numbers2=list4.count(20)
print(numbers2)
#列表的添加和删除方法 添加李四，王五，赵6;删除最后一个数据，删除第二个数据
list4.append('李四')
list4.append('王五')
list4.append('赵6')
print(list4)
list4.pop()
print(list4)
name=list4.pop(1)
print('删除的数据为：', name)
print(list4)
#列表的修改
my_list=[1,2]
my_list[0]=200
print(my_list)
my_list[1]=100
print(my_list)
#列表的反转1.切片
list5=list4[::-1]
print(list4)
print(list5)
#2.reverse
list4.reverse()
print(list4)




#列表的排序，列表的数据要一样
your_list1=[3,9,0,6]
your_list1.sort()#排序 升序
print(your_list1)
your_list1.sort(reverse=True)#降序
print(your_list1)
