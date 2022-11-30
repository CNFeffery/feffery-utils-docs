import time
from datetime import datetime
from dash.dependencies import Input, Output, State

from server import app


@app.callback(
    Output('top-progress-demo', 'color'),
    Input('top-progress-color', 'color')
)
def top_progress_demo_update_color(color):

    return color


@app.callback(
    Output('top-progress-trigger-demo1-output', 'children'),
    Input('top-progress-trigger-demo1', 'nClicks'),
    prevent_initial_call=True
)
def top_progress_demo(nClicks):

    time.sleep(5)

    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')
