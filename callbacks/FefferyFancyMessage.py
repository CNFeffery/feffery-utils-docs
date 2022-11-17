import feffery_utils_components as fuc
from dash.dependencies import Input, Output, State

from server import app


@app.callback(
    Output('fancy-message-demo1-container', 'children'),
    Input('trigger-fancy-message-demo1', 'nClicks'),
    State('fancy-message-demo1-type', 'value'),
    prevent_initial_call=True
)
def fancy_message_demo1(nClicks, message_type):

    return fuc.FefferyFancyMessage(
        'FefferyFancyMessage示例',
        id='fancy-message-demo1',
        type=message_type,
        visible=True
    )


@app.callback(
    Output('fancy-message-demo2-container', 'children'),
    Input('trigger-fancy-message-demo2', 'nClicks'),
    State('fancy-message-demo2-position', 'value'),
    prevent_initial_call=True
)
def fancy_message_demo2(nClicks, position):

    return fuc.FefferyFancyMessage(
        'FefferyFancyMessage示例',
        id='fancy-message-demo2',
        position=position,
        visible=True,
        type='success'
    )
