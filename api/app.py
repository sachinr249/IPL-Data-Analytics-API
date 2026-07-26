from flask import Flask,jsonify,request
import ipl

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World"

@app.route('/api/teams')
def teams():
    teams = ipl.teamsAPI()
    return jsonify(teams)

@app.route('/api/teamvteam')
def team_vs_team():
    team1 = request.args.get('team1')
    team2 = request.args.get('team2')
    response = ipl.team_vs_team_API(team1,team2)
    return jsonify(response)
@app.route('/api/AllTeamsRecord')
def team_recor():
    record = ipl.all_teams_record_API()
    return jsonify(record)

@app.route('/api/SeasonRecord')
def season_record():
    season = request.args.get('season')
    response = ipl.points_table_API(season)
    return jsonify(response)



app.run(debug=True)