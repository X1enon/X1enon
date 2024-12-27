'''4 if statements and comparison '''
#if/elif/elif/else for muiltiple conditions

#4.1 if can be nested(基本上函数语法都可以嵌套)
a = 80
if a >= 60:
	if a >= 90:
		print('a > 90')
	elif a>= 80:
		print('a = 80')
	else:
		print('invalid')
else:
	pirnt('not a')

#4.2 Syntax: value_if_ture if condition else value_if_false
is_raining = True
message = "Take an umbrella" if is_raining else "Enjoy the sunshine!"
print(message)
#这里先确定boolean后一行内完成if else

#4.3 Chained compaisons \ in or not in \  and or \ boolean
age = 30
if 20 <= age <= 35:
    print("You are in your prime.")

loop = ['a' , 'b' , 'c']
if 'a' in loop:
	print('a in the loop.')
if 'd' not in loop:
	print('d not in the loop.')
if 'b' in loop is False: #有时候可以直接在if上完成boolean然后写if True/False
	print('b in the loop')

