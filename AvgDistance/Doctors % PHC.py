import matplotlib.pyplot as plt
import csv

x = []
y1 = []
y2 = []
y3 = []
y4 = []
y5 = []

label=[]

with open('C:\\Users\\Siddhartha\\PyCharmProjects\\RuralHealthAnalysis\\DataFiles\\Analysis\\New\\Doctors PHC new.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        label.append(row[1])
        x.append(str(row[1]))
        y1.append(float(row[11]))
        y2.append(float(row[12]))
        y3.append(float(row[13]))
        y4.append(float(row[14]))
        y5.append(float(row[15]))

plt.plot(x, y1, 'o')
plt.plot(x, y2, 'o')
plt.plot(x, y3, 'o')
plt.plot(x, y4, 'o')
plt.plot(x, y5, 'o')


plt.xticks(x, label, rotation='vertical')
plt.plot(x,y1, label='% of PHC with 4+ Doctors')
plt.plot(x,y2, label='% of PHC with 3 Doctors')
plt.plot(x,y3, label='% of PHC with 2 Doctors')
plt.plot(x,y4, label='% of PHC with 1 Doctors')
plt.plot(x,y5, label='% of PHC with 0 Doctors')

plt.xlabel('States of India')
plt.ylabel('Number')


plt.title('% of Doctors in PHC')
plt.legend()
plt.show()