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

'''
    In this cell we create a var with type list for each team with the nexts paramas:
        - index[0] : Name of the team from the var team_lst
        - index[1] : Team id from the var team_id
        - index[2] : url of comuniate that give us almost of the data 
                    (Player name, Position, Season Points, Season Points Average, Value, On start average)
        - index[3] : Number of players in the squad.
        - index[4] : url of comuniazo that give us the points of the last 5 matchs of the each player on the squad
        - index[5] : url of espn that give us the matchs played, goals received (goalkeepers), goals, assists.
        
    Then we store all of the vars in a list to give it like a param to the main function.
    
'''

ath_b = [team_lst[0], team_id[0], 'https://www.comuniate.com/plantilla/1/athletic', 'https://www.comuniazo.com/comunio-apuestas/equipos/athletic', 'https://espndeportes.espn.com/futbol/equipo/plantel/_/id/93/esp.athletic_bilbao']
at_m = [team_lst[1], team_id[1], 'https://www.comuniate.com/plantilla/2/atletico', 'https://www.comuniazo.com/comunio-apuestas/equipos/atletico', 'https://espndeportes.espn.com/futbol/equipo/plantel/_/id/1068/esp.atletico_madrid']
osa = [team_lst[2], team_id[2], 'https://www.comuniate.com/plantilla/12/osasuna', 'https://www.comuniazo.com/comunio-apuestas/equipos/osasuna', 'https://espndeportes.espn.com/futbol/equipo/plantel/_/id/97/esp.osasuna']
rcd_esp = [team_lst[3], team_id[3], 'https://www.comuniate.com/plantilla/7/espanyol', 'https://www.comuniazo.com/comunio-apuestas/equipos/espanyol', 'https://espndeportes.espn.com/futbol/equipo/plantel/_/id/88/esp.espanyol']
barc = [team_lst[4], team_id[4], 'https://www.comuniate.com/plantilla/3/barcelona', 'https://www.comuniazo.com/comunio-apuestas/equipos/barcelona', 'https://espndeportes.espn.com/futbol/equipo/plantel/_/id/83/esp.barcelona']
geta = [team_lst[5], team_id[5], 'https://www.comuniate.com/plantilla/8/getafe', 'https://www.comuniazo.com/comunio-apuestas/equipos/getafe', 'https://espndeportes.espn.com/futbol/equipo/plantel/_/id/2922/esp.getafe']
grana = [team_lst[6], team_id[6], 'https://www.comuniate.com/plantilla/71/granada', 'https://www.comuniazo.com/comunio-apuestas/equipos/granada', 'https://espndeportes.espn.com/futbol/equipo/plantel/_/id/3747/esp.granada_cf']
r_mad = [team_lst[7], team_id[7], 'https://www.comuniate.com/plantilla/15/real-madrid', 'https://www.comuniazo.com/comunio-apuestas/equipos/real-madrid', 'https://espndeportes.espn.com/futbol/equipo/plantel/_/id/86/esp.real_madrid']
rayo = [team_lst[8], team_id[8], 'https://www.comuniate.com/plantilla/70/rayo-vallecano', 'https://www.comuniazo.com/comunio-apuestas/equipos/rayo-vallecano', 'https://espndeportes.espn.com/futbol/equipo/plantel/_/id/101/esp.rayo_vallecano']
leva = [team_lst[9], team_id[9], 'https://www.comuniate.com/plantilla/10/levante', 'https://www.comuniazo.com/comunio-apuestas/equipos/levante', 'https://espndeportes.espn.com/futbol/equipo/plantel/_/id/1538/esp.levante']
mall = [team_lst[10], team_id[10], 'https://www.comuniate.com/plantilla/11/mallorca', 'https://www.comuniazo.com/comunio-apuestas/equipos/mallorca', 'https://espndeportes.espn.com/futbol/equipo/plantel/_/id/84/esp.mallorca']
bet = [team_lst[11], team_id[1], 'https://www.comuniate.com/plantilla/4/betis', 'https://www.comuniazo.com/comunio-apuestas/equipos/betis', 'https://espndeportes.espn.com/futbol/equipo/plantel/_/id/244/esp.betis_sevilla']
r_soc = [team_lst[12], team_id[12], 'https://www.comuniate.com/plantilla/13/real-sociedad', 'https://www.comuniazo.com/comunio-apuestas/equipos/real-sociedad', 'https://espndeportes.espn.com/futbol/equipo/plantel/_/id/89/esp.real_sociedad']
villa = [team_lst[13], team_id[13], 'https://www.comuniate.com/plantilla/19/villarreal', 'https://www.comuniazo.com/comunio-apuestas/equipos/villarreal', 'https://espndeportes.espn.com/futbol/equipo/plantel/_/id/102/esp.villarreal']
val = [team_lst[14], team_id[14], 'https://www.comuniate.com/plantilla/18/valencia', 'https://www.comuniazo.com/comunio-apuestas/equipos/valencia', 'https://espndeportes.espn.com/futbol/equipo/plantel/_/id/94/esp.valencia']
alav = [team_lst[15], team_id[15], 'https://www.comuniate.com/plantilla/89/alaves', 'https://www.comuniazo.com/comunio-apuestas/equipos/alaves', 'https://espndeportes.espn.com/futbol/equipo/plantel/_/id/96/esp.alaves']
cadi = [team_lst[16], team_id[16], 'https://www.comuniate.com/plantilla/105/cadiz', 'https://www.comuniazo.com/comunio-apuestas/equipos/cadiz', 'https://espndeportes.espn.com/futbol/equipo/plantel/_/id/3842/esp.cadiz']
elch = [team_lst[17], team_id[17], 'https://www.comuniate.com/plantilla/75/elche', 'https://www.comuniazo.com/comunio-apuestas/equipos/elche', 'https://espndeportes.espn.com/futbol/equipo/plantel/_/id/3751/esp.elche']
celta = [team_lst[18], team_id[18], 'https://www.comuniate.com/plantilla/5/celta', 'https://www.comuniazo.com/comunio-apuestas/equipos/celta', 'https://espndeportes.espn.com/futbol/equipo/plantel/_/id/85/esp.celta_vigo']
sevil = [team_lst[19], team_id[19], 'https://www.comuniate.com/plantilla/17/sevilla', 'https://www.comuniazo.com/comunio-apuestas/equipos/sevilla', 'https://espndeportes.espn.com/futbol/equipo/plantel/_/id/243/esp.fc_sevilla']

teams_set = [ath_b, at_m, osa, rcd_esp, barc, geta, grana, r_mad, rayo, leva, mall, bet, r_soc, villa, val, alav, cadi,elch,celta, sevil]