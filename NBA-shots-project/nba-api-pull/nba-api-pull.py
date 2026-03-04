# What we get from API: 
##['PLAYER_ID', 'PLAYER_NAME', 'TEAM_ID', 'TEAM_ABBREVIATION', 'AGE', 'PLAYER_HEIGHT', 'PLAYER_HEIGHT_INCHES', 'PLAYER_WEIGHT', 'COLLEGE', 'COUNTRY', 'DRAFT_YEAR', 'DRAFT_ROUND', 'DRAFT_NUMBER', 'GP', 'PTS', 'REB', 'AST', 'NET_RATING', 'OREB_PCT', 'DREB_PCT', 'USG_PCT', 'TS_PCT', 'AST_PCT']
# What we want as output (no specific order):
##[PLAYER_ID,PLAYER_NAME,AGE,PLAYER_HEIGHT_INCHES,PLAYER_WEIGHT,DRAFT_YEAR,SEASON_1]
### Structure of SEASON_1 = '2024' 

# User Notes
## You may need to play with TIME_BETWEEN_CALLS to prevent rate limit blocking from the NBA 

import time
import pandas as pd
from nba_api.stats.endpoints import LeagueDashPlayerBioStats

# Display Settings
pd.set_option('display.max_columns', None)

# Var init 
SEASONS_TO_PULL = [
    "2003-04", "2004-05", "2005-06", "2006-07", "2007-08",
    "2008-09", "2009-10", "2010-11", "2011-12", "2012-13",
    "2013-14", "2014-15", "2015-16", "2016-17", "2017-18",
    "2018-19", "2019-20", "2020-21", "2021-22", "2022-23",
    "2023-24"
]
COLS_TO_DROP = ['TEAM_ID', 'TEAM_ABBREVIATION', 'PLAYER_HEIGHT', 'COLLEGE', 'COUNTRY', 'DRAFT_ROUND', 'DRAFT_NUMBER', 'GP', 'PTS', 'REB', 'AST', 'NET_RATING', 'OREB_PCT', 'DREB_PCT', 'USG_PCT', 'TS_PCT', 'AST_PCT']
TIME_BETWEEN_CALLS = 30

seasonIndex = 0
for season1 in range(2004, 2025):
  # Asking "return every player with the season=season1"
  allFromSeason = LeagueDashPlayerBioStats(
    season=SEASONS_TO_PULL[seasonIndex]
  )

  currentSeasonFrame = allFromSeason.get_data_frames()[0]   # 0 because this specific endpoint only returns one results set 
  currentSeasonFrame = currentSeasonFrame.drop(columns = COLS_TO_DROP)
  currentSeasonFrame['SEASON_1'] = season1
  currentSeasonFrame.to_csv('NBA_' + str(season1) + '_Players.csv', index=False)
  print('NBA_' + str(season1) + '_Players.csv has been successfully retrieved and created. \nIt pulled from the ' + SEASONS_TO_PULL[seasonIndex] + ' Season')
  seasonIndex += 1
  time.sleep(TIME_BETWEEN_CALLS)

print('Data retrieval complete!!')  













