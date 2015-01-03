__author__ = 'Administrator'


import random
import xlwt3
import matplotlib.pyplot as plt

a1 = a2 = a3 = a4 = a5 = a6 = a7 = a8 = a9 = a0 = 0
b1 = b2 = b3 = b4 = b5 = b6 = b7 = b8 = b9 = b0 = 0
c1 = c2 = c3 = c4 = c5 = c6 = c7 = c8 = c9 = c0 = 0
Lsum = []
Csum = []
index = 0
f = open('analysis.txt', 'w', encoding='utf-8')
for j in range(1):
    for item in range(1, 101):
        l = [1, 2, 3]
        result = ''
        Asum = 0
        for i in l:
            a = random.randint(0, 9)
            Asum += a
            result += str(a)
        index +=1
        content = result, '和值为', Asum, '差值为', int(sorted(result)[2]) - int(sorted(result)[0])

        if (content[0][0]) == '1':
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
        if (content[0][0]) == '7':
            a7 += 1
        if (content[0][0]) == '8':
            a8 += 1
        if (content[0][0]) == '9':
            a9 += 1
        if (content[0][0]) == '0':
            a0 += 1
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
        if (content[0][1]) == '7':
            b7 += 1
        if (content[0][1]) == '8':
            b8 += 1
        if (content[0][1]) == '9':
            b9 += 1
        if (content[0][1]) == '0':
            b0 += 1
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
        if (content[0][2]) == '7':
            c7 += 1
        if (content[0][2]) == '8':
            c8 += 1
        if (content[0][2]) == '9':
            c9 += 1
        if (content[0][2]) == '0':
            c0 += 1
        Lsum.append(Asum)
        Csum.append(int(sorted(result)[2]) - int(sorted(result)[0]))
        add = str(index) + ': ' + str(list(result))
        f.write(add)
        f.write('\n')
f.close()

No1 = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a0]
No2 = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b0]
No3 = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c0]

excel = xlwt3.Workbook()
sheet = excel.add_sheet('sheet1', True)
for shuzi in range(1, 11):
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


plt.xlabel('Number')
plt.ylabel('Frequency')
plt.title('Data analysis')
f1 = plt.figure(1)
p1 = plt.subplot(221)
p2 = plt.subplot(222)
p3 = plt.subplot(212)
a = 0.7
for i in range(len(No1)):
    plt1 = p3.bar(left=a, height=No1[i], width=0.2, yerr=0.0001, color='Red')
    a += 0.2
    plt2 = p3.bar(left=a, height=No2[i], width=0.2, yerr=0.0001, color='Yellow')
    a += 0.2
    plt3 = p3.bar(left=a, height=No3[i], width=0.2, yerr=0.0001, color='blue')
    a += 0.6
p3.legend((plt1, plt2, plt3), ('FstNum', 'SecNum', 'ThdNum'), loc=9, shadow=True, fontsize='small')
p1.plot(range(1, 101), Lsum, color='Red',)
p2.plot(range(1, 101), Csum, color='Blue')
p1.legend('Lsum', fontsize='xx-small')
p2.legend('Csum', fontsize='xx-small')
plt.show()