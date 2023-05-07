from urllib.request import urlopen
from bs4 import BeautifulSoup
import os


# URL of page
url = 'https://www.pro-football-reference.com/boxscores/'

# Open URL and pass to BeautifulSoup
html = urlopen(url)
stats_page = BeautifulSoup(html, 'html.parser')

winner = ""
loser = ""
stat = 0
WEEK_NUMBER = stats_page.find(class_='section_heading').text.strip()
print(WEEK_NUMBER)

Dict = {
    'Arizona Cardinals': 'ARI',
    'Atlanta Falcons': 'ATL',
    'Baltimore Ravens': 'BAL',
    'Buffalo Bills': 'BUF',
    'Carolina Panthers': 'CAR',
    'Chicago Bears': 'CHI',
    'Cincinnati Bengals': 'CIN',
    'Cleveland Browns':'CLE',
    'Dallas Cowboys':'DAL',
    'Denver Broncos':'DEN',
    'Detroit Lions':'DET',
    'Green Bay Packers':'GB',
    'Houston Texans':'HOU',
    'Indianapolis Colts':'IND',
    'Jacksonville Jaguars': 'JAC',
    'Kansas City Chiefs': 'KC',
    'Las Vegas Raiders':'LV',
    'Los Angeles Chargers': 'CHA',
    'Los Angeles Rams':'LAR',
    'Miami Dolphins':'MIA',
    'Minnesota Vikings':'MIN',
    'New England Patriots':'NE',
    'New Orleans Saints':'NO',
    'New York Giants':'NYG',
    'New York Jets':'NYJ',
    'Philadelphia Eagles':'PHI',
    'Pittsburgh Steelers':'PIT',
    'San Francisco 49ers':'SF',
    'Seattle Seahawks':'SEA',
    'Tampa Bay Buccaneers':'TB',
    'Tennessee Titans':'TEN',
    'Washington Commanders':'WAS'
}


def GrabLatestGameScores():
    game_scores = stats_page.find_all('table', class_='teams')
    game_number = 1

    for game_score in game_scores:

        losing_team = game_score.find(class_="loser")
        winning_team = game_score.find(class_="winner")

        WinnerName = winning_team.contents[1].text.strip()
        LoserName = losing_team.contents[1].text.strip()

        try:
            file1 = open(f"GameScores/{WEEK_NUMBER}/{Dict[WinnerName]}v{Dict[LoserName]}.txt", "w+")
            print(f"{winning_team.contents[1].text.strip()} - {winning_team.contents[3].text}")
            file1.writelines(f" {winning_team.contents[1].text.strip()} - {winning_team.contents[3].text} \n")

            print(f"{losing_team.contents[1].text.strip()} - {losing_team.contents[3].text}")
            file1.writelines(f" {losing_team.contents[1].text.strip()} - {losing_team.contents[3].text} \n")

            GrabStats(WinnerName, LoserName, game_number - 1)
            winner = WinnerName
            loser = LoserName
            stat = game_number-1

            game_number = game_number + 1

        except FileNotFoundError as e:
            os.makedirs(f"GameScores/{WEEK_NUMBER}")
            GrabLatestGameScores()



        file1.close()



def GrabStats(winner,loser,stat):
    player_stats = stats_page.find_all('table', class_='stats')
    # print(player_stats)
    TOP_PASSER_LABEL = player_stats[stat].contents[1].contents[1].contents[1].text.strip()
    TOP_PASSER_NAME = player_stats[stat].contents[1].contents[1].contents[3].text.strip()
    TOP_PASSER_YDS = player_stats[stat].contents[1].contents[1].contents[5].text.strip()

    TOP_RUSHER_LABEL = player_stats[stat].contents[1].contents[3].contents[1].text.strip()
    TOP_RUSHER_NAME = player_stats[stat].contents[1].contents[3].contents[3].text.strip()
    TOP_RUSHER_YDS = player_stats[stat].contents[1].contents[3].contents[5].text.strip()

    TOP_RECEIVER_LABEL = player_stats[stat].contents[1].contents[5].contents[1].text.strip()
    TOP_RECEIVER_NAME = player_stats[stat].contents[1].contents[5].contents[3].text.strip()
    TOP_RECEIVER_YDS = player_stats[stat].contents[1].contents[5].contents[5].text.strip()
    try:
        PlayerScores = open(f"TopPlayerStats/{WEEK_NUMBER}/{Dict[winner]}v{Dict[loser]}stats.txt", "w+")

        print(f"{TOP_PASSER_LABEL} {TOP_PASSER_NAME} {TOP_PASSER_YDS}")
        PlayerScores.writelines(f"{TOP_PASSER_LABEL} {TOP_PASSER_NAME} {TOP_PASSER_YDS}\n")

        print(f"{TOP_RUSHER_LABEL} {TOP_RUSHER_NAME} {TOP_RUSHER_YDS} ")
        PlayerScores.writelines(f"{TOP_RUSHER_LABEL} {TOP_RUSHER_NAME} {TOP_RUSHER_YDS}\n")

        print(f"{TOP_RECEIVER_LABEL} {TOP_RECEIVER_NAME} {TOP_RECEIVER_YDS} ")
        PlayerScores.writelines(f"{TOP_RECEIVER_LABEL} {TOP_RECEIVER_NAME} {TOP_RECEIVER_YDS}\n")

        PlayerScores.close()
    except FileNotFoundError as e:
        os.makedirs(f"TopPlayerStats/{WEEK_NUMBER}")
        GrabStats(winner,loser,stat)




GrabLatestGameScores()

