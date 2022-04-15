import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from xgboost import XGBRegressor
from sklearn.ensemble import GradientBoostingRegressor



class comunio_pred_lib():
    
    def create_df(journey):
        comunio = pd.read_csv(f'../data/pruebas/only_comunio_stats_J{journey}.csv')
        clas = pd.read_excel(f'../data/classification_J_{journey}.xlsx', sheet_name=f'classification_J_{journey}', index_col='Unnamed: 0')
        cal = pd.read_csv('../data/pruebas/Season_21-22.csv')
        
        teams_dict = {'Athletic Club': 'Athletic Club' ,
                    'CA Osasuna':'Osasuna',
                    'Club Atlético de Madrid':'Atlético Madrid',
                    'Cádiz CF':'Cádiz',
                    'Deportivo Alavés':'Alavés',
                    'Elche CF':'Elche',
                    'FC Barcelona':'Barcelona',
                    'Getafe CF':'Getafe',
                    'Granada CF':'Granada',
                    'Levante UD':'Levante',
                    'RC Celta de Vigo':'Celta Vigo',
                    'RCD Espanyol de Barcelona':'Espanyol',
                    'RCD Mallorca':'Mallorca',
                    'Rayo Vallecano de Madrid':'Rayo Vallecano',
                    'Real Betis Balompié':'Betis',
                    'Real Madrid CF':'Real Madrid',
                    'Real Sociedad de Fútbol':'Real Sociedad',
                    'Sevilla FC':'Sevilla',
                    'Valencia CF':'Valencia',
                    'Villarreal CF':'Villarreal'}
        
        new_team_name = []
        for team in comunio.Team:
    
            for k,v in teams_dict.items():
        
                if k == team:
            
                    new_team_name.append(v)
        
        comunio['Team'] = new_team_name
        
        points_per_team = comunio.groupby('Team').sum().reset_index()
        points_per_team= points_per_team.rename(columns={'Total_Points': 'Squad_Points',
                                                        'Points_Average': 'Squad_Average_Points',
                                                        'Avg_last_5_games': 'Squad_Avg_last_5_Games',
                                                        'Value': 'Value_Squad',
                                                        f'J_{journey -4}': f'Squad_Points_J_{journey -4}',
                                                        f'J_{journey -3}': f'Squad_Points_J_{journey -3}',
                                                        f'J_{journey -2}': f'Squad_Points_J_{journey -2}',
                                                        f'J_{journey -1}': f'Squad_Points_J_{journey -1}',
                                                        f'J_{journey}': f'Squad_Points_J_{journey}',})
        
        points_per_team = points_per_team.drop(['Team_id','On_start_%'], axis=1)
        
        df_1 = comunio.merge(points_per_team, how='left', left_on='Team', right_on='Team')
        
        matches_J = cal.loc[cal['Journey'] == (journey+1)]
        matches_J
        
        vs = []
        for team in df_1.Team:

            for index in matches_J.index:
            
                if team == matches_J.loc[index].Home:
                
                    vs.append(matches_J.loc[index].Away)
                    
                if team == matches_J.loc[index].Away:
                    
                    vs.append(matches_J.loc[index].Home)
        
        df_1['vs'] = vs
        
        points_per_vs_team = comunio.groupby('Team').sum().reset_index()
        points_per_vs_team= points_per_vs_team.rename(columns={'Total_Points': 'Vs_Squad_Points',
                                                            'Team':'Vs_Team',
                                                            'Points_Average': 'Vs_Squad_Average_Points',
                                                            'Avg_last_5_games': 'Vs_Squad_Avg_last_5_Games',
                                                            'Value':'Vs_Value_Squad',
                                                            f'J_{journey -4}': f'Vs_Squad_Points_J_{journey -4}',
                                                            f'J_{journey -3}': f'Vs_Squad_Points_J_{journey -3}',
                                                            f'J_{journey -2}': f'Vs_Squad_Points_J_{journey -2}',
                                                            f'J_{journey -1}': f'Vs_Squad_Points_J_{journey -1}',
                                                            f'J_{journey}': f'Vs_Squad_Points_J_{journey}',})
        
        points_per_vs_team = points_per_vs_team.drop(['Team_id','On_start_%'], axis=1)
        
        df_2 = df_1.merge(points_per_vs_team, how='left', left_on='vs', right_on='Vs_Team')
        
        team_clas = []

        for team in comunio.Team:
            for index in clas.index:
                
                if team in clas.loc[index].Team:
                    
                    team_clas.append(clas.loc[index].Position)
        
        team_clas_vs = []

        for team in df_2.Vs_Team:
            for index in clas.index:
            
                if team in clas.loc[index].Team:
                    
                    team_clas_vs.append(clas.loc[index].Position)
        
        df_2['Team_clas'] = team_clas
        df_2['Vs_Team_clas'] = team_clas_vs
        
        
        return df_2.drop('Team_id', axis=1)
    
    def preprocess_data(train,target,journey):
        j_target = target[['Player',f'J_{journey}']]
        j_target= j_target.rename(columns={'Player': 'Jugador', f'J_{journey}':'Target'})
        df= train.merge(j_target, how='left', left_on='Player', right_on='Jugador')
        df = df.dropna()
        X = df.drop(['Target'], axis=1)._get_numeric_data()
        y = df.Target
        
                    
        return X, y
    
    
    def predict_rf(data):
        train = comunio_pred_lib.create_df(30)
        target = comunio_pred_lib.create_df(31)
        rf = RandomForestRegressor()
        X,y = comunio_pred_lib.preprocess_data(train,target,31)
        
        X_train, X_test, y_train, y_test = train_test_split(X,y, random_state=42)
                
        rf.fit(X_train,y_train)
        
        print('RF MSE en test',mean_squared_error(y_test, rf.predict(X_test)))
        
        rf.fit(X,y)
        
        data = pd.DataFrame(data)._get_numeric_data()
        
        pred = rf.predict(data)
        
        return pred
    
    def predict_xgb(data):
        train = comunio_pred_lib.create_df(30)
        target = comunio_pred_lib.create_df(31)
        xgb = XGBRegressor()
        X,y = comunio_pred_lib.preprocess_data(train,target,31)
        
        X_train, X_test, y_train, y_test = train_test_split(X,y, random_state=42)
                
        xgb.fit(X_train,y_train)
        
        print('XGB MSE en test', mean_squared_error(y_test, xgb.predict(X_test)))
        
        xgb.fit(X,y)
        
        data = pd.DataFrame(data)._get_numeric_data()
        
        pred = xgb.predict(data)
        
        return pred
    
    def predict_gb(data):
        train = comunio_pred_lib.create_df(30)
        target = comunio_pred_lib.create_df(31)
        gb = GradientBoostingRegressor()
        X,y = comunio_pred_lib.preprocess_data(train,target,31)
        
        X_train, X_test, y_train, y_test = train_test_split(X,y, random_state=42)
                
        gb.fit(X_train,y_train)
        
        print('GB MSE en test', mean_squared_error(y_test, gb.predict(X_test)))
        
        gb.fit(X,y)
        
        data = pd.DataFrame(data)._get_numeric_data()
        
        pred = gb.predict(data)
        
        return pred