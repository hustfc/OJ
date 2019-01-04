n, m = map(int, input().split())
machineTime, machineClass = [0] * n, [0] * n
taskTime, taskClass = [0] * m, [0] * m
for i in range(n):
    machineTime[i], machineClass[i] = map(int ,input().split())
for i in range(m):
    taskTime[i], taskClass[i] = map(int, input().split())
totalEarn = 0
for i in range(n):
    earn = 0
    for j in range(m):
        if taskTime[j] < machineTime[i] and taskClass[j] < machineClass[j]:
            earn = 200 *