import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fuc.FefferyWindowSize(id='window-size-demo'),
        fac.AntdText(id='window-size-demo-output'),
    ]

    return demo_contents


@app.callback(
    Output('window-size-demo-output', 'children'),
    [Input('window-size-demo', '_width'), Input('window-size-demo', '_height')],
)
def window_size_demo(_width, _height):
    return f'_width: {_width}  _height: {_height}'


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
[
    fuc.FefferyWindowSize(id='window-size-demo'),
    fac.AntdText(id='window-size-demo-output'),
]

...

@app.callback(
    Output('window-size-demo-output', 'children'),
    [Input('window-size-demo', '_width'), Input('window-size-demo', '_height')],
)
def window_size_demo(_width, _height):
    return f'_width: {_width}  _height: {_height}'
"""
        }
    ]
