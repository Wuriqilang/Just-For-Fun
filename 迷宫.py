#一行代码打印迷宫
print(''.join(__import__('random').choice('\u2571\u2572') for i in range(50*24)))
#或者
#print(''.join(__import__('random').choice('/\\') for i in range(50*24)))