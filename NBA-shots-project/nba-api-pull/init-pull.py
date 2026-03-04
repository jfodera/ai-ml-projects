import pandas as pd
import json
from nba_api.stats.endpoints import LeagueDashPlayerBioStats
from nba_api.stats.endpoints import commonplayerinfo 

# ## Asking "return every player with the season=2025-26"
# allFromSeason = LeagueDashPlayerBioStats(
#   season="2024-25"
# )
# df = allFromSeason.get_data_frames()[0]   # 0 because this specific endpoint only returns one results set 

# Create the endpoint object with the player ID (required parameter)
# playerInfo = commonplayerinfo.CommonPlayerInfo(
#   player_id=2544,                # LeBron James' NBA player ID
# )

# df1 = playerInfo.get_data_frames()[0]

# print(df1.columns.tolist())

pid = 1628389  # Example: Lonzo Ball (ID; adjust for current players)
info = commonplayerinfo.CommonPlayerInfo(player_id=pid)
print(info.common_player_info.get_data_frame()[['DISPLAY_FIRST_LAST', 'SEASON_EXP']])

# df.to_csv('NBA_2025_Players.csv', index=False)



