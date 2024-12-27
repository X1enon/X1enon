#Dictionaries
#1 make a dict
mydict = {
'name':'alex',
'age':30,
'city':'nyc',}
print(mydict)

#2 访问
name = mydict['name']
print(name)

#3 修改
mydict['country'] = 'USA'
mydict['age'] = 18


#4 字典推导
squares = {x: x**2 for x in range(10)} #这里和list用法相似
print(squares) #但是结果里有索引和相应的值

#6 字典索引
age = mydict.get('age') 
age = mydict.get('gendar','Unknown') #因为列表里没有性别索引，所以这里给予一个默认值用来反映

#7 添加键值对
gendar = mydict.setdefault('gendar','female') #sedefault.()用于创建新的值对

#8 返回所有值对,这里区别于直接打印字典格式的value，items可以提取并返回所有的值
for key, value in mydict.items():
	print(f"{key},{value}")

#9 返回所有键 或 值
key1 = mydict.keys()
key1 = mydict.values()

#10 删除并返回所对应的值
age = mydict.pop('age')
print(age)
print(mydict)

item = mydict.popitem() #随机删除
print(item)
print(mydict)

#11 多个字典更新
my_dict = {'name': 'Alice', 'age': 30}
new_info = {'city': 'Beijing', 'country': 'China'}
my_dict.update(new_info)
print(my_dict)  # 输出：{'name': 'Alice', 'age': 30, 'city': 'Beijing', 'country': 'China'}

#12 清空字典
mydict.clear()

#del用来删除字典里特殊的字符，如果删除所有字符会占用更多内存
my_dict = {'name': 'Alice', 'age': 30} 
for key in list(my_dict.keys()):
    del my_dict[key]
print(my_dict)  # 输出：{} (空字典)
