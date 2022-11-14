
from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('idle-demo-output', 'children'),
    Input('idle-demo', 'isIdle')
)
def idle_demo(isIdle):

    return f'isIdle: {isIdle}'
