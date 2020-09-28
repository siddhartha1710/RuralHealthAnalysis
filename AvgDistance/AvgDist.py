import matplotlib.pyplot as plt
import csv

x = []
y1 = []
y2 = []
y3 = []
y4 = []
y5 = []
y6 = []
label=[]

with open('C:\\Users\\Siddhartha\\PyCharmProjects\\RuralHealthAnalysis\\DataFiles\\Files\\Avg Dist_new.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        label.append(row[1])
        x.append(str(row[1]))
        y1.append(float(row[2]))
        y2.append(float(row[3]))
        y3.append(float(row[4]))
        y4.append(float(row[5]))
        y5.append(float(row[6]))
        y6.append(float(row[7]))
plt.plot(x, y1, 'o')
plt.plot(x, y2, 'o')
plt.plot(x, y3, 'o')
plt.plot(x, y4, 'o')
plt.plot(x, y5, 'o')
plt.plot(x, y6, 'o')

plt.xticks(x, label, rotation='vertical')
plt.plot(x,y1, label='Average Rural Area (Sq. Km.) - covered by a Sub Centre')
plt.plot(x,y2, label='Average Rural Area (Sq. Km.) - covered by a PHC')
plt.plot(x,y3, label='Average Rural Area (Sq. Km.) - covered by a CHC')
plt.plot(x,y4, label='Average Radial Distance (Kms) - covered by a Sub Centre')
plt.plot(x,y5, label='Average Radial Distance (Kms) - covered by a PHC')
plt.plot(x,y6, label='Average Radial Distance (Kms) - covered by a CHC')
plt.xlabel('States of India')
plt.ylabel('Number')


plt.title('Average Distance')
plt.legend()
plt.show()