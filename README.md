# Using_Python_GetLogDetails
Problem Description : Given a Log File , Get the Following details from Log file, 
1. Top 10 requested pages and the number of requests made for each.
2. Percentage of successful requests and unsuccessfull requests 
3. Top 10 unsuccessful page requests ,
4. The top 10 hosts making the most requests, displaying the IP address and number of requests made.

Approach : 
1. Read the logfile 
2. Extract the necessary fields using split to the dictionary
3. Appending the data as required by test to the respective list 

Assumptions
1.Since the given html file was large in size , i have copied the data to the .txt and then i have refered it from there
2.Alernative solution would be to convert the html file to the text file , which is currently not part of this code but can be implemented .
3. I have taken 2 days data to generate the output , but again this can scaled to big files as well .

Further enhancements.
1. Appending to the csv file the result file .

How to Run the file 
1. Open terminal
2. Navigate to the project folder
3. python3 Main_Runner_file.py
4. User is propmpted with the inputs , select anyone and then exit 
