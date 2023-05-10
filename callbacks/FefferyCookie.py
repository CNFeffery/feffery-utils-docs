from flask import request
from dash.dependencies import Input, Output, State

from server import app


@app.callback(
    Output('cookie-dynamic-update-value-demo', 'value'),
    Input('cookie-dynamic-update-value-demo-add-one', 'nClicks'),
    State('cookie-dynamic-update-value-demo', 'value'),
    prevent_initial_call=True
)
def cookie_dynamic_update_value_demo_add_one(nClicks, value):

    return str(int(value) + 1)


@app.callback(
    Output('cookie-dynamic-update-value-demo-output', 'children'),
    Input('cookie-dynamic-update-value-demo-update-output', 'nClicks')
)
def cookie_dynamic_update_value_demo_output(nClicks):

    return 'feffery-cookie-dynamic-update-demo: {}'.format(
        request.cookies.get('feffery-cookie-dynamic-update-demo')
    )
