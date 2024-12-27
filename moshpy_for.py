'''6 for loops'''
#6.1 basic 
my_list = [1,2,3,4,5,6,7]
for num in my_list:
	print(num)

#6.2 enumerate()获取索引和值
my_list = ['apple','banana','orange']
for index, fruit in enumerate(my_list):
 print(f"索引：{index},'水果':{fruit}'")

#6.3 dinctionary
my_dict = {'name':'alex','age':30}
for key in my_dict: #key == 'name/age' key可以认为是键位或索引
	print(key)
for value in my_dict.values(): # my_dict.values() 用来提取字典里面的值
	print(value)
for key, value in my_dict.items(): #这里使用f-strings格式打印键位和索引
	print(f"key：{key}, value: {value}")

#6.4 math even or odd 
for num in range(10):
	if num % 2 == 0:
		continue #这里筛选出偶数直接跳过，最后打印出来的会是奇数
	print(num)	

for num in range(11):
	if num% 2 == 1:
		print(num)

#6.5 嵌套 用于二维数组和矩阵运算
for i in range(3):
	for j in range(3):
		print(f"({i} , {j})")

#6.6.1 for in list in row
number = [] #建立空列表
for number in range(10):
	print(number) 

#6.6.2 for in list in [] 
number = [x*2 for x in range(5)]
print(number) #1~4的2x

number = [x**3 for x in range(1,10)]
print(number) #1~9的立方

