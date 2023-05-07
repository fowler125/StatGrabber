from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import date
from datetime import datetime
import matplotlib.pyplot as plt

today = date.today()

now = datetime.now()

d4 = today.strftime("%b-%d-%Y")
print("Today's Date =", d4)

# URL of page
url = 'https://www.pro-football-reference.com/years/2022/leaders.htm'

# Open URL and pass to BeautifulSoup
html = urlopen(url)
stats_page = BeautifulSoup(html, 'html.parser')

TOP_PASSERS = stats_page.find('div', id='leaders_pass_yds')

fig,ax = plt.subplots()

def TopWeekStats():
    z = 1
    i = 1
    WeekScores = open(f"TopWeekStats/{d4} stats.txt", "w+")
    for TOP_PASSER in TOP_PASSERS:
        PASSING_RANK = TOP_PASSERS.contents[i].contents[z+2].contents[i].text.strip()
        PASSING_NAME = TOP_PASSERS.contents[i].contents[z+2].contents[i+2].text.strip()
        PASSING_NUM = TOP_PASSERS.contents[i].contents[z+2].contents[i+4].text.strip()

        print(PASSING_RANK)
        WeekScores.writelines(f"{PASSING_RANK}\n")
        print(PASSING_NAME)
        WeekScores.writelines(f"{PASSING_NAME}\n")
        print(PASSING_NUM)
        WeekScores.writelines(f"{PASSING_NUM}\n")
        z = z+2

def TopPassingVisual():
    z = 1
    i = 1
    players = []
    yards=[]
    bar_labels = ['red','blue','_red','orange','_blue','green']

    bar_colors = ['tab:red','tab:blue','tab:red','tab:orange','tab:blue','tab:green']
    for TOP_PASSER in TOP_PASSERS:
        PASSING_RANK = TOP_PASSERS.contents[i].contents[z+2].contents[i].text.strip()
        PASSING_NAME = TOP_PASSERS.contents[i].contents[z+2].contents[i+2].text.strip()
        PASSING_NUM = TOP_PASSERS.contents[i].contents[z+2].contents[i+4].text.strip()

        print(PASSING_RANK)


        print(PASSING_NAME)
        players.append(PASSING_NAME)
        print(PASSING_NUM)
        yards.append(PASSING_NUM)

        z = z+2

    ax.bar(players,yards,label=bar_labels,color=bar_colors)
    ax.set_ylabel('Passing Yards')
    ax.set_title('Top Passing Leaders')
    ax.legend('Players')
    plt.show()

    #print(TOP_PASSERS.text.strip())

    #print(stats_page.find_all('tr'))

#TopPassingVisual()
TopWeekStats()