#需求：8个老师随机分派在3个教室
'''
1.准备数据
    1.1  8位老师
    1.2  3个教室
2.分派老师到教室
3.验证分配结果
'''
import random
teachers = ['A','B','C','D','E','F','G','H']
offices = [[],[],[]]

for name in teachers:
    num = random.randint(0, 2)
    offices[num].append(name)
i = 1

for office in offices:
    print(f'办公室{i}中的人数是{len(office)},教室里分派的老师分别是：')
    for name in office:
        print(name)
    i += 1