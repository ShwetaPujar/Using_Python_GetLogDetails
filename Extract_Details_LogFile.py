import itertools
import operator
from collections import Counter

class Test_LogFile():
    d = {}
    list_url = []
    list_codes = []
    list_pages_unscuccess = []
    list_ip = []
    key = 0


    def __init__(self):
        print("Reading the data from the LogFile")

#Setup - Read the LogFile.txt and extract the data and store in the respective lists
    def setup(self):
        i = 0
        file1 = open("LogFile.txt", "r")
        with open("LogFile.txt") as f:
            for line in f:
                #split to get only the needed information from the line in the LogFile.txt
                self.d[i] = line.split()
                #print("Extracting the data from the LogFile")
                #print(self.d[i][0], self.d[i][6],self.d[i][8])
                self.list_url.append(self.d[i][6])
                self.list_codes.append(self.d[i][8])
                if (self.d[i][8] == '404'):
                    self.list_pages_unscuccess.append(self.d[i][6])
                self.list_ip.append(self.d[i][0])
                i = i + 1
        f.close()


    def getDuplicatesWithCount(listOfElems):
        ''' Get frequency count of duplicate elements in the given list '''
        dictOfElems = dict()
        # Iterate over each element in list
        for elem in listOfElems:
            # If element exists in dict then increment its value else add it in dict
            if elem in dictOfElems:
                dictOfElems[elem] += 1
            else:
                dictOfElems[elem] = 1
        dictOfElems = {key: value for key, value in dictOfElems.items() if value > 1}
        return dictOfElems

#Get the Total URL count
    def getURLCount(self):
        N=10
        flag=0
        dictOfElems = self.getDuplicatesWithCount(self.list_url)
        #for key, value in dictOfElems.items():
            #print(key , ' :: ', value)
        for key, value in dictOfElems.items():
                if(value >flag):
                    flag=value
        for key,value in dictOfElems.items():
            if value==flag:
                print ("###############################################")
                print("URL with maximum number of hits")
                print(key,value)
        #print("Sorted list of urls")
        #print (sorted(dictOfElems.items(),key=operator.itemgetter(1),reverse=True))
        #Sorting the list to get the descending order to get the top10 URL
        sorted_dict=sorted(dictOfElems.items(),key=operator.itemgetter(1),reverse=True)
        print ("Top 10 requested URL's")
        out=dict(itertools.islice(sorted_dict,N))
        print(out)

    def success_unsuccess_request(self):
        count = 0
        bad_req = 0
        #print("List is", list_codes)
        print("Total URL Requests =",len(self.list_codes))
        for j in range(len(self.list_codes)):
            if (self.list_codes[j] == '200' and '303'):
                count = count + 1
            if (self.list_codes[j] == '404'):
                bad_req = bad_req + 1

        print("404 Bad requests =", bad_req)
        print("Successfull Request 200 and 300 =", count)
        percentage = (count / len(self.list_codes)) * 100
        percentage_badreq = (bad_req / len(self.list_codes)) * 100
        print("Percentage of the successfull requests =", percentage)
        print("percentage of unsuccessfull requests =", percentage_badreq)

    def top10_unsucess_req(self):
        N=10
        #print("Url having unsuccessfull status codes",list_pages_unsuccess)
        list_counter=self.get_counter(self.list_pages_unscuccess)
        print("Top 10 unsucessfull pages")
        page_10=self.top_10(list_counter)
        print(page_10)

    def get_counter(list_withoutcount):
        list_with_count =[]
        list_with_count = (Counter(list_withoutcount))
        print("Count",list_with_count)
        list_with_count=sorted(list_with_count, key=list_with_count.get, reverse=True)
        return(list_with_count)


    def ip_most_requests(self):
        #print("List of ip address",list_ip)
        list_counter=self.get_counter(self.list_ip)
        #print("Top ip address making maximum requests", list_counter)
        ip_10=self.top_10(list_counter)
        print("Top 10 ip address making maximum requets")
        print(ip_10)

    def top_10(my_list):
        top10=list(itertools.islice(my_list,10))
        return(top10)




