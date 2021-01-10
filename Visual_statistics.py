
from pathlib import Path
from collections import defaultdict
import matplotlib.pyplot as plt
list = []
count = 0
result = open('Statistics_result.txt', 'w')
language_list = ["python", "c++", "C", "java", "objective-c",
                 "php", "basic", "ruby"]
for i in range(len(language_list)):
    temp = [0, 0, 0, 0]
    path = language_list[i]+".txt"
    result.write(language_list[i]+" statistics:")
    #print(language_list[i]+" statistics:"+"\n")
    with open(path, encoding='utf-8')as f:
        for line in f:
            temp_list = eval(line)
            view = int(temp_list[3])
            if view > 10000:
                temp[0] += 1
            elif view > 1000:
                temp[1] += 1
            elif view > 100:
                temp[2] += 1
            else:
                temp[3] += 1
    result.write(str(temp)+" view\n")
    plt.plot([4, 3, 2, 1], temp, linewidth=1.0)
    for j in range(1, 5):
        plt.annotate(r'$%s$' % language_list[i], xy=(j, temp[4-j]), xycoords='data', xytext=(+10, +0),
                     textcoords='offset points', fontsize=10, arrowprops=dict(arrowstyle='->', connectionstyle='arc3, rad = .2'))
plt.xlabel("Views level")
plt.ylabel("number of article")
plt.title("Diffrent languages' articles view level")
plt.text(1, 300, "Level1:view<100\nLevel2:100<view<1000\nLevel3:1000<view<10000\nLevel4:view>10000")
plt.show()

for i in range(len(language_list)):
    temp = [0, 0, 0, 0]
    path = language_list[i]+".txt"
    result.write(language_list[i]+" statistics:")
    #print(language_list[i]+" statistics:"+"\n")
    with open(path, encoding='utf-8')as f:
        for line in f:
            temp_list = eval(line)
            like = float(temp_list[5])
            if like > 100:
                temp[0] += 1
            elif like > 50:
                temp[1] += 1
            elif like > 10:
                temp[2] += 1
            else:
                temp[3] += 1
    result.write(str(temp)+" like\n")
    plt.plot([4, 3, 2, 1], temp, linewidth=1.0)
    for j in range(1, 5):
        plt.annotate(r'$%s$' % language_list[i], xy=(j, temp[4-j]), xycoords='data', xytext=(+10, +0),
                     textcoords='offset points', fontsize=10, arrowprops=dict(arrowstyle='->', connectionstyle='arc3, rad = .2'))
plt.xlabel("Likes level")
plt.ylabel("number of article")
plt.title("Diffrent languages' articles like level")
plt.text(3, 300, "Level1:like<10\nLevel2:10<like<50\nLevel3:50<like<100\nLevel4:like>100")
plt.show()

for i in range(len(language_list)):
    temp = [0, 0, 0, 0]
    path = language_list[i]+".txt"
    result.write(language_list[i]+" statistics:")
    #print(language_list[i]+" statistics:"+"\n")
    with open(path, encoding='utf-8')as f:
        for line in f:
            temp_list = eval(line)
            comment = float(temp_list[4])
            if comment > 100:
                temp[0] += 1
            elif comment > 50:
                temp[1] += 1
            elif comment > 10:
                temp[2] += 1
            else:
                temp[3] += 1
    result.write(str(temp)+" comment\n")
    plt.plot([4, 3, 2, 1], temp, linewidth=1.0)
    for j in range(1, 5):
        plt.annotate(r'$%s$' % language_list[i], xy=(j, temp[4-j]), xycoords='data', xytext=(+10, +0),
                     textcoords='offset points', fontsize=10, arrowprops=dict(arrowstyle='->', connectionstyle='arc3, rad = .2'))
plt.xlabel("comments level")
plt.ylabel("number of article")
plt.title("Diffrent languages' articles comment level")
plt.text(3, 300, "Level1:comment<10\nLevel2:10<comment<50\nLevel3:50<comment<100\nLevel4:comment>100")
plt.show()
