__author__ = 'jhuan'

import sys
import random
import xlwt3
import matplotlib.pyplot as plt

#-----初始化脚本中部分变量-----
a1 = a2 = a3 = a4 = a5 = a6 = 0
b1 = b2 = b3 = b4 = b5 = b6 = 0
c1 = c2 = c3 = c4 = c5 = c6 = 0
Lsum = []
Csum = []

l = []                                #原始组合列表
for i in range(1,7):
    for j in range(1,7):
        for k in range(1,7):
            s=sorted(str(i)+str(j)+str(k))
            s=int(''.join(s))
            l.append(s)
    count=len(set(l))                   #去重以后组合的总数
    l=list(sorted(set(l)))              #去重以后的结果

#----取值进行计算----
x = sys.argv[1]
while not x.isdigit() or x == '':
    x = input('请输入取值次数：')
x = int(x)

#-------------K3玩法产生3位1~6数字从小到大依次排列的组合，并得到和值，差值。--------------
#取x次开奖周期的模拟结果
lm=[]  #定义一个空列表用于接收生成的结果
for j in range(x):
    for item in range(1, 79):  # 每个周期内开奖78次
        c = [1, 2, 3]
        result = ''
        Asum = 0  # 初始化和值为0
        for i in c:
            a = random.randint(1, 6)  # 模拟产生3个数字
            Asum += a
            result += str(a)
        content = sorted(result), '和值为', Asum, '差值为', int(sorted(result)[2]) - int(sorted(result)[0])
        if (content[0][0]) == '1':  # 下面是分别判断每次开奖结果的第一位第二位和第三位数字为多少从而得到出现的频率。
            a1 += 1
        if (content[0][0]) == '2':
            a2 += 1
        if (content[0][0]) == '3':
            a3 += 1
        if (content[0][0]) == '4':
            a4 += 1
        if (content[0][0]) == '5':
            a5 += 1
        if (content[0][0]) == '6':
            a6 += 1
        if (content[0][1]) == '1':
            b1 += 1
        if (content[0][1]) == '2':
            b2 += 1
        if (content[0][1]) == '3':
            b3 += 1
        if (content[0][1]) == '4':
            b4 += 1
        if (content[0][1]) == '5':
            b5 += 1
        if (content[0][1]) == '6':
            b6 += 1
        if (content[0][2]) == '1':
            c1 += 1
        if (content[0][2]) == '2':
            c2 += 1
        if (content[0][2]) == '3':
            c3 += 1
        if (content[0][2]) == '4':
            c4 += 1
        if (content[0][2]) == '5':
            c5 += 1
        if (content[0][2]) == '6':
            c6 += 1
        Lsum.append(Asum)  # 生成一个和值结果的列表
        Csum.append(int(sorted(result)[2]) - int(sorted(result)[0]))  # 生成一个差值结果的列表
        lm.append(int(''.join(sorted(result))))

#--------打开一个用于保存统计结果的文档--------
f = open('analysis.txt', 'w', encoding='utf-8')
for i in l:
    count=lm.count(i)
    add = str(list(str(i))) + '出现' + str(count) + '次！'
    f.write(add)
    f.write('\n')
f.close()

#----生成开奖结果3个数字中每一位出现各个数字的总频率列表----
No1 = [a1, a2, a3, a4, a5, a6]
No2 = [b1, b2, b3, b4, b5, b6]
No3 = [c1, c2, c3, c4, c5, c6]

#----------将结果写入excel----------
excel = xlwt3.Workbook()
sheet = excel.add_sheet('sheet1', True)
for shuzi in range(1, 7):
    sheet.write(0, shuzi, shuzi)
for weishu in range(1, 4):
    sheet.write(weishu, 0, 'Num'+str(weishu))
for r1 in range(len(No1)):
    sheet.write(1, r1+1, No1[r1])
for r2 in range(len(No2)):
    sheet.write(2, r2+1, No2[r2])
for r3 in range(len(No3)):
    sheet.write(3, r3+1, No3[r3])
excel.save('analysis.xls')


#------生成一个图表包含频率的柱形图，差值和和值的曲线图。------
plt.xlabel('Number')
plt.ylabel('Frequency')
plt.title('Data analysis')
f1 = plt.figure(1)
p1 = plt.subplot(221)
p2 = plt.subplot(222)
p3 = plt.subplot(212)
a = 0.7
for i in range(len(No1)):  # 生成频率的柱形图
    plt1 = p3.bar(left=a, height=No1[i], width=0.2, yerr=0.0001, color='Red')
    a += 0.2
    plt2 = p3.bar(left=a, height=No2[i], width=0.2, yerr=0.0001, color='Yellow')
    a += 0.2
    plt3 = p3.bar(left=a, height=No3[i], width=0.2, yerr=0.0001, color='blue')
    a += 0.6
p3.legend((plt1, plt2, plt3), ('1stNum', '2ndNum', '3rdNum'), loc=9, shadow=True, fontsize='small')
#生成和值和差值的曲线图
p1.plot(range(1, 78*x + 1), Lsum, 'o', color='Red')
p2.plot(range(1, 78*x + 1), Csum, color='Blue')
p1.legend('Lsum', fontsize='xx-small')
p2.legend('Csum', fontsize='xx-small')
plt.show()  #显示图表