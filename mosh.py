'''1 comments : Mosh cheat sheet 井号键可用于留言标注用途'''

'''2 Variables   integer/float/string/boolean/list/dictionary'''
#2.1 Strings 
#2.1.1 ' ' or " " or ''' '''(a multi-line string)
print('Python3')
print("Python3")
print('''
Python3
is
a
program lauguage
	''')

#2.1.2 strings[:] 切片
strings = "Python is easy."
print(strings[0]) # the first one is [0]
print(strings[1])
print(strings[2])
print(strings[1:-1])
print(strings[1:6])
print(strings[-2])
print(strings[1:]) # n: = the n-st to the end
print(strings[:-1]) # :-n the beginning to the -n

#切片的运用
print('CSS' + strings[6:])


#2.1.3 format() or f-strings for string formatting

#format basic
name = "alex"
age = 30
height = 180
selfintro = "My name is {} and I am {} years old. I am {} cm tall.".format(name,age,height)
print(selfintro) 

#pro 
print("{name} is {age} years old. {height}".format(name='Alex',age=30,height=180))
#you can set the value in one line

print("{1} and {0}".format("apple", "orange"))  
# Output: orange and apple
# Number 0 and 1 is the order of format

#plus
number = 3.141
print("The pi is {:2f}".format(number))
#{2:2f}是一个整体
#{}是插入值 ：表达格式 .2这里确认保留小数点2位 f-float

#f-strings basic
name = "Alice"
age = 30
greeting = f"Hello, my name is {name} and I am {age} years old."
print(greeting)  # Output: Hello, my name is Alice and I am 30 years old.

#math
x = 10
y = 5
result = f"The sum of {x} and {y} is {x + y}"
print(result)  # Output: The sum of 10 and 5 is 15

#format plus
number = 3.14159
print(f"The value is {number:.2f}")  # Output: The value is 3.14

#2.1.4 格式
name = "alex cage"
print(name.upper())
print(name.lower())
print(name.title())
print(name.find("e"))
print(name.find('y'))
print(name.replace('a','t')) #这里可以和切片的用法互换
print("\nToday is a nice day.") #n = enter
print("\tToday is a nice day.") #t = tab

#2.1.5 检查字符是否在定量中 boolean
name1 = 'nealanan'
'neal' in name1 #return True/False

#2.2 int/float/arithmetic
6 / 2 == 3.0 # / return a float
6 // 2 == 3 # // return a int
6 % 2 == 0
6 % 4 == 2 #余数 remainder of division
6**2 == 36
#python2中 == 是boolean指令
x = x + 10 
x += 10 #这是上面的简写

#2.2 comparison operators
a = 1
b = 2
a > b
a >= b
a < b
a<= b
a == b #equals
a != b #not equals

#2.3 Lists

#2.3.1 list and index
num = [1,2,3,"four","five"]
print(num[0]) # a list starts with [0]
print(num[1]) # return the second
print(num[-1])
print(num[-2])
#切片
print(num[1:4])
print(num[0:])
print(num[:-1])

#insert and del ，sort sorted reverse ::-1
num = [1,2,3,4,5,6]
num[0] = 0 #直接通过命令修改值
num.append(5) #add 5 to the end
num.insert(0,6) add 6 at the index position of 0

num.remove(6)
del num[1]
num.pop() #remove the last index
number.clear #remove all the index

num1 = [1,2,1,3,4,5,4,6]

num1.sort() #sort the list
num2 = num1.sorted() #这里创建了一个新的正序列表，但没有改变原来的值
num2 = sorted(num1, reverse = True) #sorted可作为函数，进行倒序排列

num1.reverse() #reverse the list
num2 = num1[::-1] #这里创建了一个新的反转列表，但没有改变原来的值 

num2 =num1.copy() #这里复制了num1的值并赋予num2，此时两个列表虽然值一样，但并不是同一个list


#2.3.2 list and math

#2.3.2.1 列表推导式 list comprehension
# 普通方式生成平方列表
squares = []
for x in range(10):
    squares.append(x**2)

# 列表推导式
squares = [x**2 for x in range(10)]

#2.3.2.2 生成器表达式 Generator Expression 
squares = (x**2 for x in range(10))

#2.3.2.3 list 解包
x,y,z = 1,2,3
x,y,z = [1,2,3] #这两个返回的结果是一样的

#2.3.3 list增量
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1 += list2
print(list1)

#2.3.4 metrik
matrix = [
[1,2,3]
[4,5,5]
[7,8,9]
]

#1 访问单个元素
# 访问第一行第二列的元素
element = matrix[0][1]  # 结果是 2

#2 访问一行
# 访问第二行
row = matrix[1]  # 结果是 [4, 5, 5]

#3 访问一列
# 访问第一列 (需要列表推导式或循环)
column = [row[0] for row in matrix]  # 结果是 [1, 4, 7]

#4 切片
# 获取前两行
submatrix = matrix[:2]  # 结果是 [[1, 2, 3], [4, 5, 5]]

#5.1 math sq
sq = [num**2 for row in matrix for num in row]

#5.2 提取元素
greater_than_5 = [num for row in matrix for num in row if num >5]

#5.3 numpy
import numpy as np
np_matrix = np.array(matrix)

#5.4 pandas
import pandas as pd
df = pd.DataFrame(matrix)

#5.6 提取所有元素的平均值
def calculate_average(matrix):
    """计算矩阵中所有元素的平均值"""
    total = sum(num for row in matrix for num in row)
    count = len(matrix) * len(matrix[0])
    return total / count

average = calculate_average(matrix)
print(average)

