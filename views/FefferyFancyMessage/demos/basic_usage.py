import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component, Input, Output, State

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdSpace(
            [
                fac.AntdSelect(
                    id='fancy-message-demo-type',
                    options=[
                        {'label': type_, 'value': type_}
                        for type_ in ['blank', 'success', 'error']
                    ],
                    defaultValue='blank',
                    allowClear=False,
                    style={'width': '100px'},
                ),
                fac.AntdSelect(
                    id='fancy-message-demo-position',
                    options=[
                        {'label': position, 'value': position}
                        for position in [
                            'top-left',
                            'top-center',
                            'top-right',
                            'bottom-left',
                            'bottom-center',
                            'bottom-right',
                        ]
                    ],
                    defaultValue='top-center',
                    allowClear=False,
                    style={'width': '150px'},
                ),
                fac.AntdButton('触发消息提示', id='trigger-fancy-message-demo'),
            ]
        ),
        fac.Fragment(id='fancy-message-demo-container'),
    ]

    return demo_contents


@app.callback(
    Output('fancy-message-demo-container', 'children'),
    Input('trigger-fancy-message-demo', 'nClicks'),
    [
        State('fancy-message-demo-type', 'value'),
        State('fancy-message-demo-position', 'value'),
    ],
    prevent_initial_call=True,
)
def fancy_message_demo(nClicks, message_type, message_position):
    return fuc.FefferyFancyMessage(
        'FefferyFancyMessage示例',
        id='fancy-message-demo',
        type=message_type,
        position=message_position,
    )


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
[
    fac.AntdSpace(
        [
            fac.AntdSelect(
                id='fancy-message-demo-type',
                options=[
                    {'label': type_, 'value': type_}
                    for type_ in ['blank', 'success', 'error']
                ],
                defaultValue='blank',
                allowClear=False,
                style={'width': '100px'},
            ),
            fac.AntdSelect(
                id='fancy-message-demo-position',
                options=[
                    {'label': position, 'value': position}
                    for position in [
                        'top-left',
                        'top-center',
                        'top-right',
                        'bottom-left',
                        'bottom-center',
                        'bottom-right',
                    ]
                ],
                defaultValue='top-center',
                allowClear=False,
                style={'width': '150px'},
            ),
            fac.AntdButton('触发消息提示', id='trigger-fancy-message-demo'),
        ]
    ),
    fac.Fragment(id='fancy-message-demo-container'),
]

...

@app.callback(
    Output('fancy-message-demo-container', 'children'),
    Input('trigger-fancy-message-demo', 'nClicks'),
    [
        State('fancy-message-demo-type', 'value'),
        State('fancy-message-demo-position', 'value'),
    ],
    prevent_initial_call=True,
)
def fancy_message_demo(nClicks, message_type, message_position):
    return fuc.FefferyFancyMessage(
        'FefferyFancyMessage示例',
        id='fancy-message-demo',
        type=message_type,
        position=message_position,
    )
"""
        }
    ]
