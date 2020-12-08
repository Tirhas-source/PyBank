import os
import csv

csvpath =  os.path.join('budget_data.csv')
csvoutput = 'Pybank_output.txt'

total_months = []
pL = []
pL_change = []
 

    # Skip the header labels to iterate with the values
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile)        
    csv_header = next(csvreader)  
    #print(csv_header)    

    # Iterate the rows and add total months and profit loss to the lists
    for row in csvreader: 
        #total_months = total_months + 1
        total_months.append(row[0])
        pL.append(int(row[1]))

    # Iterate find  change in profit loss
    for i in range(len(pL)-1):
        
        # find difference between two months
        pL_change.append(pL[i+1]-pL[i])
        
# profit loss change 
greatest_increase = max(pL_change)
greatest_decrease = min(pL_change)

# match month to profit loss change 
max_month = pL_change.index(max(pL_change)) + 1
min_month = pL_change.index(min(pL_change)) + 1 

# Print

print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(len(total_months)))
print("Total: " + str(sum(pL)))
print("Average Change: " + str(round(sum(pL_change)/len(pL_change),2)))
print("Greatest Increase in Profits: " + total_months[max_month] + " (" + (str(greatest_increase)) + ")")
print("Greatest Decrease in Profits: " + total_months[min_month] + " (" + (str(greatest_decrease))+ ")")

#output 

with open (csvoutput, "w") as txt:
    txt.write("Financial Analysis")
    txt.write("\n")
    txt.write("----------------------------")
    txt.write("\n")
    txt.write("Total Months: " + str(len(total_months)))
    txt.write("\n")
    txt.write("Total: " + str(sum(pL)))
    txt.write("\n")
    txt.write("Average Change: " + str(round(sum(pL_change)/len(pL_change),2)))
    txt.write("\n")
    txt.write("Greatest Increase in Profits: " + total_months[max_month] + " (" + (str(greatest_increase)) + ")")
    txt.write("\n")
    txt.write("Greatest Decrease in Profits: " + total_months[min_month] + " (" + (str(greatest_decrease))+ ")")
    
