'''5 while loops通常用于无限循环，在用户输入、文字获取文字获取方面、数学计算'''

#5.1 如果条件为True时会形成无限循环，需要通过if 和 break 停止循环

while True:
	user_input = input("请输入内容（输入‘leave’即可退出）： ")
	if uer_input.lower() == 'leave':
		print('您已退出。')
		break
	print(f'您刚才输入了：{uer_input}.')

#5.2 循环可以与迭代器和生成器配合使用
my_list = [1, 2, 3, 4, 5]
iterator = iter(my_list)

while True:
    try:
        item = next(iterator)
        print(item)
    except StopIteration:
        break

