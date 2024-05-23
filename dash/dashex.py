import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

# Load the CSV file
df = pd.read_csv(r'C:\Users\reyha\Desktop\ilkcsv.csv')

# Exclude the 'City' column from X and Y axis dropdown options
columns = [col for col in df.columns if col != 'City']

# Create the Dash application
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Define the application layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1("Real Estate Analysis"),
            dcc.Dropdown(
                id='city-dropdown',
                options=[{'label': city, 'value': city} for city in df['City'].unique()],
                placeholder="Choose city",
            ),
        ], width=4),
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Dropdown(
                id='x-axis-dropdown',
                options=[{'label': col, 'value': col} for col in columns],
                placeholder="Select column for X axis",
            ),
        ], width=4),
        dbc.Col([
            dcc.Dropdown(
                id='y-axis-dropdown',
                options=[{'label': col, 'value': col} for col in columns],
                placeholder="Select column for Y axis (optional)",
            ),
        ], width=4),
        dbc.Col([
            dcc.Dropdown(
                id='plot-type-dropdown',
                options=[
                    {'label': 'Histogram', 'value': 'histogram'},
                    {'label': 'Scatter Plot', 'value': 'scatter'},
                    {'label': 'Box Plot', 'value': 'box'},
                    {'label': 'Bar Plot', 'value': 'bar'},
                    {'label': 'Line Plot', 'value': 'line'},
                    {'label': 'Pie Chart', 'value': 'pie'},
                    {'label': 'Violin Plot', 'value': 'violin'}
                ],
                placeholder="Choose plot type",
            ),
        ], width=4),
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='feature-graph'),
        ], width=12),
    ]),
])

# Define the callback function
@app.callback(
    Output('feature-graph', 'figure'),
    [Input('city-dropdown', 'value'),
     Input('x-axis-dropdown', 'value'),
     Input('y-axis-dropdown', 'value'),
     Input('plot-type-dropdown', 'value')]
)
def update_graph(selected_city, x_col, y_col, plot_type):
    if selected_city:
        filtered_df = df[df['City'] == selected_city]
    else:
        filtered_df = df

    if plot_type and x_col:
        if plot_type == 'histogram':
            fig = px.histogram(filtered_df, x=x_col, title=f'{selected_city} City - {x_col} Histogram')
        elif plot_type == 'scatter' and y_col:
            fig = px.scatter(filtered_df, x=x_col, y=y_col, title=f'{selected_city} City - {x_col} vs {y_col} Scatter Plot')
        elif plot_type == 'box':
            fig = px.box(filtered_df, x=x_col, y=y_col, title=f'{selected_city} City - {x_col} Box Plot')
        elif plot_type == 'bar' and y_col:
            fig = px.bar(filtered_df, x=x_col, y=y_col, title=f'{selected_city} City - {x_col} Bar Plot')
        elif plot_type == 'line' and y_col:
            fig = px.line(filtered_df, x=x_col, y=y_col, title=f'{selected_city} City - {x_col} Line Plot')
        elif plot_type == 'pie':
            fig = px.pie(filtered_df, names=x_col, title=f'{selected_city} City - {x_col} Pie Chart')
        elif plot_type == 'violin' and y_col:
            fig = px.violin(filtered_df, x=x_col, y=y_col, title=f'{selected_city} City - {x_col} Violin Plot')
        else:
            fig = px.histogram(filtered_df, x=x_col, title=f'{selected_city} City - {x_col} Histogram')
    else:
        fig = px.histogram(filtered_df, x='Price', nbins=50, title=f'{selected_city} City - Price Distribution')

    return fig

# Run the application
if __name__ == '__main__':
    app.run_server(debug=True)
