import dash
from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('set-title-demo-output', 'title'),
    Input('set-title-demo', 'value'),
    prevent_initial_call=True
)
def set_title_demo(value):

    return value or dash.no_update
