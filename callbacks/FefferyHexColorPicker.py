from dash.dependencies import Input, Output, State

from server import app


@app.callback(
    [Output('hex-color-picker-demo-output', 'style'),
     Output('hex-color-picker-demo-output', 'children')],
    Input('hex-color-picker-demo', 'color'),
    State('hex-color-picker-demo-output', 'style')
)
def hex_color_picker_demo(color, old_style):

    return [
        {
            **old_style,
            'background': color
        },
        color
    ]
