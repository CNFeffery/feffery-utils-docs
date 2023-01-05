from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('json-viewer-demo1', 'theme'),
    Input('json-viewer-demo1-theme', 'value')
)
def json_viewer_demo1(value):

    return value


@app.callback(
    Output('json-viewer-demo2', 'indent'),
    Input('json-viewer-demo2-indent', 'value')
)
def json_viewer_demo2(value):

    return value or 4
