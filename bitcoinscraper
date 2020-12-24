import requests
import webbrowser
import sys
import urllib
from bs4 import BeautifulSoup
from csv import writer

response = requests.get('https://finance.yahoo.com/quote/%5EDJI/history/')
soup = BeautifulSoup(response.text,'html.parser')

table = soup.find(attrs= {"data-test":"historical-prices"})
rows = table.find_all('tr')
#print rows[1].find('td').find('span').get_text()
#Popping the headers of the table
rows.pop(0)
for row in rows:
    date = row.find('td').find('span').get_text()
    openPrice = row.find_all('td')[1].find('span').get_text()
    closePrice = row.find_all('td')[4].find('span').get_text()
    if(date == 'Sep 03, 2020'):
        break
    searchURL = 'https://google.com/search?q='+''.join('what caused the dow to move on ')+''.join(date)
    searchURL = searchURL.replace(" ","'%20")
    #print (searchURL)
    search = requests.get(searchURL)
    search.raise_for_status()
    soup1 = BeautifulSoup(search.text,'html.parser')
    linkElements = soup1.select('.r a')
    numLinks = min(3,len(linkElements))
    #for i in range(numLinks):
        #webbrowser.open_new(linkElements[i].get('href'))
    #break
    print date,'+',openPrice,'+',closePrice
   
    #print("~~~~~~~~~~~~~~~~~~~")
    #print "Date:",date
    #print "Open:",openPrice
    #print "Close:",closePrice    
    #print("~~~~~~~~~~~~~~~~~~~")
    

    
    
    
