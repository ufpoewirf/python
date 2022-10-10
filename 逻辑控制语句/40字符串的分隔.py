str1='hello l love\t itcast and\nloveyou'
#默认 按照空白字符分隔 split 字符串拆分 默认空白字符\n \t 空格
list1=str1.split()
print(list1)
#按照空格分隔
list2=str1.split(' ')
print(list2)
#按照and分隔
list3=str1.split('and')
print(list3)
#字符串连接（join） 容器一般是列表，列表中的数据只能是字符串
list5=['hello','l love','itcast','and','loveyou']
#使用，隔开
str5=','.join(list5)
print(str5)