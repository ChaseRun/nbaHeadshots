# nbaHeadshots

#### A package for downloading NBA player headshots from stats.NBA.com

##### Development Version: v0.0.1

`nbaHeadshots` was created to make player headsnhots from `www.stats.nba.com` more accessible and easilly downloadable. 

## Installation
```commandline
pip install nbaHeadshots
```

## Example Usage
Currently the package only consists of two functions:
* `getHeadshotById(id, saveFolder, fileName=None)`
* `getAllHeadshots(saveFolder)`


Player Id's are based on `www.stats.nba.com` player ids. [nba_api](https://github.com/swar/nba_api) is an easy way to get a list of these player ids and its also useful for getting nab statistics. There is a json file of basic player information loacted at `src/playerInfo.json`. Image files are saved in .png format. Different formats can be used by specifying fileName.

```python
from nbaHeadshots import getHeadshotById, getAllHeadshots

# Lebron James headshot will be saved as lebron.jpg in saveHere folder
getHeadshotById(2544, folder="saveHere/", fileName="lebron.jpg")

# Lebron James headshot will be saved as 2544.png in current directory
getHeadshotById(2544)

# All headshots will be saved as "id".png in saveHere folder
getAllHeadshots("saveHere/")
```

