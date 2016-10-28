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
      f = open('./' + curDate.isoformat() + '.txt', 'r')
   except IOError:
      return json.dumps({'message': 'no information for given date'}), 500

   return json.dumps(json.load(f)), 200
