import matplotlib.pyplot as plt
import csv

x = []
y1 = []

label=[]


with open('C:\\Users\\Siddhartha\\PyCharmProjects\\RuralHealthAnalysis\\DataFiles\\Analysis\\New\\Population CHC 2011 new.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        label.append(row[1])
        x.append(str(row[1]))
        y1.append(float(row[6]))

plt.plot(x, y1, 'o')


plt.xticks(x, label, rotation='vertical')

plt.bar(x,y1,color="red", label='Number of people per CHC')

plt.xlabel('States')
plt.ylabel('Number')


plt.title('Number of people per CHC')
plt.legend()
plt.show()