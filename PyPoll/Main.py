import os
import csv



csv_filepath = os.path.join('Resources', 'election_data.csv')

candidate=[]
winner=''
vote=0
value=0



with open(csv_filepath, 'r') as f:
    
    csv_reader = csv.reader(f, delimiter= ',')
    next(csv_reader, None)

    for row in csv_reader:
        candidate.append(row[2])

    total=len(candidate)
    count=value.count(candidate)
    
    for key, value in count.items():
        if value >vote:
            winner=key
            vote = value

    print("")
    print("Election Results")
    print("...............................")
    print("Total Votes:" +str(total))
    print("--------------------------------")
    for key, value in count.items():
        print(key + ":" + str("{0:.lf}".format(value/total*100)) + "% (" +str(value) +")")
        print("----------------------------------------")
        print("winner: " + winner)
        print("-------------------")
with open('Report_' + csv_filepath.split('.')[0] + '.txt', 'w', newline='') as textfile:

    textfile.write("Election Results" +"\n")
    textfile.write("..............................." +"\n")
    textfile.write("Total Votes:" +str(total))
    textfile.write("--------------------------------" +"\n")
    for key, value in count.items():
        textfile.write(key + ":" + str("{0:.lf}".format(value/total*100)) + "% (" +str(value) +")" +"\n")
        textfile.write("----------------------------------------" +"\n")
        textfile.write("winner: " + winner +"\n")
        textfile.write("-------------------" +"\n")