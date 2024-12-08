import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdButton('执行示例', id='execute-js-demo', type='primary'),
            fuc.FefferyExecuteJs(id='execute-js-demo-output'),
        ],
        direction='vertical',
    )

    return demo_contents


@app.callback(
    Output('execute-js-demo-output', 'jsString'),
    Input('execute-js-demo', 'nClicks'),
    prevent_initial_call=True,
)
def execute_js_demo(nClicks):
    return 'alert("FefferyExecuteJs示例");'


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
fac.AntdSpace(
    [
        fac.AntdButton('执行示例', id='execute-js-demo', type='primary'),
        fuc.FefferyExecuteJs(id='execute-js-demo-output'),
    ],
    direction='vertical',
)

...

@app.callback(
    Output('execute-js-demo-output', 'jsString'),
    Input('execute-js-demo', 'nClicks'),
    prevent_initial_call=True,
)
def execute_js_demo(nClicks):
    return 'alert("FefferyExecuteJs示例");'
"""
        }
    ]
