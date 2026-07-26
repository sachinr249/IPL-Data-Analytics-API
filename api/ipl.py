import pandas as pd
import numpy as np

ipl = pd.read_csv('ipl-matches.csv')

#teams
def teamsAPI():
    teams = list(set(list(ipl['Team1']) + list(ipl['Team2'])))
    team_dict = {'teams': teams}
    return team_dict

def team_vs_team_API(team1,team2):
    new_data = ipl[(((ipl['Team1']==team1) & (ipl['Team2']==team2)) | ((ipl['Team2']==team1) & (ipl['Team1']==team2)))]
    total_matches = new_data.shape[0]
    win_by_team1 = new_data[new_data['WinningTeam']==team1].shape[0]
    win_by_team2 = new_data[new_data['WinningTeam']==team2].shape[0]
    draw = win_by_team1-win_by_team2
    mom = new_data['Player_of_Match'].value_counts().sort_values(ascending=False).head(1).index[0]
    result_dict = {'Total Matches': (total_matches),
                   team1:(win_by_team1),
                   team2:(win_by_team2),
                   'Draw':(draw),
                   'Most player of match winner':mom
                   }
    return result_dict

def all_teams_record_API():
    teams =ipl['Team1'].unique()
    dict_result = {}
    for team in teams:
        team_match = ipl[((ipl['Team1'] == team) | (ipl['Team2'] == team))]
        #No result
        no_result_matches = team_match[(team_match['WonBy'] == 'NoResults')].shape[0]
         #matches played by team
        total_matches = team_match.shape[0] - no_result_matches
        #woned by team
        win_mathces = team_match[(team_match['WinningTeam']==team)].shape[0]
        #Home_wins (Team1 is at Home)
        home_win = team_match[((team_match['WinningTeam']==team) & (team_match['Team1']==team))].shape[0]
        #Percentage
        win_per = (win_mathces/total_matches)*100
        home_win_per = (home_win/total_matches)*100
        away_win_per = 100 - home_win_per
    
        dict_result[team] = {
            'Total Matches Played':total_matches,
            'Winning Percentage': round(win_per,2),
            'Winning Percentage at Home' : round(home_win_per,2),
            'Winning Percentage Away From Home' : round(away_win_per,2)
        }

    return dict_result

def points_table_API(season):

    season_df = ipl[ipl['Season']==season]
    teams_name = list(set(list(season_df['Team1']) + list(season_df['Team2'])))
    result_dict = {}

    for team in teams_name:
        T_matches_played_team = int((season_df['Team1'] == team).sum() + (season_df['Team2']==team).sum())
        matches_won = int((season_df['WinningTeam']==team).sum())
        no_result = int((season_df['WonBy']=='NoResults').sum())
        points = matches_won*2 + no_result*1
        
        result_dict[team]={
            'Matches Played': T_matches_played_team,
            'Matches Won' : matches_won,
            'NO Result Matches':no_result,
            'Points':points
        }

    return result_dict