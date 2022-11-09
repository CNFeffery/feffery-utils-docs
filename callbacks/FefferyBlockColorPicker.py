from dash.dependencies import Input, Output, State

from server import app


@app.callback(
    Output('block-color-picker-demo-output', 'style'),
    Input('block-color-picker-demo', 'color'),
    State('block-color-picker-demo-output', 'style')
)
def block_color_picker_demo(color, old_style):

    return {
        **old_style,
        'background': color
    }
