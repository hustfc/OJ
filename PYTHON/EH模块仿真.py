import simpy
Kd = 10 #10对D2D设备
time_downlink = 10 #下行链路传输时间
time_dedicated = 10 #蜂窝用户专属传输时间
time_D2D = 1 #D2D传输时间
a = [0] * (Kd + 2)
a[0] = time_downlink
for i in range(1, Kd + 1):
    a[i] = time_D2D
a[Kd + 1] = time_dedicated

def EH(env):
    while True:
       print('%7.4f : BS开始给CU传输信息，同时DU收集能量' % env.now)
       yield env.timeout(a[0])
       print('%7.4f : 下行链路结束，同时D2D开始通信' % env.now)
       for i in range(1, Kd + 1):
           print('%7.4f : D2D%02d开始通信' % (env.now, i))
           yield env.timeout(a[i])
           print('%7.4f : D2D%02d结束通信' % (env.now, i))
       print('%7.4f : DUS结束通信关闭，CUS单独通信' % env.now)
       yield env.timeout(a[0])
       print('%7.4f : 上行链路结束，CUS关闭通信' % env.now)

#仿真启动
env = simpy.Environment() #实例化环境
env.process(EH(env)) #添加汽车进程
env.run(until=100)  #设定仿真结束条件，这里是100秒之后停止

