from dash.dependencies import Input, Output, State

from server import app


@app.callback(
    [Output('rgb-color-picker-demo-output', 'style'),
     Output('rgb-color-picker-demo-output', 'children')],
    Input('rgb-color-picker-demo', 'color'),
    State('rgb-color-picker-demo-output', 'style')
)
def rgb_color_picker_demo(color, old_style):

    return [
        {
            **old_style,
            'background': color
        },
        color
    ]
