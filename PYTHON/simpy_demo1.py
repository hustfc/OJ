import simpy

#定义一个汽车进程
def car(env):
    while True:
        print('Start parking at %d' % env.now)
        parking_duration = 5
        yield env.timeout(parking_duration)
        print('Start driving at %d' % env.now)
        trip_duration = 2
        yield env.timeout(trip_duration)
#仿真启动
env = simpy.Environment() #实例化环境
env.process(car(env)) #添加汽车进程
env.run(until=15)  #设定仿真结束条件，这里是15秒之后停止