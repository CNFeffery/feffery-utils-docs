from dash.dependencies import Input, Output, State

from server import app


@app.callback(
    [Output('wheel-color-picker-demo-output', 'style'),
     Output('wheel-color-picker-demo-output', 'children')],
    Input('wheel-color-picker-demo', 'color'),
    State('wheel-color-picker-demo-output', 'style')
)
def wheel_color_picker_demo(color, old_style):

    return [
        {
            **old_style,
            'background': color
        },
        color
    ]
