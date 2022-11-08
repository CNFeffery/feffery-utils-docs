import time
from datetime import datetime
import feffery_utils_components as fuc
from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('extra-spinner-demo-output', 'children'),
    Input('extra-spinner-demo', 'nClicks'),
    prevent_initial_call=True
)
def extra_spinner_demo(nClicks):

    time.sleep(5)

    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


@app.callback(
    Output('extra-spinner-demo-spin', 'indicator'),
    Input('extra-spinner-demo-type', 'value')
)
def extra_spinner_demo_indicator(value):

    return fuc.FefferyExtraSpinner(
        type=value
    )
