import os
import csv


folderName='Resources'
filenames=os.listdir(folderName)
for filename in filenames:

    
    csvpath=os.path.join(folderName, filename)

date= []
ProfitLosses=0
changesum=0
net_total=[]
change=[0]
great_increase=0
great_decrease=0


with open(csvpath, newline='') as csvfile:
    
    csv_reader = csv.reader(csvfile, delimiter=',')
    for row in csv_reader:
        next(csv_reader, None)
        date.append(row[0])
        net_total.append(row[1])

for i in range(0, len(net_total)-1):
        change.append((net_total[i+1]) - int(net_total[i]))
for j in range (0, len(change)):
        
        if change [j] > great_increase:
            great_increase = change[j]
            
            
            if change[j] < great_decrease:
                great_decrease = change[j]
                
                changesum=changesum+abs(change[j])
                total=total+int(net_total[j])
                average=int(changesum/(len(change)-1))
                
                print("")
                print("Finacial Analysis")
                print("---------------------------------")
                print("Total Months: " +str(len(date)))
                print("Average Changes: $" + str(average))
                print("Great Increase: " + date[change.index(great_increase)]+"($" + str(great_increase)+")")
                print("Great Decrease: " + date[change.index(great_decrease)]+"($" + str(great_decrease)+")")
       
        with open('Report_' + csv.split('.')[0] + '.txt', 'w', newline='') as textfile:
            textfile.write( print("Finacial Analysis" +"\n"))
            textfile.write("---------------------------------")
            textfile.write("Total Months: " +str(len(date)) + "\n")
            textfile.write("Average Changes: $" + str(average) + "\n")
            textfile.write("Great Increase: " + date[change.index(great_increase)]+"($" + str(great_increase)+")" +"\n")
            textfile.write("Great Decrease: " + date[change.index(great_decrease)]+"($" + str(great_decrease)+")")

