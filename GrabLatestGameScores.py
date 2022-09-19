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


def GrabLatestGameScores():

    game_scores  = stats_page.find_all('table',class_='teams')
    game_number = 1


    for game_score in game_scores:

        losing_team = game_score.find(class_="loser")
        winning_team = game_score.find(class_="winner")
        print(f"Game {game_number}")
        print(f"{winning_team.contents[1].text.strip()} {winning_team.contents[3].text}")
        print(f"{losing_team.contents[1].text.strip()} {losing_team.contents[3].text}")

        game_number = game_number+1

def GrabStats():

    player_stats = stats_page.find_all('table',class_='stats')

    for player_stat in player_stats:
        top_passer = player_stats.find()


GrabLatestGameScores()


