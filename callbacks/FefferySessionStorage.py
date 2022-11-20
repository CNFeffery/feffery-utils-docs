import json
from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('session-storage-demo-trigger', 'jsString'),
    Input('session-storage-demo-input', 'nClicks'),
    prevent_initial_call=True
)
def trigger_session_storage_set(nClicks):

    return '''sessionStorage.setItem('session-storage-demo', JSON.stringify({'点击次数': %s, '当前时间': new Date(Date.now())}))''' % str(nClicks)


@app.callback(
    Output('session-storage-demo-output', 'children'),
    Input('session-storage-demo', 'data'),
    prevent_initial_call=True
)
def session_storage_demo(data):

    return json.dumps(
        data,
        ensure_ascii=False,
        indent=4
    )
