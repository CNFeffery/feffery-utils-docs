from dash.dependencies import Input, Output, State

from server import app


@app.callback(
    Output('timeout-demo', 'delay'),
    Input('timeout-demo-start', 'nClicks'),
    State('timeout-demo-delay', 'value'),
    prevent_initial_call=True
)
def start_new_timeout(nClicks, value):

    if value > 0:
        return value


@app.callback(
    Output('timeout-demo-output', 'jsString'),
    Input('timeout-demo', 'timeoutCount'),
    prevent_initial_call=True
)
def after_timeout(timeoutCount):

    return 'alert(`timeoutCount=${%s}`)' % timeoutCount


@app.callback(
    Output('timeout-demo-start', 'loading'),
    Input('timeout-demo', 'delay')
)
def enable_start_new(delay):

    return bool(delay)
