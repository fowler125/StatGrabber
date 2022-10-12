from urllib.request import urlopen
from bs4 import BeautifulSoup


# URL of page
url = 'https://www.pro-football-reference.com/boxscores/'

# Open URL and pass to BeautifulSoup
html = urlopen(url)
stats_page = BeautifulSoup(html, 'html.parser')

TOP_PASSERS = stats_page.find_all('tr')

def TopWeekStats():
    print(TOP_PASSERS)
    #print(stats_page.find_all('tr'))


TopWeekStats()