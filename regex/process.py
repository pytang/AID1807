import multiprocessing as mp
from time import sleep

def fun():
    sleep(3)
    print("子进程事件")

#创建进程对象
p = mp.Process(target=fun)

# 启动进程
p.start()

sleep(2)
print("这是父进程")

# 回收进程
p.join()
