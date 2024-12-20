import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fuc.FefferyIdle(id='idle-demo'),
        fac.AntdText(id='idle-demo-output'),
    ]

    return demo_contents


@app.callback(
    Output('idle-demo-output', 'children'), Input('idle-demo', 'isIdle')
)
def idle_demo(isIdle):
    return f'isIdle: {isIdle}'


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
[
    fuc.FefferyIdle(id='idle-demo'),
    fac.AntdText(id='idle-demo-output'),
]

...

@app.callback(
    Output('idle-demo-output', 'children'), Input('idle-demo', 'isIdle')
)
def idle_demo(isIdle):
    return f'isIdle: {isIdle}'
"""
        }
    ]
