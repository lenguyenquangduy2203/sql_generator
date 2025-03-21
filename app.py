import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from src.pages import home, docs, play_ground

# Initialize Dash app with multiple pages
app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server  # Required for deployment

# Define app layout with navigation
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    dbc.NavbarSimple(
        children=[
            dbc.NavItem(dcc.Link("Home", href="/", className="nav-link")),
            dbc.NavItem(dcc.Link("Docs", href="/docs", className="nav-link")),
            dbc.NavItem(dcc.Link("Play Ground", href="/play-ground", className="nav-link")),
        ],
        brand="SQL Generator",
        color="blue",
        className="mb-4"
    ),
    html.Div(id='page-content')  # Placeholder for pages
])

# Define callback to update the page content based on URL
@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == "/docs":
        return docs.layout
    elif pathname == "/play-ground":
        return play_ground.layout
    return home.layout  # Default to home page

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
