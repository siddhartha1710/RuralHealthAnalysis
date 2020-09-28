import matplotlib.pyplot as plt
import csv

x = []
y1 = []
y2 = []
y3 = []


label=[]

with open('C:\\Users\\Siddhartha\\PyCharmProjects\\RuralHealthAnalysis\\DataFiles\\Analysis\\New\\Doctors PHC new.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        label.append(row[1])
        x.append(str(row[1]))
        y1.append(float(row[16]))
        y2.append(float(row[17]))
        y3.append(float(row[18]))


plt.plot(x, y1, 'o')
plt.plot(x, y2, 'o')
plt.plot(x, y3, 'o')


plt.xticks(x, label, rotation='vertical')
plt.plot(x,y1, label='% of PHC without Lab Tech')
plt.plot(x,y2, label='% of PHC without Pharma')
plt.plot(x,y3, label='% of PHC with Lady Doctor')

plt.xlabel('States of India')
plt.ylabel('Number')


plt.title('% of Doctors in PHC')
plt.legend()
plt.show()