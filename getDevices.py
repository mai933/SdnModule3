"""
Script that logs into Cisco DNA Center always on sandbox
and retrieves a list of network devices

"""

#import requests library and basic HTTP auth to pass a username and password

import requests
import getpass
from pprint import pprint
from requests.auth import HTTPBasicAuth

#Defines global variables we don't want chnged

USER = input("Please Enter Your Username: ")
password = getpass.getpass()
print(username)
URL = "https://sandboxdnac.cisco.com/api/system/v1/auth/token"


#Create dictionary for the resposne payload, headers, in this we are doing an http post
#so we need to specify the content type we are sending rather than accepting a format

headers = {'Content-Type': 'application/json'}

#creates a response variable with the value of our post request notice this is a post not a get
#which is different than what we have been doing so far we are sending the server something not
#asking for it.  Also note we are passing a username and password and lastly as you will notice
#in the next lab we have set verify to false this is because DNA Center is using a self signed
#certificate and we are aware so we want to accept the risk and continue
#THIS SHOULD NOT BE DONE IN A PRODUCTION ENVIRONMENT IT IS A SECURITY ISSUE!!!!

response = requests.post(URL, auth=HTTPBasicAuth(USER, PASS), headers=headers, verify=False)

#converts our respone to json format and stores it in our variable resposneJSON

token = response.json()['Token']

#prints responseJSON variable



#Creates a variable URL2 and assigns the value of the follow up API request
#to DNA Center to retrieve a list of network devices

URL2 = "https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device"

#Creates dictionary for follow up get request headers specifying the format as JSON and
#passing the value for the token from the variable above.

getHeader = {'Accept': 'application/json', 'X-auth-token': token}

#Creates object getResponse with the contents of our http get request to the URL2 variable
#passing our getHeader dictionary and not verifying the cert validity since it is self signed 

getResponse = requests.get(URL2, headers=getHeader, verify=False)

#Takes our response variable and converts it to JSON format storing it in devicesJSON



#prints devicesJSON to the screen

devices = getResponse.json()['response']
for device in devices:
    name = device['hostname']
    mgmtIP = device['managementIpAddress']
    print("The Device Named: " + str(name) + " is at IP " + str(mgmtIP))
  


