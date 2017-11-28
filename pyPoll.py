import os
import csv

voterID =[]
candidate=[]
header=[]
# Read data_1 file and convert two columns into two lists including the header
with open('election_data_1.csv', encoding="ascii", errors="surrogateescape") as csvfile:
						csv_reader = csv.reader(csvfile)
						
						for row in csv_reader:
							voterID.append(row[0])
							candidate.append(row[2])
# Create a new object by zipping the two lists.
new1_csv=zip(voterID,candidate)


voterID =[]
candidate=[]

# Read data_2 file and convert two columns into two lists without the header
with open('election_data_2.csv', encoding="ascii", errors="surrogateescape") as csvfile:
						csv_reader = csv.reader(csvfile)
						next(csv_reader)
						for row in csv_reader:

							voterID.append(row[0])
							candidate.append(row[2])
# Create a second object by zipping the above two lists.
new2_csv=zip(voterID,candidate)
#Open a new file and write the above two objects into the new file.
with open("poll_final.csv", 'w', newline="") as new_file:
		csv_writer = csv.writer(new_file)
		
		#csv_writer=csv.writer(header)		
		csv_writer.writerows(new1_csv)
		#csv_writer.writerows(row)
		csv_writer.writerows(new2_csv)


#Open and read the new file for further calculations
with open("poll_final.csv", encoding="ascii", errors="surrogateescape") as csvfile:
		csv_reader = csv.reader(csvfile)
		#Skip the header to do the calculations starting from the second row
		next(csv_reader)
		
		#Determine the total number of votes cast by counting the total number of voter IDs
		##Calculate the number of votes for each candidate by making a dictionary with candidates as keys
		#and voterID as values

		voterID=[]
		aDict={}
		
		for row in csv_reader:
			voterID.append(row[0]) 

			k=row[1]
			v=row[0]
			if not k in aDict:
				aDict[k]=[v]
			else:
				aDict[k].append(v)
			
		Totalvotes=len(voterID)
		
						
		print("Election Results")
		print("---------------------------")
		print("Total Votes: "+ str(Totalvotes))
		print("---------------------------")

		
		for k,v in aDict.items():
							
			print (k,": ",str(round(len(v)*100/Totalvotes,1)),"%  ("+ str(len(v))+ ")")

			#Determine the winner who received max votes
			def mostVotes(d):

				max_count = max(len(v)for v in d.values())
				winner = [k for k,v in d.items() if len(v)==max_count]
				return winner
			



		print("---------------------------")
		print("Winner:", " ".join(mostVotes(aDict)))
		print("---------------------------")
						









