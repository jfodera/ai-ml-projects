# Pulling NBA Data

## Link Directory 
- [colab](https://colab.research.google.com/drive/1Z2egQVk9wMvgxuJdX1dQfK9hZb7uheMp?usp=sharing#scrollTo=McWElB8dVJ4R)
- [proposal](https://docs.google.com/document/d/1PT-N8yz52p085xTtOs6XFQ2Y8TVXUJsnfTHcmKbnP7w/edit?tab=t.0#heading=h.tgynognlbwvg)

## Data Retrieval Plan
- [2004-2024 shot data for every season with player named/ids](https://www.kaggle.com/datasets/mexwell/nba-shots)
- [Pull player specific biometric](https://github.com/swar/nba_api) data for each season, join that with individual season shot data
	- season over season biometric changes per player don't matter because anonymized
  - Going to pull locally so we only have to retrieve from API once (not every single time we run the colab)
    - This is because NBA.com could change their standards/documentation for data retrieval at any moment, so hopefully out project would require less frequent updates to stay working if we already have the data as a CSV file (or maybe we make a kaggle)
  - Could also utilize [this Kaggle](https://www.kaggle.com/datasets/justinas/nba-players-data) if pulling is difficult
  - Note that what we are pulling from with LeagueDashPlayerBioStats is structured as such: 
    - for each year there is a relation with its own set of NBA players that played that year
    - each player from each is its own seperate row (even if said player has played multiple years)
    - This is the structure we are trying to replicate with our output. 
  - **Goal Output from NBA Player API**: Player Name, NBA Player ID, Year Played, age, Height, Weight, draftYear
  

- After taking the join of those datasets, remove player identifying info (teams, id, name)
  - Basically go through and drop columns we want 
- Final output of pipeline goal is to be a csv


### Before submit
- Do we want to make the player biometric data a kaggle? 
- Ask team if we want to include draft year in biometric data? 
  - draftYear, yearsExperience or both? 
- retrieving years experience is possible using the NBA API, but requires some more in api manipulation, so I wanted to check with you guys before I put the time into doing that
- Let team know that wingspan information is only available for players that attended the combine (not all players) 
  - so is it something we should include or no? 
- How do we want to handle undrafted players? 
- move our output over to Kaggle
- I dropped POSITION_GROUP is that ok? 
## Things learned
- The [nba API](https://github.com/swar/nba_api?tab=readme-ov-file) we are using is a wrapper on the official API on NBA.com
  - In clicking around NBA.com, it seems the URL is simply a get request to their API, returning the HTML output 
    - confirmed via postman 
  - The repo itself seems up to date as it was last updated 2 weeks ago 
    - The function of the repo, along with being a wrapper is to, provide extensive documentation about the NBA API's to allow for ease of use 
- LeagueDashPlayerBioStats nba API source code is [here](https://github.com/swar/nba_api/blob/master/src/nba_api/stats/endpoints/leaguedashplayerbiostats.py)
  - This is what we will be 'calling' on the nba_api end 
## Post Data Retrieval Plan
- When everything is in and set up
  - run VAF for multi-colinearity 
- keep the year on, for stratification and analyzation of results but DONT train on it, 

- Goal row: each shot from each ear


# Current 
- Now just need to turn this into a loop that adjusts for rate limits to fully be done