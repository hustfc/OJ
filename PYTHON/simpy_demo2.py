from random import seed, randint
seed(23)
import simpy

class EV:
    def __init__(self, env):
        self.env = env
        self.drive_proc = env.process(self.drive(env))  #驾驶进程，来调用drive函数
        self.bat_ctrl_proc = env.process(self.bat_ctrl(env))  #充电进程，来调用bat_ctrl函数
        self.bat_ctrl_reactive = env.event() #充电开始事件，事件可以用来激活
        self.bat_ctrl_sleep = env.event()   #充电结束事件
    def drive(self, env):
        #驾驶进程
        while True:
            print('开始驾驶时间: ', env.now)
            yield env.timeout(randint(20, 40))
            print('驾驶停止时间: ', env.now)

            #停车1-6小时
            print('开始停车时间: ', env.now)
            self.bat_ctrl_reactive.succeed() #激活充电事件
            self.bat_ctrl_reactive = env.event()
            yield env.timeout(randint(60, 360)) and self.bat_ctrl_sleep #停车时间和充电程序关闭都满足
            print('结束停车时间：', env.now)

    def bat_ctrl(self, env):
        #充电进程
        while True:
            print('充电程序休眠时间：', env.now)
            yield self.bat_ctrl_reactive #休眠直到充电事件被激活
            print('充电程序激活时间：', env.now)
            yield env.timeout(randint(30, 90))
            print('充电程序结束时间：', env.now)
            self.bat_ctrl_sleep.succeed()
            self.bat_ctrl_sleep = env.event()
env = simpy.Environment()
EV(env)
env.run(until=300)