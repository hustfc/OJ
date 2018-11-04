from random import seed, randint
seed(23)
import simpy

class EV:
    def __init__(self, env):
        self.env = env
        self.com_proc_proc = env.process(self.communicate(env))  #通信进程，来调用communicate函数
        self.power_ctrl_proc = env.process(self.power_ctrl(env))  #能量收集进程，来调用power_ctrl函数
        self.power_ctrl_reactive = env.event() #创建能量收集开始事件，事件可以用来激活
        self.power_ctrl_sleep = env.event()   #创建能量收集结束事件

    def communicate(self, env):
        #通信进程
        while True:
            print('%7.4f 开始通信时间: ' % env.now)
            print('通信中...........')
            yield env.timeout(randint(20, 40))
            print('%7.4f 通信停止时间: ' % env.now)

            #收集能量
            print('%7.4f 开始收集能量时间: ' % env.now)
            self.power_ctrl_reactive.succeed() #激活通信事件
            self.power_ctrl_reactive = env.event()
            yield env.timeout(randint(60, 360)) and self.power_ctrl_sleep #能量收集时间和能量收集装置关闭都满足
            print('%7.4f 能量收集完成并且装置关闭时间：' % env.now)

    def power_ctrl(self, env):
        #能量收集进程
        while True:
            #print('能量收集休眠时间：', env.now)
            yield self.power_ctrl_reactive #休眠直到充电事件被激活
            print('%7.4f 能量收集激活时间：' % env.now)
            print('收集能量中...........')
            yield env.timeout(randint(30, 90))
            print('%7.4f 能量收集结束时间：' % env.now)
            self.power_ctrl_sleep.succeed()  #激活收集能量装置关闭
            self.power_ctrl_sleep = env.event()
env = simpy.Environment()
EV(env)
env.run(until=300)