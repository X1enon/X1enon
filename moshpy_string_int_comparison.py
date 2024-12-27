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



