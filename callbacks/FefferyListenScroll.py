from dash.dependencies import Input, Output

from server import app

app.clientside_callback(
    '''( position ) => JSON.stringify(position)''',
    Output('listen-scroll-demo-output', 'children'),
    Input('listen-scroll-demo', 'position')
)


app.clientside_callback(
    '''( position ) => JSON.stringify(position)''',
    Output('listen-scroll-target-demo-output', 'children'),
    Input('listen-scroll-target-demo', 'position')
)