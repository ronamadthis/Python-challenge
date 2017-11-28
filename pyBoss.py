import os
import csv

us_state_abbrev = {

    'Alabama': 'AL',

    'Alaska': 'AK',

    'Arizona': 'AZ',

    'Arkansas': 'AR',

    'California': 'CA',

    'Colorado': 'CO',

    'Connecticut': 'CT',

    'Delaware': 'DE',

    'Florida': 'FL',

    'Georgia': 'GA',

    'Hawaii': 'HI',

    'Idaho': 'ID',

    'Illinois': 'IL',

    'Indiana': 'IN',

    'Iowa': 'IA',

    'Kansas': 'KS',

    'Kentucky': 'KY',

    'Louisiana': 'LA',

    'Maine': 'ME',

    'Maryland': 'MD',

    'Massachusetts': 'MA',

    'Michigan': 'MI',

    'Minnesota': 'MN',

    'Mississippi': 'MS',

    'Missouri': 'MO',

    'Montana': 'MT',

    'Nebraska': 'NE',

    'Nevada': 'NV',

    'New Hampshire': 'NH',

    'New Jersey': 'NJ',

    'New Mexico': 'NM',

    'New York': 'NY',

    'North Carolina': 'NC',

    'North Dakota': 'ND',

    'Ohio': 'OH',

    'Oklahoma': 'OK',

    'Oregon': 'OR',

    'Pennsylvania': 'PA',

    'Rhode Island': 'RI',

    'South Carolina': 'SC',

    'South Dakota': 'SD',

    'Tennessee': 'TN',

    'Texas': 'TX',

    'Utah': 'UT',

    'Vermont': 'VT',

    'Virginia': 'VA',

    'Washington': 'WA',

    'West Virginia': 'WV',

    'Wisconsin': 'WI',

    'Wyoming': 'WY',

}


EmpID =[]
Name=[]
DOB=[]
SSN=[]
State=[]
header=["EmpID","Name","DOB","SSN","State"]
# Read data_1 file and convert two columns into two lists without the header
with open('employee_data1.csv', encoding="ascii", errors="surrogateescape") as csvfile:
						csv_reader = csv.reader(csvfile)
						next(csv_reader)
						for row in csv_reader:
							EmpID.append(row[0])
							Name.append(row[1])
							DOB.append(row[2])
							SSN.append(row[3])
							State.append(row[4])
# Create a new object by zipping the two lists.
new1_csv=zip(EmpID,Name,DOB,SSN,State)


EmpID =[]
Name=[]
DOB=[]
SSN=[]
State=[]
# Read data_2 file and convert two columns into two lists including the header
with open('employee_data2.csv', encoding="ascii", errors="surrogateescape") as csvfile:
						csv_reader = csv.reader(csvfile)
						next(csv_reader)
						for row in csv_reader:

							EmpID.append(row[0])
							Name.append(row[1])
							DOB.append(row[2])
							SSN.append(row[3])
							State.append(row[4])
# Create a second object by zipping the above two lists.
new2_csv=zip(EmpID,Name,DOB,SSN,State)
#Open a new file and write the above two objects into the new file.
with open("Employee_final.csv", 'w', newline="") as new_file:
		csv_writer = csv.writer(new_file)

		csv_writer.writerow(header)
		#csv_writer=csv.writer(header)		
		csv_writer.writerows(new2_csv)
				#csv_writer.writerows(row)
		csv_writer.writerows(new1_csv)


#Open and read the new file for further calculations
with open("employee_final.csv", encoding="ascii", errors="surrogateescape") as csvfile:
		csv_reader = csv.reader(csvfile)
		#Skip the header to do the calculations starting from the second row
		next(csv_reader)
	#Open six empty lists to be filled by data from the newly created CSV file.	
		EmpID =[]
		Firstname=[]
		LastName=[]
		DOB=[]
		SSN=[]
		State=[]

		for row in csv_reader:
			EmpID.append(row[0])
			NewName =row[1].split(" ")
			Firstname.append(NewName[0])
			LastName.append(NewName[1])
			NewDOB=row[2].split("-")
			DOB.append(NewDOB[1]+"/"+NewDOB[2]+"/"+NewDOB[0])
			NewSSN=row[3].split("-")
			SSN.append("***-**-"+NewSSN[2])
			State.append(us_state_abbrev[row[4]])


# Zip lists together
cleaned_csv = zip(EmpID, Firstname, LastName, DOB,SSN,State)
# Set variable for output file
output_file = os.path.join("boss_final.csv")

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["EmpID","First Name","Last Name","DOB","SSN","State"])

    # Write in zipped rows
    writer.writerows(cleaned_csv)
			
		