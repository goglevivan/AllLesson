# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 13:17:07 2019

@author: Dell
"""
import requests
from bs4 import BeautifulSoup as bs
headers = {'accept':'*/*',
           'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'}
stringinf=[]
url ='https://vk.com/id172101791'
def get_html(url,headers):
    session = requests.Session()
    request = session.get(url,headers = headers)
    if request.status_code == 200:
        soup = bs(request.content,'html.parser') 
        divs = soup.find_all('div',attrs={'class':"clear_fix profile_info_row "})
        for div in divs:
            title = div.find('a')
            stringinf.append(title)
            zn = stringinf[-1]
            zn = str(zn)
        return zn[115:-4]
            
    else:
        return'ERROR'

print(get_html(url,headers))
