# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 19:00:14 2019

@author: Dell
"""
1

import requests
from bs4 import BeautifulSoup
'''
def get_html(url):
    r = requests.get(url)
    return r.text

def get_data(html):
    soup = BeautifulSoup(html,'lxml')
    h1 = soup.find('div', id = 'home-welcome').find('body').find('h1').text
    return h1

def main():
    url = 'http://example.com/'
    print(get_data(get_html(url)))
    
if __name__ == '__main__':
    main()
'''

def get_html(url):
 	r = requests.get(url)
 	return r.text

def get_data(html):
    soup = BeautifulSoup(html,'lxml')
    h1 = soup.text
    return h1


def main():
    url = "http://www.nbrb.by/API/ExRates/Rates/145"
    data1 =get_data(get_html(url))
    dct1 = {}
    dct1 = eval(data1)
    url2 = "http://www.nbrb.by/API/ExRates/Rates/292"
    data2 =get_data(get_html(url2))
    dct2 = {}
    dct2 = eval(data2)
    
    GreateDate = dct1["Date"]
    Today = GreateDate[8:10]+'.' + GreateDate[5:7] + '.' + GreateDate[:4]
    
    print('За ',Today, ' курс ',dct2["Cur_OfficialRate"],' рублей за 1 Евро, ',dct1["Cur_OfficialRate"],' за 1 доллар')
main()


'''
if __name__ == '__main__':
 	main()'''