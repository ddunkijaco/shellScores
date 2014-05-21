import requests
from xml.etree import ElementTree
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-l')
args = parser.parse_args()

def showScores(leagues=[]):
    if leagues == []:
        leagues = ['NFL', 'MLB', 'NHL', 'NBA', 'NCF']

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

showScores(args.l.split(",") if args.l else [])
