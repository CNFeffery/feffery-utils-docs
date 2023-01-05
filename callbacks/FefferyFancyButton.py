from dash.dependencies import Input, Output

from server import app

@app.callback(
    Output('fancy-button-output1', 'children'),
    Input('fancy-button1', 'nClicks'),
    prevent_initial_call=True
)
def fancy_button_demo1(nClicks):

    return f'nClicks: {nClicks}'

@app.callback(
    Output('fancy-button-output2', 'children'),
    Input('fancy-button2', 'nClicks'),
    prevent_initial_call=True
)
def fancy_button_demo2(nClicks):

    return f'nClicks: {nClicks}'