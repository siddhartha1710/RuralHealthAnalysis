import matplotlib.pyplot as plt
import csv

x = []
y1 = []
y2 = []
y3 = []

label=[]

with open('C:\\Users\\Siddhartha\\PyCharmProjects\\RuralHealthAnalysis\\DataFiles\\Analysis\\New\\Final Analysis new.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        label.append(row[1])
        x.append(str(row[1]))
        y1.append(float(row[14]))


plt.plot(x, y1,'o')


plt.xticks(x, label, rotation='vertical')
plt.bar(x,y1,color="green", label='Final Score')
plt.xlabel('States of India')
plt.ylabel('Number')


plt.title('India')
plt.legend()
plt.show()