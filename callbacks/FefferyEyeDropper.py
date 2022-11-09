from dash.dependencies import Input, Output, State

from server import app


@app.callback(
    Output('eye-dropper-demo', 'enable'),
    Input('enable-eye-dropper', 'nClicks'),
    prevent_initial_call=True
)
def enable_eye_dropper_demo(nClicks):

    return True


@app.callback(
    Output('eye-dropper-demo-output', 'style'),
    Input('eye-dropper-demo', 'color'),
    State('eye-dropper-demo-output', 'style'),
    prevent_initial_call=True
)
def eye_dropper_demo(color, old_style):

    return {
        **old_style,
        'background': color
    }
