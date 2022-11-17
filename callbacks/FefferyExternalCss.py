import dash
from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('external-css-demo', 'cssUrl'),
    [Input('mount-dark-css', 'nClicks'),
     Input('unmount-css', 'nClicks')],
    prevent_initial_call=True
)
def external_css_demo(*args):

    if dash.ctx.triggered_id == 'mount-dark-css':
        return '/assets/css/dark.css'

    else:
        return ''
