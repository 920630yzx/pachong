# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 15:07:22 2018

@author: 肖
"""

'''1.生成器表达式:类似于列表推导,但是,生成器返回按需产生结果的一个对象,
而不是一次构建一个结果列表  优点:节约内存。'''
gen = (x *x for x in range(3)) 
gen  
next(gen)
next(gen)
next(gen)

'''2.生成器函数：常规函数定义，但是，使用yield语句而不是return语句返回结果。
yield一次返回一个结果，在每个结果中间，挂起函数的状态，以便下次从它离开的地方继续执行。'''
def gen():
	print('first')
	yield 1
	print('second')
	yield 2
	print('three')
	yield 3
	print('end')
g = gen()
g
next(g)
next(g)
next(g)
next(g)

'''3.对于生成器，每次执行next()方法后，代码会执行到yield关键字处，并将yield后的参数值返回，
同时当前生成器函数的上下文会被保留下来。也就是函数内所有变量的状态会被保留，
同时函数代码执行到的位置会被保留，感觉就像函数被暂停了一样。当再一次调用next()方法时，
代码会从yield关键字的下一行开始执行。很神奇吧！如果执行next()时没有遇到yield关键字即退出（或返回），
则抛出StopIteration异常。有没有觉得每次都得调用next()方法太麻烦？for循环可以自动实现next()方法，运行生成器。'''
# 斐波那契数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1    

for n in fib(10):
	print(n)

'''4.使用生成器，函数不用一次性生成所有的元素，只需在每次调用next的时候生成元素，
这样更节省内存和CPU。注:yield与return的比较：
相同：都有返回值的功能。
不同：return只能返回一次值，而yield可以返回多次值。
'''

# 另一个案例
def yield_test(n):  
    for i in range(n):  
        yield call(i)  
        print("i=",i)  
    # 做一些其它的事情      
    print("do something.")      
    print("end.")  

def call(i):  
    return i*200  

# 使用for循环  
for i in yield_test(5):  
    print(i,",!!!")

yield_test(5)



