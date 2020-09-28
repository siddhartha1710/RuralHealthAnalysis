import matplotlib.pyplot as plt
import csv

x = []
y1 = []
y2 = []
y3 = []
y4 = []
y5 = []
label=[]


with open('C:\\Users\\Siddhartha\\PyCharmProjects\\RuralHealthAnalysis\\DataFiles\\Health Centers\\Meghalaya.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        label.append(row[2])
        x.append(str(row[2]))
        y1.append(int(row[3]))
        y2.append(int(row[4]))
        y3.append(int(row[5]))
        y4.append(int(row[6]))
        y5.append(int(row[7]))
plt.plot(x, y1, 'o')
plt.plot(x, y2, 'o')
plt.plot(x, y3, 'o')
plt.plot(x, y4, 'o')
plt.plot(x, y5, 'o')

plt.xticks(x, label, rotation='vertical')

plt.plot(x,y1, label='No. of Sub Center')
plt.plot(x,y2, label='No. of PHC')
plt.plot(x,y3, label='No. of CHC')

plt.plot(x,y4, label='No. of Sub Divisional Hospital')
plt.plot(x,y5, label='No. of District Hospital')

plt.xlabel('Meghalaya')
plt.ylabel('Number')


plt.title('Meghalaya (Health Centers)')
plt.legend()
plt.show()