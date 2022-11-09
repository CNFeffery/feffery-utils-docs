from dash.dependencies import Input, Output, State

from server import app


@app.callback(
    Output('twitter-color-picker-demo-output', 'style'),
    Input('twitter-color-picker-demo', 'color'),
    State('twitter-color-picker-demo-output', 'style')
)
def twitter_color_picker_demo(color, old_style):

    return {
        **old_style,
        'background': color
    }
