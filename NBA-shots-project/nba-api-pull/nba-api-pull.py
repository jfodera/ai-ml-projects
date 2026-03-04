# What we get from API: 
##['PLAYER_ID', 'PLAYER_NAME', 'TEAM_ID', 'TEAM_ABBREVIATION', 'AGE', 'PLAYER_HEIGHT', 'PLAYER_HEIGHT_INCHES', 'PLAYER_WEIGHT', 'COLLEGE', 'COUNTRY', 'DRAFT_YEAR', 'DRAFT_ROUND', 'DRAFT_NUMBER', 'GP', 'PTS', 'REB', 'AST', 'NET_RATING', 'OREB_PCT', 'DREB_PCT', 'USG_PCT', 'TS_PCT', 'AST_PCT']
# What we want as output (no specific order):
##[PLAYER_ID,PLAYER_NAME,AGE,PLAYER_HEIGHT_INCHES,PLAYER_WEIGHT,DRAFT_YEAR,SEASON_1]
### Structure of SEASON_1 = '2024' 

import pandas as pd
from nba_api.stats.endpoints import LeagueDashPlayerBioStats

# Display Settings
pd.set_option('display.max_columns', None)

# Var init 
seasonsToPull = [
    "2003-04", "2004-05", "2005-06", "2006-07", "2007-08",
    "2008-09", "2009-10", "2010-11", "2011-12", "2012-13",
    "2013-14", "2014-15", "2015-16", "2016-17", "2017-18",
    "2018-19", "2019-20", "2020-21", "2021-22", "2022-23",
    "2023-24"
]
colsToDrop = ['TEAM_ID', 'TEAM_ABBREVIATION', 'PLAYER_HEIGHT', 'COLLEGE', 'COUNTRY', 'DRAFT_ROUND', 'DRAFT_NUMBER', 'GP', 'PTS', 'REB', 'AST', 'NET_RATING', 'OREB_PCT', 'DREB_PCT', 'USG_PCT', 'TS_PCT', 'AST_PCT']


seasonIndex = 0
for season1 in range(2004, 2025):
  # Asking "return every player with the season=2025-26"
  allFromSeason = LeagueDashPlayerBioStats(
    season=seasonsToPull[seasonIndex]
  )
  seasonIndex += 1

  currentSeasonFrame = allFromSeason.get_data_frames()[0]   # 0 because this specific endpoint only returns one results set 
  currentSeasonFrame = currentSeasonFrame.drop(columns = colsToDrop)
  currentSeasonFrame['SEASON_1'] = season1
  currentSeasonFrame.to_csv('NBA_' + str(season1) + '_Players.csv', index=False)
  print('NBA_' + str(season1) + '_Players.csv has been successfully pulled ')
  













