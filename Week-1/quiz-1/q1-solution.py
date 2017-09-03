"""
Question:
Pick one IP from each region, find network latency from via the below code snippet
(ping 3 times), and finally sort the average latency by region.
http://ec2-reachability.amazonaws.com/
Expected Output for all 15 regions:
1. us-west-1 [50.18.56.1] - 100ms (Smallest average latency)
2. xx-xxxx-x [xx.xx.xx.xx] - 200ms
3. xx-xxxx-x [xx.xx.xx.xx] - 300ms
...
15. xx-xxxx-x [xx.xx.xx.xx] - 1000ms (Largest average latency)
"""

from __future__ import print_function
import subprocess   #this library is for creating a process to perform the operation
import re           #this library is used for regex mathcing string patterns
import numpy as np  #this is to convert to float data type
from operator import itemgetter  #this library is for sorting the outer list using an index in the inner list

hosts = [["us-east-1","23.23.255.255"],["us-east-2","13.58.0.253"],
         ["us-west-1","13.56.63.251"],["us-west-2","34.208.63.251"],
         ["us-gov-west-1","52.61.0.254"],["ca-central-1","35.182.0.251"],
         ["eu-west-1","34.240.0.253"],["eu-central-1","18.194.0.252"],
         ["eu-west-2","35.176.0.252"],["ap-northeast-1","13.112.63.251"],
         ["ap-northeast-2","13.124.63.251"],["ap-southeast-1","13.228.0.251"],
         ["ap-southeast-2","13.54.63.252"],["ap-south-1","13.126.0.252"],
         ["sa-east-1","18.231.0.252"]]

length = len(hosts)

for region in range(0,length):
    ping = subprocess.Popen(
        ["ping", "-c", "3", hosts[region][1]], #pinging each host mentioned in the hosts list
        stdout = subprocess.PIPE, #creating a pipe
        stderr = subprocess.PIPE
    )

    out, error = ping.communicate()
    timeArray = re.findall('time=\d+.\d+',str(out)) #Extracting the time using regex
    time = re.findall('\d+.\d+', str(timeArray)) #Extracting the value from the time
    floatTime = np.round([float(i) for i in time], 3) #Converting the string list to a float list with 3 decimal places
    average =  sum(floatTime)/len(floatTime) #Finding the average of the list
    average = np.round(average,3) #rounding into 3 decimal places
    hosts[region].append(average) #appending average values into each item in the list

hosts = sorted(hosts,key=lambda x: x[2]) #sorting the list using the average values as an index

#Printing out the list
for region in range(0,length):
        if(region==0):
            print(str(region+1)+'.',str(hosts[region][0]),'['+str(hosts[region][1])+']'+' - '+str(hosts[region][2])+'ms'+' (Smallest average latency)')
        if(region==length-1):
            print(str(region+1)+'.',str(hosts[region][0]),'['+str(hosts[region][1])+']'+' - '+str(hosts[region][2])+'ms'+' (Largest average latency)')    
        if((region !=0) and (region !=length-1)):
            print(str(region+1)+'.',str(hosts[region][0]),'['+str(hosts[region][1])+']'+' - '+str(hosts[region][2])+'ms')


