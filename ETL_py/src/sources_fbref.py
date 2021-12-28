import http.client
import json
import pandas as pd

# Firts we realice the connection to the API, with the instructions describes in its documentation.
connection = http.client.HTTPConnection('api.football-data.org')
headers = { 'X-Auth-Token': '2643e9e1f8624a75a8eb21f12ad5c0bf' } # personal token given by the API.
connection.request('GET', '/v2/competitions/PD/teams?season=2021', None, headers ) # request for teams names
response = json.loads(connection.getresponse().read().decode())['teams'] #
team_lst = [response[t]['name'] for t in range(len(response))] # create a list of the teams
team_id = [i for i in range(1,21)] # create a list to give an id to each team
df_teams = pd.DataFrame(team_lst, columns = ['Team']) # create a Data Frame with the teams.
df_teams.insert(0, 'Team_id', team_id) # add column id to the Data Frame
df_teams.to_csv('data/teams20-21.csv', index=False) # export df to a csv file.

#equipos con nueva fuente de datos fbref
'''
    In this cell we create a var with type list for each team with the nexts paramas:
        - index[0] : Name of the team from the var team_lst
        - index[1] : Team id from the var team_id
        - index[2] : url of comuniate that give us almost of the data 
                    (Player name, Position, Season Points, Season Points Average, Value, On start average)
        - index[3] : url of comuniazo that give us the points of the last 5 matchs of the each player on the squad
        - index[4] : url of fbref that give us the matchs played, goals, goals, assists.
        
    Then we store all of the vars in a list to give it like a param to the main function.
    
'''
ath_b_fbref = [team_lst[0], team_id[0], 'https://www.comuniate.com/plantilla/1/athletic', 'https://www.comuniazo.com/comunio-apuestas/equipos/athletic', 'https://fbref.com/es/equipos/2b390eca/Estadisticas-de-Athletic-Club']
at_m_fbref = [team_lst[1], team_id[1], 'https://www.comuniate.com/plantilla/2/atletico', 'https://www.comuniazo.com/comunio-apuestas/equipos/atletico', 'https://fbref.com/es/equipos/db3b9613/Estadisticas-de-Atletico-Madrid']
osa_fbref = [team_lst[2], team_id[2], 'https://www.comuniate.com/plantilla/12/osasuna', 'https://www.comuniazo.com/comunio-apuestas/equipos/osasuna', 'https://fbref.com/es/equipos/03c57e2b/Estadisticas-de-Osasuna']
rcd_esp_fbref = [team_lst[3], team_id[3], 'https://www.comuniate.com/plantilla/7/espanyol', 'https://www.comuniazo.com/comunio-apuestas/equipos/espanyol', 'https://fbref.com/es/equipos/a8661628/Estadisticas-de-Espanyol']
barc_fbref = [team_lst[4], team_id[4], 'https://www.comuniate.com/plantilla/3/barcelona', 'https://www.comuniazo.com/comunio-apuestas/equipos/barcelona', 'https://fbref.com/es/equipos/206d90db/Estadisticas-de-Barcelona']
geta_fbref = [team_lst[5], team_id[5], 'https://www.comuniate.com/plantilla/8/getafe', 'https://www.comuniazo.com/comunio-apuestas/equipos/getafe', 'https://fbref.com/es/equipos/7848bd64/Estadisticas-de-Getafe']
grana_fbref = [team_lst[6], team_id[6], 'https://www.comuniate.com/plantilla/71/granada', 'https://www.comuniazo.com/comunio-apuestas/equipos/granada', 'https://fbref.com/es/equipos/a0435291/Estadisticas-de-Granada']
r_mad_fbref = [team_lst[7], team_id[7], 'https://www.comuniate.com/plantilla/15/real-madrid', 'https://www.comuniazo.com/comunio-apuestas/equipos/real-madrid', 'https://fbref.com/es/equipos/53a2f082/Estadisticas-de-Real-Madrid']
rayo_fbref = [team_lst[8], team_id[8], 'https://www.comuniate.com/plantilla/70/rayo-vallecano', 'https://www.comuniazo.com/comunio-apuestas/equipos/rayo-vallecano', 'https://fbref.com/es/equipos/98e8af82/Estadisticas-de-Rayo-Vallecano']
leva_fbref = [team_lst[9], team_id[9], 'https://www.comuniate.com/plantilla/10/levante', 'https://www.comuniazo.com/comunio-apuestas/equipos/levante', 'https://fbref.com/es/equipos/9800b6a1/Estadisticas-de-Levante']
mall_fbref = [team_lst[10], team_id[10], 'https://www.comuniate.com/plantilla/11/mallorca', 'https://www.comuniazo.com/comunio-apuestas/equipos/mallorca', 'https://fbref.com/es/equipos/2aa12281/Estadisticas-de-Mallorca']
bet_fbref = [team_lst[11], team_id[1], 'https://www.comuniate.com/plantilla/4/betis', 'https://www.comuniazo.com/comunio-apuestas/equipos/betis', 'https://fbref.com/es/equipos/fc536746/Estadisticas-de-Real-Betis']
r_soc_fbref = [team_lst[12], team_id[12], 'https://www.comuniate.com/plantilla/13/real-sociedad', 'https://www.comuniazo.com/comunio-apuestas/equipos/real-sociedad', 'https://fbref.com/es/equipos/e31d1cd9/Estadisticas-de-Real-Sociedad']
villa_fbref = [team_lst[13], team_id[13], 'https://www.comuniate.com/plantilla/19/villarreal', 'https://www.comuniazo.com/comunio-apuestas/equipos/villarreal', 'https://fbref.com/es/equipos/2a8183b3/Estadisticas-de-Villarreal']
val_fbref = [team_lst[14], team_id[14], 'https://www.comuniate.com/plantilla/18/valencia', 'https://www.comuniazo.com/comunio-apuestas/equipos/valencia', 'https://fbref.com/es/equipos/dcc91a7b/Estadisticas-de-Valencia']
alav_fbref = [team_lst[15], team_id[15], 'https://www.comuniate.com/plantilla/89/alaves', 'https://www.comuniazo.com/comunio-apuestas/equipos/alaves', 'https://fbref.com/es/equipos/8d6fd021/Estadisticas-de-Alaves']
cadi_fbref = [team_lst[16], team_id[16], 'https://www.comuniate.com/plantilla/105/cadiz', 'https://www.comuniazo.com/comunio-apuestas/equipos/cadiz', 'https://fbref.com/es/equipos/ee7c297c/Estadisticas-de-Cadiz']
elch_fbref = [team_lst[17], team_id[17], 'https://www.comuniate.com/plantilla/75/elche', 'https://www.comuniazo.com/comunio-apuestas/equipos/elche', 'https://fbref.com/es/equipos/6c8b07df/Estadisticas-de-Elche']
celta_fbref = [team_lst[18], team_id[18], 'https://www.comuniate.com/plantilla/5/celta', 'https://www.comuniazo.com/comunio-apuestas/equipos/celta', 'https://fbref.com/es/equipos/f25da7fb/Estadisticas-de-Celta-Vigo']
sevil_fbref = [team_lst[19], team_id[19], 'https://www.comuniate.com/plantilla/17/sevilla', 'https://www.comuniazo.com/comunio-apuestas/equipos/sevilla', 'https://fbref.com/es/equipos/ad2be733/Estadisticas-de-Sevilla']
teams_set_fbref = [ath_b_fbref, at_m_fbref, osa_fbref, rcd_esp_fbref, barc_fbref, geta_fbref, grana_fbref, r_mad_fbref, rayo_fbref, leva_fbref, mall_fbref, bet_fbref, r_soc_fbref, villa_fbref, val_fbref, 
                   alav_fbref, cadi_fbref,elch_fbref,celta_fbref, sevil_fbref]