from dash.dependencies import Input, Output, State

from server import app


@app.callback(
    Output('circle-color-picker-demo-output', 'style'),
    Input('circle-color-picker-demo', 'color'),
    State('circle-color-picker-demo-output', 'style')
)
def circle_color_picker_demo(color, old_style):

    return {
        **old_style,
        'background': color
    }
