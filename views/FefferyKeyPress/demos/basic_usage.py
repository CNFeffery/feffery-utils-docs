import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdParagraph(
            [
                fac.AntdText('用于监听指定的按键行为，常用的按键别名有：'),
                *[
                    fac.AntdText([fac.AntdText(key_name, keyboard=True), '、'])
                    for key_name in [
                        'backspace',
                        'tab',
                        'enter',
                        'shift',
                        'ctrl',
                        'alt',
                        'pausebreak',
                        'capslock',
                        'esc',
                        'space',
                        'pageup',
                        'pagedown',
                        'end',
                        'home',
                        'leftarrow',
                        'uparrow',
                        'rightarrow',
                        'downarrow',
                        'insert',
                        'delete',
                        'leftwindowkey',
                        'rightwindowkey',
                    ]
                ],
            ]
        ),
        fuc.FefferyKeyPress(id='key-press-demo', keys='ctrl.s'),
        fac.AntdParagraph(id='key-press-demo-output'),
    ]

    return demo_contents


@app.callback(
    Output('key-press-demo-output', 'children'),
    Input('key-press-demo', 'pressedCounts'),
)
def key_press_demo(pressedCounts):
    return f'pressedCounts: {pressedCounts}'


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
[
    fac.AntdParagraph(
        [
            fac.AntdText('　　用于监听指定的按键行为，常用的按键别名有：'),
            *[
                fac.AntdText([fac.AntdText(key_name, keyboard=True), '、'])
                for key_name in [
                    'backspace',
                    'tab',
                    'enter',
                    'shift',
                    'ctrl',
                    'alt',
                    'pausebreak',
                    'capslock',
                    'esc',
                    'space',
                    'pageup',
                    'pagedown',
                    'end',
                    'home',
                    'leftarrow',
                    'uparrow',
                    'rightarrow',
                    'downarrow',
                    'insert',
                    'delete',
                    'leftwindowkey',
                    'rightwindowkey',
                ]
            ],
        ]
    ),
    fuc.FefferyKeyPress(id='key-press-demo', keys='ctrl.s'),
    fac.AntdParagraph(id='key-press-demo-output'),
]

...

@app.callback(
    Output('key-press-demo-output', 'children'),
    Input('key-press-demo', 'pressedCounts'),
)
def key_press_demo(pressedCounts):
    return f'pressedCounts: {pressedCounts}'
"""
        }
    ]
