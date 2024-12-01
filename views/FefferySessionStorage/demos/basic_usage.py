import json
from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdButton('执行示例js代码', id='session-storage-demo-input'),
        fuc.FefferyExecuteJs(id='session-storage-demo-trigger'),
        fuc.FefferySessionStorage(id='session-storage-demo'),
        html.Pre(id='session-storage-demo-output'),
    ]

    return demo_contents


@app.callback(
    Output('session-storage-demo-trigger', 'jsString'),
    Input('session-storage-demo-input', 'nClicks'),
    prevent_initial_call=True,
)
def trigger_session_storage_set(nClicks):
    return (
        """sessionStorage.setItem('session-storage-demo', JSON.stringify({'点击次数': % s, '当前时间': new Date(Date.now())}))"""
        % str(nClicks)
    )


@app.callback(
    Output('session-storage-demo-output', 'children'),
    Input('session-storage-demo', 'data'),
    prevent_initial_call=True,
)
def session_storage_demo(data):
    return json.dumps(data, ensure_ascii=False, indent=4)


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': '''
[
    fac.AntdButton('执行示例js代码', id='session-storage-demo-input'),
    fuc.FefferyExecuteJs(id='session-storage-demo-trigger'),
    fuc.FefferySessionStorage(id='session-storage-demo'),
    html.Pre(id='session-storage-demo-output'),
]

...

@app.callback(
    Output('session-storage-demo-trigger', 'jsString'),
    Input('session-storage-demo-input', 'nClicks'),
    prevent_initial_call=True,
)
def trigger_session_storage_set(nClicks):
    return (
        """sessionStorage.setItem('session-storage-demo', JSON.stringify({'点击次数': % s, '当前时间': new Date(Date.now())}))"""
        % str(nClicks)
    )


@app.callback(
    Output('session-storage-demo-output', 'children'),
    Input('session-storage-demo', 'data'),
    prevent_initial_call=True,
)
def session_storage_demo(data):
    return json.dumps(data, ensure_ascii=False, indent=4)
'''
        }
    ]
