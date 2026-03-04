# Pulling NBA Data

## Link Directory 
- [colab](https://colab.research.google.com/drive/1Z2egQVk9wMvgxuJdX1dQfK9hZb7uheMp?usp=sharing#scrollTo=McWElB8dVJ4R)
- [proposal](https://docs.google.com/document/d/1PT-N8yz52p085xTtOs6XFQ2Y8TVXUJsnfTHcmKbnP7w/edit?tab=t.0#heading=h.tgynognlbwvg)

## Data Retreival Plan
- [2004-2024 shot data for every season with player named/ids](https://www.kaggle.com/datasets/mexwell/nba-shots)
- [Pull player specific biometric](https://github.com/swar/nba_api) data for each season, join that with individual season shot data
	- season over season biometric changes per player don't matter because anonymized
- After taking the join of those datasets, remove player identifying info (teams, id, name)
  - Basically go through and drop columns we want 
- Final output of pipeline goal is to be a csv

## Post Data Retreval Plan
- When everything is in and set up
  - run VAF for multi-colinearity 
- keep the year on, for stratification and analyzation of results but DONT train on it, 

- Goal row: each shot from each ear
