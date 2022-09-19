from urllib.request import urlopen
from bs4 import BeautifulSoup

# Import data manipulation modules
import pandas as pd
import numpy as np

# Import data visualization modules
import matplotlib as mpl
import matplotlib.pyplot as plt

# URL of page
url = 'https://www.pro-football-reference.com/boxscores/'
# Open URL and pass to BeautifulSoup
html = urlopen(url)
stats_page = BeautifulSoup(html, 'html.parser')

#print(stats_page.prettify())
#print(stats_page.tr)
#print(stats_page.findAll('tr'))


def GrabGameScores():

    game_scores  = stats_page.find_all('table',class_='teams')
    #print(game_scores)

    for game_score in game_scores:
        loser_team = game_score.find_next(class_="loser")
        winner_team = game_score.find_next(class_="winner")
        print(winner_team.text.strip())
        print(loser_team.text.strip())




#stats_page.findAll(name)