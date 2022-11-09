from dash.dependencies import Input, Output, State

from server import app


@app.callback(
    Output('github-color-picker-demo-output', 'style'),
    Input('github-color-picker-demo', 'color'),
    State('github-color-picker-demo-output', 'style')
)
def github_color_picker_demo(color, old_style):

    return {
        **old_style,
        'background': color
    }
