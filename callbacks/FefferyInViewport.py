
from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('in-viewport-demo1-output', 'children'),
    Input('in-viewport-demo1', 'inViewport')
)
def in_viewport_demo1(inViewport):

    return f'inViewport: {inViewport}'

@app.callback(
    Output('in-viewport-demo2-output', 'children'),
    Input('in-viewport-demo2', 'inViewport')
)
def in_viewport_demo2(inViewport):

    return f'inViewport: {inViewport}'