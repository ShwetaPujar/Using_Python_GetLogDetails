import Assignment.Extract_Details_LogFile

obj = Assignment.Extract_Details_LogFile.Test_LogFile
obj.setup(self=Assignment.Extract_Details_LogFile.Test_LogFile)

#Get the User requirement to generate the output
print("Please select the following")
print("1:Top 10 requested pages and the number of requests made for each")
print("2:Percentage of successful requests (200 and 300) and Unsuccessfull request 404")
print("3:Top 10 unsuccessful page requests")
print("4:The top 10 hosts making the most requests, displaying the IP address and number of requests made.")
n=input("Please Enter any valid number from the list\n")

#Based on the selection invoke the methods
if (n=='1'):
    #Assignment.Url_Count.getURLCount()
    obj.getURLCount(self=Assignment.Extract_Details_LogFile.Test_LogFile)
elif(n=='2'):
    #Assignment.Url_Count.success_unsuccess_request(list_codes)
    obj.success_unsuccess_request(self=Assignment.Extract_Details_LogFile.Test_LogFile)
elif(n=='3'):
    #Assignment.Url_Count.top10_unsucess_req(list_pages_unscuccess)
    obj.top10_unsucess_req(self=Assignment.Extract_Details_LogFile.Test_LogFile)
elif(n=='4'):
    #Assignment.Url_Count.ip_most_requests(list_ip)
    obj.ip_most_requests(self=Assignment.Extract_Details_LogFile.Test_LogFile)
else:
    print("Wrong input")


