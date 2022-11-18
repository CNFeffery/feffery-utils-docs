import feffery_utils_components as fuc
from dash.dependencies import Input, Output, State

from server import app


@app.callback(
    Output('fancy-notification-demo-container', 'children'),
    Input('trigger-fancy-notification-demo', 'nClicks'),
    [State('fancy-notification-demo-type', 'value'),
     State('fancy-notification-demo-position', 'value'),
     State('fancy-notification-demo-theme', 'value')],
    prevent_initial_call=True
)
def fancy_notification_demo(nClicks,
                            notification_type,
                            notification_position,
                            notification_theme):

    return fuc.FefferyFancyNotification(
        'FefferyFancyNotification示例',
        id='fancy-notification-demo',
        type=notification_type,
        position=notification_position,
        theme=notification_theme
    )
