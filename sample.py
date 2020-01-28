
from bs4 import BeautifulSoup 
import urllib.request 
def make_soup(url): 
    thepage=urllib.request.urlopen(url) 
    soupdata=BeautifulSoup(thepage, "html.parser") 
    return soupdata 

soup= make_soup("https://en.wikipedia.org/wiki/2015_in_hip_hop_music") 
albumdatasaved="" 
# find all table ,get the first 
table = soup.find_all('table', class_="wikitable")[0] # Only use the first table 
# iter over it 
for record in table.findAll('tr'): 
    albumdata="" 
    for data in record.findAll('td'): 
     albumdata=albumdata+","+data.text 
    albumdatasaved=albumdatasaved+"\n"+albumdata[1:] 

print(albumdatasaved) 