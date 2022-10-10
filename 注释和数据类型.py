# Python是解释型语言，在执行的时候需要解释器（翻译）一边执行，从上到下去执行，下方代码出现错误不会影响上方代码执行
# get from version control 从版本控制中恢复一个版本 configure 配置设置
print('hello world')
# 控制台输出，验证结果是否正确
"""ctrl+/ 单行注释 三对单引号是多行注释，可以换行不用执行
"""
'''
三对单引号组成的注释
'''
"""indent 代码的缩进问题 红色波浪线 标记的bug，必须要修改
 灰色波浪线是代码规范性问题，不影响代码执行print(BLOCK comment should start with'#')
注释应该以＃号空格开始 no newwline at end of file 没有新行在文件末尾 使用代码格式化解决 ctrl alt L（code--reformat code）
绿色波浪线：不影响代码执行 pycharm 认为你写的不是一个单词
"""
# 变量
name ="小明"
age=18
sex='女'
height='170.1'
# 使用变量，打印小明 is not defined 没有定义
print(name)
print(age,sex,height)
"""Python中的关键字 false 假 none 空 true 真 and 与 as 起别名使用 assert 断言使用 break 打乱 class 定义类使用 continue
继续在循环里面使用 def 定义 del 删除 elif 如果 else 否则 except 除了 for 循环使用 global 全局的 import打包 lambda 表达式
nonlocal非本地 pass占位 ralse抛出异常 return返回 while循环 yieid 生成器
"""
# 驼峰命名法：大驼峰 Myname 小驼峰 myName 下划线命名：my-name
"""数据类型--数字型--整型（整数，int）；浮点型（小数，float）；布尔型（bool,true or false）
非数字型--字符串（使用引号引起来的就是字符串）；列表（list[1，2，3]；元组（tuple(1,2,3)集合（set{1,2,3};字典（dict{"name"：
"小明"，”age“：18}
"""



