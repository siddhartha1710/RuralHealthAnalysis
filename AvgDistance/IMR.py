import matplotlib.pyplot as plt
import csv

x = []
y1 = []
y2 = []
y3 = []
y4 = []

label=[]

with open('C:\\Users\\Siddhartha\\PyCharmProjects\\RuralHealthAnalysis\\DataFiles\\Analysis\\New\\Infant Mortality Rate new.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        label.append(row[1])
        x.append(str(row[1]))
        y1.append(float(row[2]))
        y2.append(float(row[3]))
        y3.append(float(row[4]))
        y4.append(float(row[5]))

plt.plot(x, y1, 'o')
plt.plot(x, y2, 'o')
plt.plot(x, y3, 'o')
plt.plot(x, y4, 'o')


plt.xticks(x, label, rotation='vertical')
plt.plot(x,y1, label='IMR Total')
plt.plot(x,y2, label='IMR Rural')
plt.plot(x,y3, label='IMR Urban')
plt.plot(x,y4, label='IMR Urban - Rural')

plt.xlabel('States of India')
plt.ylabel('Number')


plt.title('Infant Mortality Rate')
plt.legend()
plt.show()