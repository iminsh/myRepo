#! python3
# bd.py - open several Baidu search results

import requests, sys, webbrowser, bs4

print('baiduing...')
res = requests.get('http://www.baidu.com/s?wd=beautifulsoup4')
res.raise_for_status()

# retrieve top serach result links
soup = bs4.BeautifulSoup(res.text, 'lxml')

# open a browser tab for each result
linkElems = soup.select('.t a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    strLink = linkElems[i].get('href')
    print('===', strLink, '===')
    # webbrowser.open(strLink)

    res = requests.get(strLink)
    res.raise_for_status()
    print('URL:', res.url)
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    imgs = soup.select('img')
    for imgTag in imgs:
        print('\t', imgTag.get('src'))
    
    print('======================')
    

    

