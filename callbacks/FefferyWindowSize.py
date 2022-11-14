
from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('window-size-demo-output', 'children'),
    [Input('window-size-demo', '_width'),
     Input('window-size-demo', '_height')]
)
def window_size_demo(_width, _height):

    return f'_width: {_width}  _height: {_height}'
