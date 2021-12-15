import requests as req
import pandas as pd
from bs4 import BeautifulSoup as bs
from fuzzywuzzy import process, fuzz

def comunio_stats(team_lst, journey):
    '''
    Description.
    ------------
    
    With this function we want to obtain a dataset from diferents sources with the stadistics of all players of
    La Liga, to value its performance across the season.
    
    Params.
    -------
    
    The function receives a list with the teams of La Liga, and a the  journey's match.
    The team from teams_lst is a list with some variables:
        
        - index[0] : Name of the team from the var team_lst
        - index[1] : Team id from the var team_id
        - index[2] : url of comuniate that give us almost of the data 
                    (Player name, Position, Season Points, Season Points Average, Value, On start average)
        - index[3] : url of comuniazo that give us the points of the last 5 matchs of the each player on the squad
        - index[4] : url of espn that give us the matchs played, goals received (goalkeepers), goals, assists.
    
    Journey's Macht only works from actually journey to future journeys (we can't obtains data from past journeys with this script)
    
    Returns.
    --------
        Prints the name of the team with each iteration.
        When script finish , returns 'Finished'
        Store in 'data' directory this files:
        
            1 csv file with teams of La Liga, 'data/teams.csv'.
            1 csv file with the player's squad for each team, 'data/team_name_J_number_of_journey.csv'.
            1 csv file with all the player's stats of La Liga.
            1 json file with all the player's stats of La Liga.
    
    '''
    
    df_teams = pd.DataFrame()
    
    for team in team_lst:
        
        print(team[0])
        
        soup = bs(req.get(team[2]).text , 'html.parser') # soup from comuniate web
        soup2 = bs(req.get(team[3]).text , 'html.parser') # soup from comuniazo web
        soup3 = bs(req.get(team[4]).text , 'html.parser') # soup from espn web

        num_players = soup.find_all('div', class_='col-md-12') # Firts count the players on the squad
        total_players = 0
        for i in range (2,6):
            # This loop sum the number of player for position on the squad
            total_players += len(num_players[i].find_all('div', 
                                                         class_='enlace2 ficha_jugador col-md-6 col-sm-6 col-xs-12'))
        
        players = total_players

        team_id = team[1]

        squad = team[0] # this line give us the name of the team
        
        # With this lines get the names of the playes
        name = soup.find_all('strong')
        name = [name[i].text for i in range(22, (22 + players * 2), 2)]
        
        # With this lines we want to get the position of the players
        pos_gk = soup.find_all('span', class_='label-posicion label-success')
        gks = [pos_gk[i].text.strip() for i in range(len(pos_gk))]

        pos_df = soup.find_all('span', class_='label-posicion label-info')
        dfs = [pos_df[i].text.strip() for i in range(len(pos_df))]

        pos_md = soup.find_all('span', class_='label-posicion label-warning')
        mds = [pos_md[i].text.strip() for i in range(len(pos_md))]

        pos_fw = soup.find_all('span', class_='label-posicion label-danger')
        fws = [pos_fw[i].text.strip() for i in range(len(pos_fw))]
    
        # Create an unique array for the positions of the players for arrays of the same length
        all_pos = gks + dfs + mds + fws
        
        # This lines get the total points on the season of the players
        pts = soup.find_all('span', class_='texto_pequenio2 label-posicion label-primary')
        pt = [pts[i].text for i in range(len(pts))]
        
        # This lines get the fantasy market value of the players
        values = soup.find_all('small')
        value = [values[i].text.split('€')[0].replace('.','') for i in range(0,len(values),3)]
        
        # This line get the average points of the players along the season
        pt_avg = [values[i].text.split()[-1] for i in range(1,len(values),3)]
        
        # This line get the percentage of the games that player are on the initial 11
        on_start_per = [values[i].text.split('%')[0] for i in range(2,len(values),3)]
        
        # With this line get a list of the points in the last five matchs
        points = soup2.find_all('div', class_='streak')
        pts_last_five_jouyneys = [points[i].text.split() for i in range(len(points))] 
        
        # Create variables to get a single value for each game of the last five games
        jback5 = []
        jback4 = []
        jback3 = []
        jback2 = []
        jback1 = []
        avg_last_5 = []
        
        # in this loop we iterate on each index of each list from pts_last_five_journeys to store the points
        # in an individual var and change type of this var to int for calculate the avg of the last 5 games
        # if the player have a '-' simbol we give o points, he don't play but we use 0 to calculate de avg
        
        for i, ptos in enumerate(pts_last_five_jouyneys):
            
            avg = 0
            
            if pts_last_five_jouyneys[i][0] == '-':
                jback5.append(0)
            else:
                jback5.append(int(pts_last_five_jouyneys[i][0]))
                avg += int(pts_last_five_jouyneys[i][0])
            
            if pts_last_five_jouyneys[i][1] == '-':
                jback4.append(0)
            else:
                jback4.append(int(pts_last_five_jouyneys[i][1]))
                avg += int(pts_last_five_jouyneys[i][1])
            
            if pts_last_five_jouyneys[i][2] == '-':
                jback3.append(0)
            else:
                jback3.append(int(pts_last_five_jouyneys[i][2]))
                avg += int(pts_last_five_jouyneys[i][2])
            
            if pts_last_five_jouyneys[i][3] == '-':
                jback2.append(0)
            else:
                jback2.append(int(pts_last_five_jouyneys[i][3]))
                avg += int(pts_last_five_jouyneys[i][3])
            
            if pts_last_five_jouyneys[i][4] == '-':
                jback1.append(0)
            else:
                jback1.append(int(pts_last_five_jouyneys[i][4]))
                avg += int(pts_last_five_jouyneys[i][4])

            avg_last_5.append(avg/5)        


        journey = journey
        
        # Create a dictionary to store stats from each player on each iteration
        
        team = {'Team_id': team_id, 
                'Team': squad, 
                'Player': name,
                'Position': all_pos,
                'Total_Points': pt,
                'Points_Average': pt_avg,
                'Value': value,
                'On_start_%': on_start_per,
                'Last_5_games_points': pts_last_five_jouyneys,
                f'J_{journey - 4}': jback5,
                f'J_{journey - 3}': jback4,
                f'J_{journey - 2}': jback3,
                f'J_{journey - 1}': jback2,
                f'J_{journey}': jback1,
                'Avg_last_5_games': avg_last_5}
        
        df = pd.DataFrame(team)
        
        # Second part of web scrapping to complete the stats table, with games played, goals or goal received(gk), and assists

        goalkeepers = soup3.find('div', class_='Table__Scroller')
        goalkeepers_rows = goalkeepers.find_all('tr')
        goalkeepers_stats = [[e.text for e in goalkeepers_rows[i].find_all('td')] for i in range(1,len(goalkeepers_rows))]

        team_squad = soup3.find_all('div', class_='Table__Scroller')
        team_squad_rows = team_squad[1].find_all('tr')
        team_squad_stats = [[e.text for e in team_squad_rows[i].find_all('td')] for i in range(1,len(team_squad_rows))]
        
        # In this list we store two dictionaries with others stats to merge with the previous dictionarie
        
        pl_lst = []

        for i, player in enumerate(goalkeepers_stats):
            
            name = ''.join([e for e in goalkeepers_stats[i][0] if e.isalpha() or e == ' '])
            
            if player[6] == '--': # this conditionals are for clean this serie and give correct type
                matches = 0
            else:
                matches = player[6]
            
            if player[9] == '--':
                goals_received = 0
            else:
                goals_received = player[9]
            
            if player[10] == '--':
                assists = 0
            else:
                assists = player[10]


            gk_dict = {'Player': name, 'Matches_Played': matches, 'Goals_/_Goals_Received': goals_received, 'Assists' : assists}
            pl_lst.append(gk_dict)

        for i, player in enumerate(team_squad_stats):
            
            name = ''.join([e for e in team_squad_stats[i][0] if e.isalpha() or e == ' '])
            
            if player[6]=='--':# this conditionals are for clean this serie and give correct type
                matches = 0
            else:
                matches = player[6]
            
            if player[8] == '--':
                goals = 0
            else:
                goals = player[8]
            
            if player[9] == '--':
                assists = 0
            else:
                assists = player[9]


            pl_dict = {'Player': name, 'Matches_Played': matches, 'Goals_/_Goals_Received': goals, 'Assists' : assists}
            pl_lst.append(pl_dict)
        
        df_stats = pd.DataFrame(pl_lst)
        
        # In this part of script we use the fuzzywuzzy lib to merge both dataframes.
        
        #This part compares both dataframes and returns a score of match in the serie that we want
        # In this case we compare the serie 'Player' of both dataframes
        df[['team_matched', 'fuzz_score']]=df.Player.apply(lambda x:process.extractOne(x,
                                                                     df_stats.Player.tolist(),
                                                                     scorer=fuzz.partial_ratio)).apply(pd.Series)
        
        # merge the both daframes
        df=pd.merge(df, df_stats, left_on='team_matched', right_on='Player')
        
        # Create a new datafram only with the values of fuzzy score are greater than 85
        df_1=df[df.fuzz_score>85]
        
        #The next line drops the columns that not are necessary on dataframe
        df_1 = df_1.drop(columns = ['team_matched', 'fuzz_score', 'Player_y'])
        
        # Rename the columns to the value that we want
        df_1 = df_1.rename(columns = {'Player_x': 'Player'})
        
        # order columns of the data frame to give sense
        order_col = [0,1,2,3,15,7,16,17,4,5,8,9,10,11,12,13,14,6]
        
        # Sort the dataframe columns with the value that we want
        df_1 = df_1[df_1.columns[order_col]]
        
        df_teams = df_teams.append(df_1) # add the df of the team to the df of all teams
        
        df_1.to_csv(f'./data/{squad}_J{journey}.csv', index=False) # export df_team to a team file
    
    
    df_teams.to_json(f'./data/comunio_J{journey}.json', orient="table") # export df of all teams to json file
    df_teams.to_csv(f'./data/comunio_J{journey}.csv', index=False) # export df o all teams to csv file
    
    return 'Finished'