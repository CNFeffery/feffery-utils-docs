import random
from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('shortcut-panel-demo', 'data'),
    Input('shortcut-panel-demo', 'searchValue'),
    prevent_initial_call=True
)
def shortcut_panel_demo(searchValue):

    return [
        {
            'id': f'{searchValue}搜索结果{i}',
            'title': f'{searchValue}搜索结果{i}',
        }
        for i in range(1, random.randint(3, 6))
    ]
