import pandas as pd
import json
from nba_api.stats.endpoints import LeagueDashPlayerBioStats

## Asking "return every player with the season=2025-26"
bio = LeagueDashPlayerBioStats(season="2024-25")
df = bio.get_data_frames()[0]   # 0 because this specific endpoint only returns one results set 
print(df.columns.tolist())

df.to_csv('NBA_2025_Players.csv', index=False)



