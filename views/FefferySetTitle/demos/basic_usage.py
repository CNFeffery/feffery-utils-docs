import dash
import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdInput(
            id='set-title-demo',
            placeholder='请输入新title信息',
            style={'maxWidth': '200px'},
        ),
        fuc.FefferySetTitle(
            id='set-title-demo-output',
            originTitle='feffery-utils-components在线文档',
        ),
    ]

    return demo_contents


@app.callback(
    Output('set-title-demo-output', 'title'),
    Input('set-title-demo', 'value'),
    prevent_initial_call=True,
)
def set_title_demo(value):
    return value


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
[
    fac.AntdInput(
        id='set-title-demo',
        placeholder='请输入新title信息',
        style={'maxWidth': '200px'},
    ),
    fuc.FefferySetTitle(
        id='set-title-demo-output',
        originTitle='feffery-utils-components在线文档',
    ),
]

...

@app.callback(
    Output('set-title-demo-output', 'title'),
    Input('set-title-demo', 'value'),
    prevent_initial_call=True,
)
def set_title_demo(value):
    return value
"""
        }
    ]
