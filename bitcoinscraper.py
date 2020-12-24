import requests
import webbrowser
import sys
import urllib
from bs4 import BeautifulSoup
from csv import writer

response = requests.get('https://keys.lol/bitcoin/1')
soup = BeautifulSoup(response.text,'html.parser')
table = soup.find({"class":"flex flex-col bg-grey-lightest min-h-screen"})


#table = soup.find({"class":"container mx-auto px-2 flex-1"})
#table = soup.find({"class":"sm:flex justify-center"})
print table
##rows = table.find_all('mr-4 inline-block')

#rows.pop(0)
#for row in rows:
    ##print transaction
    
    
