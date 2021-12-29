import requests as req
import pandas as pd
from bs4 import BeautifulSoup as bs

def classification(journey):
    soup5 = bs(req.get('https://fbref.com/es/comps/12/Estadisticas-de-La-Liga').text, 'html.parser')
    
    clas_liga = soup5.find('tbody')
    pos = [clas_liga.find_all('th')[i].text for i in range(len(clas_liga.find_all('th')))]
    team = [clas_liga.find_all('td', class_='left')[i].text for i in range(0,len(clas_liga.find_all('td', class_='left')),3)]
    pj = [clas_liga.find_all('td', class_='right')[i].text for i in range(0,len(clas_liga.find_all('td', class_='right')),15)]
    pg = [clas_liga.find_all('td', class_='right')[i].text for i in range(1,len(clas_liga.find_all('td', class_='right')),15)]
    pe = [clas_liga.find_all('td', class_='right')[i].text for i in range(2,len(clas_liga.find_all('td', class_='right')),15)]
    pp = [clas_liga.find_all('td', class_='right')[i].text for i in range(3,len(clas_liga.find_all('td', class_='right')),15)]
    gf = [clas_liga.find_all('td', class_='right')[i].text for i in range(4,len(clas_liga.find_all('td', class_='right')),15)]
    gc = [clas_liga.find_all('td', class_='right')[i].text for i in range(5,len(clas_liga.find_all('td', class_='right')),15)]
    dg = [clas_liga.find_all('td', class_='right')[i].text for i in range(6,len(clas_liga.find_all('td', class_='right')),15)]
    pts = [clas_liga.find_all('td', class_='right')[i].text for i in range(7,len(clas_liga.find_all('td', class_='right')),15)]

    clas_tab = {'Position': pos, 'Team': team, 'Games': pj, 'Won': pg, 'Draw': pe, 'Lost': pp, 'Goals S.': gf, 'Goals R.': gc, 'GD': dg, 'PTS': pts}
    
    clas_df = pd.DataFrame(clas_tab)
    
    clas_df.to_excel(f'data/classification_J_{journey}.xlsx', sheet_name=f'classification_J_{journey}')
    
    return 'Classification done'