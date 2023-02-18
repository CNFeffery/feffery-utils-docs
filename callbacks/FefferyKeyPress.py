from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('key-press-demo-output', 'children'),
    Input('key-press-demo', 'pressedCounts')
)
def key_press_demo(pressedCounts):

    return f'pressedCounts: {pressedCounts}'
