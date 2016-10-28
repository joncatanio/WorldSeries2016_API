import json
from datetime import date
from flask import Blueprint, request

content_api = Blueprint('content_api', __name__)

@content_api.route("/getcontent/<int:year>/<int:month>/<int:day>")
def getcontent(year, month, day):
   curDate = date(year, month, day)

   if year == None or month == None or day == None:
      temp =  date.today()
      curDate = date(temp.year, temp.month, temp.day)

   try:
      f = open('./datastore/' + curDate.isoformat() + '.txt', 'r')
   except IOError:
      return json.dumps({'message': 'no information for given date'}), 500

   return json.dumps(json.load(f)), 200

@content_api.route("/getgames/<int:year>/<int:month>/<int:day>")
def getgames(year, month, day):
   curDate = date(year, month, day)

   if year == None or month == None or day == None:
      temp =  date.today()
      curDate = date(temp.year, temp.month, temp.day)

   try:
      f = open('./datastore/' + curDate.isoformat() + '.txt', 'r')
   except IOError:
      return json.dumps({'message': 'no information for given date'}), 500

   data = json.load(f)
   games = []

   for game in data:
      obj = {}

      obj['taglines'] = game['taglines']
      obj['home'] = game['home']
      obj['away'] = game['away']
      obj['home_win'] = game['home_win']
      obj['home_loss'] = game['home_loss']
      obj['away_win'] = game['away_win']
      obj['away_loss'] = game['away_loss']
      obj['est_time'] = game['est_time']

      rank = 0
      for factor in game['rank_factors']['home']:
         rank += int(factor['rank'])
      for factor in game['rank_factors']['away']:
         rank += int(factor['rank'])
      obj['total_rank'] = str(rank)

      games.append(obj)

   return json.dumps(games), 200

@content_api.route("/getgame/<int:year>/<int:month>/<int:day>/<string:home>/<string:away>")
def getgame(year, month, day, home, away):
   curDate = date(year, month, day)

   if year == None or month == None or day == None:
      temp =  date.today()
      curDate = date(temp.year, temp.month, temp.day)

   try:
      f = open('./datastore/' + curDate.isoformat() + '.txt', 'r')
   except IOError:
      return json.dumps({'message': 'no information for given date'}), 500

   data = json.load(f)

   for game in data:
      if game['home'] == home and game['away'] == away:
         return json.dumps(game), 200

   return json.dumps({'message': 'game not found'}), 404
