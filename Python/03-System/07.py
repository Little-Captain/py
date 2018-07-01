#!/usr/bin/env python

# 进程池 Pool

# 当需要创建的子进程数量不多时，可以直接利用 multiprocessing 中的 Process 动态成生多个进程，
# 如果是上百甚至上千个目标，手动的去创建进程的工作量巨大，就可以用到 multiprocessing 模块
# 提供的 Pool 方法

# 初始化Pool时，可以指定一个最大进程数，当有新的请求提交到Pool中时，如果池还没有满，那么就会
# 创建一个新的进程用来执行该请求；但如果池中的进程数已经达到指定的最大值，那么该请求就会等待，
# 直到池中有进程结束，才会创建新的进程来执行

from multiprocessing import Pool
import os, time, random

def worker(msg):
    t_start = time.time()
    print("%s开始执行,进程号为%d"%(msg, os.getpid()))
    time.sleep(random.random()*2)
    t_stop = time.time()
    print(msg, "执行完毕, 耗时%0.2f"%(t_stop-t_start))

po = Pool(3)
for i in range(0, 10):
    po.apply_async(worker, (i,))

print("---start---")
po.close()
po.join()
print("---end---")

# multiprocessing.Pool常用函数解析
# 1. apply_async(func[, args[, kwds]]) ：使用非阻塞方式调用func
# （并行执行，堵塞方式必须等待上一个进程退出才能执行下一个进程），
# args为传递给func的参数列表，kwds为传递给func的关键字参数列表
# 2. apply(func[, args[, kwds]])：使用阻塞方式调用func
# 3. close()：关闭Pool，使其不再接受新的任务
# 4. terminate()：不管任务是否完成，立即终止
# 5. join()：主进程阻塞，等待子进程的退出， 必须在close或terminate之后使用

# apply堵塞式
po = Pool(3)
for i in range(0, 10):
    po.apply(worker, (i,))

print('---start---')
po.close()
po.join()
print('---end---')
