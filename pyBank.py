import os
import csv

date =[]
revenue=[]
header=[]  
# Read data_1 file and convert two columns into two lists without the header
with open('budget_data_1.csv', encoding="ascii", errors="surrogateescape") as csvfile:
						csv_reader = csv.reader(csvfile)
						header=next(csv_reader)
						for row in csv_reader:
							date.append(row[0])
							revenue.append(row[1])
# Create a new object by zipping the two lists.
new1_csv=zip(date,revenue)


date =[]
revenue=[]
# Read data_2 file and convert two columns into two lists including the header
with open('budget_data_2.csv', encoding="ascii", errors="surrogateescape") as csvfile:
						csv_reader = csv.reader(csvfile)
						
						for row in csv_reader:

							date.append(row[0])
							revenue.append(row[1])
# Create a second object by zipping the above two lists.
new2_csv=zip(date,revenue)
#Open a new file and write the above two objects into the new file.
with open("revenue_final.csv", 'w', newline="") as new_file:
		csv_writer = csv.writer(new_file)
		
		#csv_writer=csv.writer(header)		
		csv_writer.writerows(new2_csv)
				#csv_writer.writerows(row)
		csv_writer.writerows(new1_csv)


#Open and read the new file for further calculations
with open("revenue_final.csv", encoding="ascii", errors="surrogateescape") as csvfile:
		csv_reader = csv.reader(csvfile)
		#Skip the header to do the calculations starting from the second row
		next(csv_reader)
	#Open three empty lists to be filled by data from the newly created CSV file.	
		date = []
		revenue = []
		rev_change = []

		for row in csv_reader:
			date.append(row[0])
			revenue.append(float(row[1]))
		print("Financial Analysis")
		print("----------------------------------")
		print("Total Months: ", len(date))
		print("Total Revenue: $", round(sum(revenue)))
		# Loop from the second row(first row after header) to the last one to do the required calculations
		for i in range(1, len(revenue)):
			rev_change.append(revenue[i] - revenue[i-1])
			avg_rev_change = sum(rev_change)/len(rev_change)
			max_rev_change = round(max(rev_change))
			min_rev_change = round(min(rev_change))
			max_rev_change_date = date[rev_change.index(max_rev_change)]
			min_rev_change_date = date[rev_change.index(min_rev_change)]

		print("Average Revenue Change: $", round(avg_rev_change))
		print("Greatest Increase in Revenue: ", str(max_rev_change_date), " ($"+ str(max_rev_change)+ ")")
		print("Greatest Decrease in Revenue: ", str(min_rev_change_date), " ($"+ str(min_rev_change)+ ")")
		







