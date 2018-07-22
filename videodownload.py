import os
import sys
import requests
from bs4 import BeautifulSoup
soup = BeautifulSoup(open('Film Noir _ Free Movies _ Free Download, Borrow and Streaming _ Internet Archive.html'),'html.parser')
soup.find('body').find('div',{'class':'results'}).find_all('div',{'class':'C234'})
data = soup.find('body').find('div',{'class':'results'}).find_all('div',{'class':'C234'})
for C234 in data:
   page_link = C234.find('a').href
   print(page_link)




