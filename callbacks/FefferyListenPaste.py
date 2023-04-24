from dash.dependencies import Input, Output, State

from server import app


app.clientside_callback(
    '''( pasteCount, pasteText ) => JSON.stringify({ pasteCount, pasteText }, null, 4)''',
    Output('listen-paste-basic-demo-output', 'children'),
    Input('listen-paste-basic-demo', 'pasteCount'),
    State('listen-paste-basic-demo', 'pasteText'),
)


app.clientside_callback(
    '''( pasteCount, pasteText ) => JSON.stringify({ pasteCount, pasteText }, null, 4)''',
    Output('listen-paste-target-container-demo-output', 'children'),
    Input('listen-paste-target-container-demo', 'pasteCount'),
    State('listen-paste-target-container-demo', 'pasteText'),
)
