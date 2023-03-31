from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('listen-unload-demo-output', 'children'),
    Input('listen-unload-demo', 'unloaded'),
    prevent_initial_call=True
)
def listen_unload_demo(unloaded):

    print(f'unloaded: {unloaded}')
