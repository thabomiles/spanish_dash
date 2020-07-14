import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px

df = pd.read_excel(r"C:\Users\User\Documents\repos\dash_on_flask\app\dashapp1\uploads\venas_abiertas.xlsx")
df['len'] = df['words'].apply(lambda x: len(x))
df['known'] = df['known'].fillna('unidentified')
a = (df['len']>3).copy()

fig = px.bar(df[a].head(20).sort_values(by="count", ascending=True),  x="count",y="words", color='known', orientation='h')


layout = html.Div([
    html.H1('Stock Tickers'),
    dcc.Graph(figure=fig),
    dcc.Dropdown(
        id='my-dropdown',
        options=[
            {'label': 'Coke', 'value': 'COKE'},
            {'label': 'Tesla', 'value': 'TSLA'},
            {'label': 'Apple', 'value': 'AAPL'}
        ],
        value='COKE'
    ),
    #dcc.Graph(id='my-graph')
], style={'width': '500'})
