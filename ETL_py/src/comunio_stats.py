import requests as req
import pandas as pd
from bs4 import BeautifulSoup as bs
from fuzzywuzzy import process, fuzz

def comunio_stats_fbref(team_lst, journey):
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
        - index[4] : url of FBREF that give us the matchs played, goals, assists.
    
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
            1 csv file with only stats from comunio
            1 csv file with only stats from fbref
            1 json file with only stats from comunio
            1 json file with only stats from fbref
    
    '''
    
    df_teams = pd.DataFrame()
    df_comunio = pd.DataFrame()
    df_fbref = pd.DataFrame()
    
    for team in team_lst:
        
        print(team[0])
        
        soup = bs(req.get(team[2]).text , 'html.parser') # soup from comuniate web
        soup2 = bs(req.get(team[3]).text , 'html.parser') # soup from comuniazo web
        soup3 = bs(req.get(team[4]).text , 'html.parser') # soup from fbref web
        
        num_players = soup.find_all('div', class_='col-md-12') # Firts count the players on the squad
        total_players = 0
        for i in range (2,6):
            # This loop sum the number of player for position on the squad
            total_players += len(num_players[i].find_all('div', 
                                                         class_='enlace2 ficha_jugador col-md-6 col-sm-6 col-xs-12'))
        
        players = total_players
        print(total_players)

        team_id = team[1]

        squad = team[0] # this line give us the name of the team
        
        # With this lines get the names of the playes
        #name = soup.find_all('strong') estas dos lineas dejaron de funcionar el 13 de enero de 2022
        #name = [name[i].text for i in range(22, (22 + players * 2), 2)]
        name = soup.find_all('span', class_='titulo_ficha_jugador')
        name = [name[i].text for i in range(players)]
        
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
        print(f'Nº jugadores en la web de comunio {len(df.Player)}')
        df.to_csv(f'data/pruebas/{squad}_comunio-stats_J{journey}.csv', index=False)
        df_comunio = df_comunio.append(df)
        
        # Second part of web scrapping to complete the stats table, with games played, goals, and assists

        players_stats = soup3.find('tbody')
    
        new_name = [' '.join(players_stats.find_all('tr')[i].text.split()[0:2])[:-2] if len(players_stats.find_all('tr')[i].text.split())>2
                    else ' '.join(players_stats.find_all('tr')[i].text.split()[0:1])[:-2] for i in range(len(players_stats.find_all('tr')))]
    
        new_pj = ['0' if players_stats.find_all('td', class_='right')[i].text == '' 
                   else players_stats.find_all('td', class_='right')[i].text 
                   for i in range (0,len(players_stats.find_all('td', class_='right')),25 )]

        new_goals = ['0' if players_stats.find_all('td', class_='right')[i].text == '' 
                   else players_stats.find_all('td', class_='right')[i].text 
                   for i in range (4,len(players_stats.find_all('td', class_='right')),25 )]

        new_assists = ['0' if players_stats.find_all('td', class_='right')[i].text == '' 
                   else players_stats.find_all('td', class_='right')[i].text 
                   for i in range (5,len(players_stats.find_all('td', class_='right')),25 )]
        
        pl_dict = {'Player': new_name, 'Matchs': new_pj, 'Goals': new_goals, 'Assists' : new_assists}

        df_stats = pd.DataFrame(pl_dict)
        
        print(f'Nº jugadores en la web de fbref {len(df_stats.Player)}')
        df_stats.to_csv(f'data/pruebas/{squad}_fbref-stats_J{journey}.csv', index=False)
        df_fbref = df_fbref.append(df_stats)
        
        # In this part of script we use the fuzzywuzzy lib to merge both dataframes.
        
        #This part compares both dataframes and returns a score of match in the serie that we want
        # In this case we compare the serie 'Player' of both dataframes
        df[['team_matched', 'fuzz_score']]=df_stats.Player.apply(lambda x:process.extractOne(x,
                                                                     df_stats.Player.tolist(),
                                                                     scorer=fuzz.partial_ratio)).apply(pd.Series)
        
        # merge the both daframes
        df=pd.merge(df, df_stats, left_on='team_matched', right_on='Player')
        
        # Create a new datafram only with the values of fuzzy score are greater than 75
        
        df_1=df[df.fuzz_score>75]
        
        #The next line drops the columns that not are necessary on dataframe
        df_1 = df_1.drop(columns = ['team_matched', 'fuzz_score', 'Player_y'])
        
        # Rename the columns to the value that we want
        df_1 = df_1.rename(columns = {'Player_x': 'Player'})
        
        # order columns of the data frame to give sense
        order_col = [0,1,2,3,15,7,16,17,4,5,8,9,10,11,12,13,14,6]
        
        # Sort the dataframe columns with the value that we want
        df_1 = df_1[df_1.columns[order_col]]
        
        df_teams = df_teams.append(df_1) # add the df of the team to the df of all teams
        
        df_1.to_csv(f'data/pruebas/{squad}_J{journey}.csv', index=False) # export df_team to a team file
    
    
    df_teams.to_json(f'data/pruebas/comunio_J{journey}.json', orient="table") # export df of all teams to json file
    df_teams.to_csv(f'data/pruebas/comunio_J{journey}.csv', index=False) # export df o all teams to csv file
    df_comunio.to_json(f'data/pruebas/only_comunio_stats_J{journey}.json', orient="table")
    df_fbref.to_json(f'data/pruebas/only_fbref_stats_J{journey}.json', orient="table")
    df_comunio.to_csv(f'data/pruebas/only_comunio_stats_J{journey}.csv', index=False)
    df_fbref.to_csv(f'data/pruebas/only_fbref_stats_J{journey}.csv', index=False)
    
    print('Jugadores en fbref ',len(df_fbref))
    print('Jugadores en comunio ',len(df_comunio))
    print('Jugadores en lista combinada ', len(df_teams))
    return 'Finished'