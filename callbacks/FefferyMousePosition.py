from dash.dependencies import Input, Output

from server import app

app.clientside_callback(
    '''( position ) => JSON.stringify(position, null, 4)''',
    Output('mouse-position-demo-output', 'children'),
    Input('mouse-position-demo', 'position')
)
