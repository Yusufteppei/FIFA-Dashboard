import pandas as pd
import dash_bootstrap_components as dbc
import dash
from dash import dcc, html, Input, Output
import plotly.graph_objects as go
import plotly.express as px
from data import DATA, get_player_data, get_player_ovr

data = pd.read_csv('data.csv')


categories = list(DATA.columns[1:])



app = dash.Dash(external_stylesheets=[dbc.themes.DARKLY])

app.title="Player Mold Comparison"
app.layout = html.Div(
    className="container",
    children=[

    dbc.Row(
        id = 'header',
        style = {
            'padding': 30
        },
        children = [
            dbc.Col(

                children=[
                    html.Div(
                        className="text-dark",
                        children=[
                            dcc.Dropdown(options=list(data['short_name']), placeholder='Select Player', id = 'player-1', value='L. Messi')
                        ],
                    ),
                    
                    
                    
                ]
            ),
            dbc.Col(
                [
                    html.Div(
                        className="text-dark",
                        children=[
                            dcc.Dropdown(options=list(data['short_name']), placeholder='Select Player', id = 'player-2', value='Cristiano Ronaldo')
                        ],
                    ),

                   
                ]
            ),
        
        ]
    ),
    # GRAPH
    dbc.Row(
        id = 'chart',
        children = [
            
            dbc.Col(
                className="m-4",
                children = [
                    html.H3(id="ovr-1", className="text-center"),
                    dcc.Graph(
                        id='spider-1',
                    )
                ]
            ),
            
            dbc.Col(
                className="m-4",
                children = [
                    html.H3(id="ovr-2", className="text-center"),
                    dcc.Graph(
                        id='spider-2',
                    )
                ]
            ),
        
        ]
    )
])

@app.callback(
   [
        Output(component_id ='ovr-1', component_property='children'),
        Output(component_id ='ovr-2', component_property='children'),
        Output(component_id='spider-1', component_property='figure'),
        Output(component_id='spider-2', component_property='figure'),
        Input(component_id='player-2', component_property='value'),
        Input(component_id='player-1', component_property='value')
   ]
)
def func(value2, value1):
    data1 = [go.Scatterpolar(
      r=get_player_data(value1),
      theta=categories,
      fill='toself',
      name=value1
    )]

    data2 = [go.Scatterpolar(
      r=get_player_data(value2),
      theta=categories,
      fill='toself',
      name=value2
    )]

    return [

        f"OVR : {get_player_ovr(value1)}",
        f"OVR : {get_player_ovr(value2)}",
        {
            'data': data1,
            'layout': go.Layout(
                title=value1,
                paper_bgcolor='#2E3436',
                plot_bgcolor='#75507B',
                font={
                    'color': '#EEEEEC'
                },
            )
        },
        {
            'data': data2,
            'layout': go.Layout(
                title=value2,
                paper_bgcolor='#2E3436',
                plot_bgcolor='#75507B',
                font={
                    'color': '#EEEEEC'
                },
            )
        },

    ]



app.run_server(debug=True, use_reloader=True, port=8060)
