from dash import html

layout = html.Div([
    html.H1("Documents", className="header-title"),
    html.P("This is a simple multi-page Dash app.", className="lead"),
], className="container py-4")
