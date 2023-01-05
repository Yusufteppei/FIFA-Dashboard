import pandas as pd

df = pd.read_csv('data.csv')

DATA = df[['short_name','mentality','attacking','power','defending','skill','movement', 'overall']]

def get_player_data(player_short_name):
    data = DATA.loc[DATA['short_name'] == player_short_name]
    
    #d = [data['mentality'], data['attacking'], data['power'], data['defending'], data['skill'], data['movement']]
    print("Data : ", data)
    print(list(data.iloc[0][1:7]))
    d = data.iloc[0][1:7]
    return d

def get_player_ovr(player_short_name):
    data = DATA.loc[DATA['short_name'] == player_short_name]
    
    #d = [data['mentality'], data['attacking'], data['power'], data['defending'], data['skill'], data['movement']]
    #print("Data : ", data)
    #print(list(data.iloc[0][1:7]))
    d = data.iloc[0][-1]
    return d
    get_player_data('L. Messi')