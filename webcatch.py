from bs4 import BeautifulSoup
import requests

def get_links():
    links = []
    page = requests.get('https://codefinity.com/blog/30-Python-Project-Ideas-for-Beginners?utm_source=google&utm_medium=cpc&utm_campaign=20955067105&utm_content=158811191432&utm_term=&gad_source=1&gclid=Cj0KCQjwu8uyBhC6ARIsAKwBGpRCVNxXXEemjVoeUfBBlYXycTAp2yskCHezu16EBveK5VaDGAVccSwaAkWgEALw_wcB')
   
    soup = BeautifulSoup(page.text, 'html.parser')
    buttons = soup.find_all('a')
    for link in buttons:
        if link.get('href') != None and 'http' in link.get('href'):
            print(link.get('href'))
            links.append(link.get('href'))
    
    return links


def putinfile(links):
    with open('links2.txt', 'x') as f:
        for linkbro in links:
            f.write(linkbro + '\n')        



passlink = input('Digite o link da página:')
putinfile(get_links())
