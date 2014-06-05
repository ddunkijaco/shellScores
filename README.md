shellScores
===========

shellScores is a python script created to show recent sports scores in the console.

shellScores requires Python 2.7 and the [Requests library](http://docs.python-requests.org/en/latest/) which can be installed via Python's easy_install using:
```
$ easy_install requests
```

If easy\_install is not installed, download ez\_setup [here](https://bootstrap.pypa.io/ez_setup.py) and install Python's setuptools by running:
```
$ python path/to/ez_setup.py
```

Boxscore data is provided by MSNBC, league score data by ESPN and odds by Bovada via their JSON-based web APIs.

Usage
===========
Executing scores.py without any arguments will provide a list of valid leagues and the most recent available scores as well as their respective starting time or current progress.

```
$ python scores.py

NFL:
Seattle: 43, Denver: 8. FINAL

MLB:
San Francisco: 6, Cincinnati: 1. FINAL
Oakland: 1, NY Yankees: 2. FINAL
Toronto: 7, Detroit: 3. FINAL
Philadelphia: 1, Washington: 4. BOT 6TH
Miami: 3, Tampa Bay: 3. TOP 6TH
NY Mets: 0, Chicago Cubs: 0. 7:05 PM ET
LA Angels: 0, Houston: 0. 7:10 PM ET
Baltimore: 0, Texas: 0. 8:05 PM ET
St. Louis: 0, Kansas City: 0. 8:10 PM ET
Milwaukee: 0, Minnesota: 0. 8:10 PM ET
Arizona: 0, Colorado: 0. 8:40 PM ET

NHL:

NBA:
Miami Heat: 0, San Antonio Spurs: 0. 9:00 PM ET

NCF:
EAST: 23, WEST: 13. FINAL
AMERICAN: 17, NATIONAL: 31. FINAL
NORTH: 10, SOUTH: 20. FINAL
```
Arguments
===========
####The -l argument
The use of the -l argument followed by the three letter abbreviation of a valid league [MLB, NFL, NBA, NHL, NCF] will print the scores and status of games occuring today in that league.

```
$ python scores.py -l MLB

MLB:
San Francisco: 6, Cincinnati: 1. FINAL
Oakland: 1, NY Yankees: 2. FINAL
Toronto: 7, Detroit: 3. FINAL
Philadelphia: 1, Washington: 4. BOT 6TH
Miami: 4, Tampa Bay: 3. TOP 6TH
NY Mets: 0, Chicago Cubs: 0. 7:05 PM ET
LA Angels: 0, Houston: 0. 7:10 PM ET
Baltimore: 0, Texas: 0. 8:05 PM ET
St. Louis: 0, Kansas City: 0. 8:10 PM ET
Milwaukee: 0, Minnesota: 0. 8:10 PM ET
Arizona: 0, Colorado: 0. 8:40 PM ET
```

####The -t argument (requires -l)
The -t argument allows the user to specify a team within a league. If the game is in progress, the script will print a current box-score and current status including rain delays. Specifying a league is required. The -t argument will accept the three letter abbreviation or the team nickname. (SJS | Sharks = San Jose Sharks).

```
$ python scores.py -l MLB -t SF
Final: Final
       | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | R | H | E |
Giants | 0 | 2 | 0 | 3 | 0 | 0 | 1 | 0 | 0 | 6 | 11| 0 |
Reds   | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 3 | 0 |
```

The box score will grow or shrink based on current number of innings/periods/quarters.

```
$ python scores.py -l MLB -t MIA
In-Progress: Bot 6th
        | 1 | 2 | 3 | 4 | 5 | 6 | R | H | E |
Marlins | 0 | 0 | 0 | 3 | 0 | 3 | 6 | 10| 0 |
Rays    | 1 | 0 | 0 | 0 | 2 | 2 | 5 | 9 | 0 |
```

If the game has not begun, the script will print the starting time.

```
$ python scores.py -l NBA -t Heat
Game starting at 9:00 PM ET
```

####The -d argument (requires -l and -t)
The -d argument allows the user to specify a date in the past to look up a box score. The API results vary on how far they go back, but typically go back at least one week.

Must be specified as YYYYMMDD.

```
$ python scores.py -l MLB -t SF -d 20140604
Final: Final
       | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | R | H | E |
Giants | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 3 | 7 | 3 |
Reds   | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 7 | 0 |
```

####The -odds argument
Using -odds followed by a valid league [MLB, NFL, NBA, NHL, NCF] will provide the moneyline odds for games in that league for the current day.
```
$ python scores.py -odds MLB

Baseball - MLB
 Thu, Jun 5, 14
   Texas Rangers (-108) vs. Baltimore Orioles (-102) []
   New York Yankees (-150) vs. Oakland Athletics (+135) [Final]
   Colorado Rockies (-128) vs. Arizona Diamondbacks (+118) []
   Houston Astros (+134) vs. Los Angeles Angels (-144) []
   Detroit Tigers (-165) vs. Toronto Blue Jays (+150) [Final]
   Washington Nationals (-220) vs. Philadelphia Phillies (+190) [Top 7 Inning]
   Chicago Cubs (-116) vs. New York Mets (+106) []
   Cincinnati Reds (+118) vs. San Francisco Giants (-128) [Final]
   Minnesota Twins (+117) vs. Milwaukee Brewers (-127) []
   Tampa Bay Rays (-172) vs. Miami Marlins (+157) [Top 6 Inning]
   Kansas City Royals (+110) vs. St. Louis Cardinals (-120) []
```
