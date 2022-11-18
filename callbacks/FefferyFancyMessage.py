import feffery_utils_components as fuc
from dash.dependencies import Input, Output, State

from server import app


@app.callback(
    Output('fancy-message-demo-container', 'children'),
    Input('trigger-fancy-message-demo', 'nClicks'),
    [State('fancy-message-demo-type', 'value'),
     State('fancy-message-demo-position', 'value')],
    prevent_initial_call=True
)
def fancy_message_demo(nClicks, message_type, message_position):

    return fuc.FefferyFancyMessage(
        'FefferyFancyMessage示例',
        id='fancy-message-demo',
        type=message_type,
        position=message_position
    )
