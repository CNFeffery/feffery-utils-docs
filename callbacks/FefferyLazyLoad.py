import time
from datetime import datetime
from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('lazy-load-demo-output', 'children'),
    Input('lazy-load-demo', 'visible'),
    prevent_initial_call=True
)
def lazy_load_demo(visible):

    if visible:
        time.sleep(2)
        return '当前内容渲染时间：{}'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
