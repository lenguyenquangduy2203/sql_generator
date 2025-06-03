from dash import Input, Output, State, html, dcc

layout = html.Div([
    html.H1("Play Ground", className="header-title"),
    html.P("You can convert SQN into SQL query here.", className="lead mb-4"),
    html.Div([
        dcc.Textarea(
            id='sqn-input',
            placeholder='Enter SQN here...',
            style={'width': '45%', 'height': 200, 'borderRadius': '5px', 'padding': '10px', 'fontFamily': 'monospace', 'fontSize': '14px'},
            className="me-3"
        ),
        
        html.Button('Convert', id='convert-button', n_clicks=0, className="btn btn-primary align-self-start", style={'marginTop': '20px'}),
        
        dcc.Textarea(
            id='sql-output',
            placeholder='SQL query will appear here...',
            style={'width': '45%', 'height': 200, 'borderRadius': '5px', 'padding': '10px', 'fontFamily': 'monospace', 'fontSize': '14px'},
            readOnly=True,
            className="ms-3"
        )
    ], style={'display': 'flex', 'alignItems': 'flex-start'}, className="container")
], className="container py-4")

def init_play_ground_handler(app):
    @app.callback(
        Output('sql-output', 'value'),
        Input('convert-button', 'n_clicks'),
        State('sqn-input', 'value'),
        prevent_initial_call=True
    )
    def convert_sqn_to_sql(n_clicks, sqn_input):
        # Placeholder conversion logic — replace with actual SQN parser
        if not sqn_input:
            return "Please enter an SQN statement."
        
        # Simulated conversion for demo purposes
        sql_query = f"-- Converted SQL from SQN:\n{sqn_input}"
        return sql_query
    