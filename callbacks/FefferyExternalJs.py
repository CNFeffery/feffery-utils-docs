import dash
from dash.dependencies import Input, Output

from server import app


@app.callback(
    [Output('external-js-demo', 'jsUrl'),
     Output('execute-party-effect', 'jsString')],
    Input('mount-js', 'nClicks'),
    prevent_initial_call=True
)
def external_js_demo(nClicks):

    if nClicks and nClicks == 1:
        return [
            'https://fastly.jsdelivr.net/npm/party-js@latest/bundle/party.min.js',
            '''
document.querySelector("#effect-when-mount").addEventListener("click", function (e) {
    party.confetti(this);
});
'''
        ]

    return dash.no_update
