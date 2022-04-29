import pandas as pd
import pickle


class comunio_pred_lib():
    
    def create_df(journey):
        comunio = pd.read_csv(f'../data/pruebas/only_comunio_stats_J{journey}.csv')
        clas = pd.read_excel(f'../data/classification_J_{journey}.xlsx', 
                             sheet_name=f'classification_J_{journey}', index_col='Unnamed: 0')
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
    
    def preprocess_data(df):
    
        X = df.drop(['Target'], axis=1)._get_numeric_data()
        y = df.Target

        x_scaler = MinMaxScaler()
        y_scaler = MinMaxScaler()

        X_train, X_test, y_train, y_test = train_test_split(X,y, random_state=42)

        X_train_s = x_scaler.fit_transform(X_train)
        X_test_s = x_scaler.transform(X_test)

        y_train_s = y_scaler.fit_transform(y_train.values.reshape(-1,1))
        y_test_s = y_scaler.transform(y_test.values.reshape(-1,1))

        return X, y, X_train, X_test, y_train, y_test ,X_train_s, X_test_s, y_train_s, y_test_s, x_scaler, y_scaler
    
    
    def predict_rf(data):
        model = pickle.load(open('comunio_rfr.model', 'rb'))
        
        data = pd.DataFrame(data)._get_numeric_data()
        
        pred = model.predict(data)
        
        return pred
    
    def predict_xgb(data):
        model = pickle.load(open('comunio_xgbr.model', 'rb'))
        
        data = pd.DataFrame(data)._get_numeric_data()
        
        pred = model.predict(data)
        
        return pred
    
    def predict_gb(data):
        model = pickle.load(open('comunio_gb.model', 'rb'))
        
        data = pd.DataFrame(data)._get_numeric_data()
        
        pred = model.predict(data)
        
        return pred
    
    def predict_rnn(data, x_scaler, y_scaler):
        model = pickle.load(open('comunio_rnn.model', 'rb'))
        
        data = pd.DataFrame(data)._get_numeric_data()
        
        pred = y_scaler.inverse_transform(model.predict(x_scaler.transform(data)))
        
        return pred
    
    def predict_rnn2(data, x_scaler, y_scaler):
        model = pickle.load(open('comunio_rnn_2.model', 'rb'))
        
        data = pd.DataFrame(data)._get_numeric_data()
        
        pred = y_scaler.inverse_transform(model.predict(x_scaler.transform(data)))
        
        return pred