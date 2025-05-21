from dash import Input, Output, State, html, dcc

layout = html.Div([
    html.H1("Play Ground"),
    html.P("You can convert SQN into SQL query here."),
    html.Div([
        dcc.Textarea(
            id='sqn-input',
            placeholder='Enter SQN here...',
            style={'width': '45%', 'height': 200}
        ),
        
        html.Button('Convert', id='convert-button', n_clicks=0, style={'margin': '0 10px'}),
        
        dcc.Textarea(
            id='sql-output',
            placeholder='SQL query will appear here...',
            style={'width': '45%', 'height': 200},
            readOnly=True
        )
    ], style={'display': 'flex', 'alignItems': 'start'}),
])

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
    