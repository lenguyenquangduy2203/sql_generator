from dash import html

layout = html.Div([
    html.Header([
        html.H1("Home Page", className="header-title"),
        html.P("Welcome to the home page of SQL Generator app.", className="header-subtitle"),
    ], className="header-section"),

    html.Main([
        html.Div([
            html.Div([
                html.Img(src="/assets/img/bg.jpg", className="card-img"),
                html.H3("SQL Converter"),
                html.P("Convert SQN into SQL query."),
            ], className="card"),

            html.Div([
                html.Img(src="/assets/img/bg.jpg", className="card-img"),
                html.H3("Feature Two"),
                html.P("Another amazing feature to explore."),
            ], className="card"),
        ], style={"display": "flex", "gap": "1rem", "flexWrap": "wrap"}),
    ], className="main-section"),


    html.Footer("© 2025 DreamyBull CompanyCompany", className="footer"),
], className="page-container")
