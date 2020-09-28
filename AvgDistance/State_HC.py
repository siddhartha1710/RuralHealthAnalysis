import matplotlib.pyplot as plt
import csv

x = []
y1 = []
y2 = []
y3 = []

label=[]

with open('C:\\Users\\Siddhartha\\PyCharmProjects\\RuralHealthAnalysis\\DataFiles\\Files\\Statewise HC_new.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        label.append(row[1])
        x.append(str(row[1]))
        y1.append(float(row[2]))
        y2.append(float(row[3]))
        y3.append(float(row[4]))

plt.plot(x, y1, 'o')
plt.plot(x, y2, 'o')
plt.plot(x, y3, 'o')

plt.xticks(x, label, rotation='vertical')
plt.plot(x,y1, label='Sub Centre')
plt.plot(x,y2, label='PHC')
plt.plot(x,y3, label='CHC')
plt.xlabel('States of India')
plt.ylabel('Number')


plt.title('India')
plt.legend()
plt.show()