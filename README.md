# WorldSeries2016_API
MLBAM Hackathon of Champions

This is the complement to the WorldSeries2016 repository. That code saves a
flat file to this repository's `datastore`. In that file is a JSON array of
relevant information we use to determine how to rank each baseball game for
the day and lists of factors that go into that computation. 

The API provides a few simple endpoints:
* `/getgames/<year>/<month>/<day>`: gets the games for the day and meta data about those games
* `/getgame/<year>/<month>/<day>/<homeTeamAbbrev>/<awayTeamAbbrev>`: gets an individual games data

Sadly we didn't have access to any databases so we treated the JSON array as our datastore,
the endpoints cut that up appropriately and send back the result. 

Example calls:
* `/getgames/2016/06/16`: gets all games (and meta data) for June 16th, 2016
* `/getgame/2016/06/16/MIN/NYY`: get Yankees @ Twins gameday prediction data on June 16th, 2016

By: Jon Catanio
