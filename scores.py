import datetime
import time
import urllib2
from xml.etree import ElementTree
import json
import argparse
import requests

parser = argparse.ArgumentParser()
parser.add_argument('-l')
parser.add_argument('-t')
parser.add_argument('-d')
args = parser.parse_args()

games = []
home_score = []
heading = []
away_score = []

league = args.l
today = str(datetime.date.today())
yyyymmdd = today.replace('-', '')
url = 'http://scores.nbcsports.msnbc.com/ticker/data/gamesMSNBC.js.asp?jsonp=true&sport=%s&period=%s'

def getBoxScore(date, url, league, team):
    header_space = ''
    header_print = ''
    away_print = ''
    home_print = ''
    f = urllib2.urlopen(url % (league, date))
    jsonp = f.read()
    f.close()
    json_str = jsonp.replace('shsMSNBCTicker.loadGamesData(', '').replace(');', '')
    json_parsed = json.loads(json_str)
    for game_str in json_parsed.get('games', []):
        game_tree = ElementTree.XML(game_str)
        away_tree = game_tree.find('visiting-team')
        home_tree = game_tree.find('home-team')
        gamestate_tree = game_tree.find('gamestate')
        home = home_tree.get('nickname')
        away = away_tree.get('nickname')
        home_alias = home_tree.get('alias')
        away_alias = away_tree.get('alias')
        team = team.lower()
        if away.lower() == team or home.lower() == team or home_alias.lower() == team or away_alias.lower() == team:
            if gamestate_tree.get('status') == "Pre-Game":
                print "Game starting at " + gamestate_tree.get('gametime')
            elif gamestate_tree.get('status') == "In-Progress" or gamestate_tree.get('status') == "Final":                
                print '%s: %s %s' % (gamestate_tree.get('status'), gamestate_tree.get('display_status1'), gamestate_tree.get('display_status2'))
                for score in home_tree.findall('score'):
                    if len(score.attrib.get('heading')) == 1:
                        heading.append(' %s ' % score.attrib.get('heading'))
                    elif len(score.attrib.get('heading')) == 2:
                        heading.append(' %s' % score.attrib.get('heading'))
                    else: heading.append('%s' % score.attrib.get('heading'))
                    if len(score.attrib.get('value')) == 1:
                        home_score.append(' %s ' % score.attrib.get('value'))
                    elif len(score.attrib.get('value')) == 2:
                        home_score.append(' %s' % score.attrib.get('value'))
                    else: home_score.append('%s' % score.attrib.get('value'))
                for score in away_tree.findall('score'):
                    if len(score.attrib.get('value')) == 1:
                        away_score.append(' %s ' % score.attrib.get('value'))
                    elif len(score.attrib.get('value')) == 2:
                        away_score.append(' %s' % score.attrib.get('value'))
                    else: away_score.append('%s' % score.attrib.get('value'))
                while len(away) < len(home):
                    away = away + ' '
                while len(home) < len(away):
                    home = home + ' '
                while len(header_space) < len(away):
                    header_space = header_space + ' '
                for x in range(len(heading)):
                    header_print += '' + heading[x] + '|'
                    away_print += '' + away_score[x] + '|'
                    home_print += '' + home_score[x] + '|'
                print len(heading)
                print header_space + '|' + header_print
                print away + '|' + away_print
                print home + '|' + home_print
                break
        
def showScores(leagues):
    for league in range(len(leagues)):
        response = requests.get('http://wu.apple.com/' + leagues[league].lower() + '/bottomline/xml/scores')
        events = ElementTree.fromstring(response.text)
        print '\n' + leagues[league] + ':'
        for game in events.iter("GAME"):
            printScores(game)

def printScores(game):
    home_team = game.find('./HOME/TEAM').text
    home_score = game.find('./HOME/SCORE').text
    away_team = game.find('./AWAY/TEAM').text
    away_score = game.find('./AWAY/SCORE').text
    game_status = game.find('./STATUS').text
    print "%s: %s, %s: %s. %s" % (away_team, away_score, home_team, home_score, game_status)

if args.t:
    getBoxScore(args.d if args.d else yyyymmdd, url,args.l,args.t)
else: showScores(args.l.split(",") if args.l else ['NFL', 'MLB', 'NHL', 'NBA', 'NCF'])


