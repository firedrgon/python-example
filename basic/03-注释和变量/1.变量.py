'''
变量定义:
变量存储在内存中的值，这就意味着在创建变量时会在内存中开辟一个空间。 基于变量的数据类型，解释器会分配指定内存，并决定什么数据可以被存储在内存中。 因此，变量可以指定不同的数据类型，这些变量可以存储整数，小数或字符。 变量赋值
Python 中的变量赋值不需要类型声明。 每个变量在内存中创建，都包括变量的标识，名称和数据这些信息。 每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。 等号 = 用来给变量赋值。
等号 = 运算符左边是一个变量名，等号 = 运算符右边是存储在变量中的值.
'''
name = "成龙"
print(name)

age = 18
print(age)

num = 4.34
print(num)

# python中可以一次性给多个变量赋值
x = y = z = 12
print(x,y,z)
a,b = 23,4.32
print(a,b)