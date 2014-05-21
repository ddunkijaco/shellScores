import requests
from xml.etree import ElementTree
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-l')
args = parser.parse_args()

def showScores(league=''):
    if league == '':
        leagues = ['NFL', 'MLB', 'NHL', 'NBA', 'NCF']
        for league in range(len(leagues)):
            response = requests.get('http://wu.apple.com/' + leagues[league].lower() + '/bottomline/xml/scores')
            events = ElementTree.fromstring(response.text) 
            print '\n' + leagues[league] + ':'
            for game in events.iter("GAME"):
                printScores(game)           
    else:
        response = requests.get('http://wu.apple.com/' + args.l.lower() + '/bottomline/xml/scores')
        events = ElementTree.fromstring(response.text) 
        print league.upper() + ':'
        for game in events.iter("GAME"):
            printScores(game)

def printScores(game):
    hTeam = game.find('./HOME/TEAM').text
    hScore = game.find('./HOME/SCORE').text
    aTeam = game.find('./AWAY/TEAM').text
    aScore = game.find('./AWAY/SCORE').text
    gStatus = game.find('./STATUS').text
    print aTeam + ': ' + aScore + ', ' + hTeam + ': ' + hScore + '. ' + gStatus

showScores(args.l if args.l else '')
