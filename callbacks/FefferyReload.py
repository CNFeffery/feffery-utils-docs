from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('trigger-reload-demo-output', 'reload'),
    Input('trigger-reload-demo', 'nClicks'),
    prevent_initial_call=True
)
def reload_demo(nClicks):

    return True


@app.callback(
    Output('trigger-reload-delay-demo-output', 'reload'),
    Input('trigger-reload-delay-demo', 'nClicks'),
    prevent_initial_call=True
)
def reload_delay_demo(nClicks):

    return True
