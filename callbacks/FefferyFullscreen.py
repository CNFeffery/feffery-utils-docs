from dash.dependencies import Input, Output, State

from server import app


@app.callback(
    [Output('fullscreen-demo', 'isFullscreen'),
     Output('toggle-fullscreen', 'children')],
    Input('toggle-fullscreen', 'nClicks'),
    State('fullscreen-demo', 'isFullscreen'),
    prevent_initial_call=True
)
def toggle_fullscreen(nClicks, isFullscreen):

    return [
        not isFullscreen,
        '全屏化' if isFullscreen else '退出全屏化'
    ]
