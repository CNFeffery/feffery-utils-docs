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
                    id='fancy-notification-demo-type',
                    options=[
                        {'label': type_, 'value': type_}
                        for type_ in ['info', 'success', 'warning', 'error']
                    ],
                    defaultValue='info',
                    allowClear=False,
                    style={'width': '100px'},
                ),
                fac.AntdSelect(
                    id='fancy-notification-demo-position',
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
                    defaultValue='top-right',
                    allowClear=False,
                    style={'width': '125px'},
                ),
                fac.AntdSelect(
                    id='fancy-notification-demo-theme',
                    options=[
                        {'label': theme, 'value': theme}
                        for theme in ['light', 'dark', 'colored']
                    ],
                    defaultValue='light',
                    allowClear=False,
                    style={'width': '100px'},
                ),
                fac.AntdButton(
                    '触发通知框', id='trigger-fancy-notification-demo'
                ),
            ]
        ),
        fac.Fragment(id='fancy-notification-demo-container'),
    ]

    return demo_contents


@app.callback(
    Output('fancy-notification-demo-container', 'children'),
    Input('trigger-fancy-notification-demo', 'nClicks'),
    [
        State('fancy-notification-demo-type', 'value'),
        State('fancy-notification-demo-position', 'value'),
        State('fancy-notification-demo-theme', 'value'),
    ],
    prevent_initial_call=True,
)
def fancy_notification_demo(
    nClicks, notification_type, notification_position, notification_theme
):
    return fuc.FefferyFancyNotification(
        'FefferyFancyNotification示例',
        id='fancy-notification-demo',
        type=notification_type,
        position=notification_position,
        theme=notification_theme,
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
                id='fancy-notification-demo-type',
                options=[
                    {'label': type_, 'value': type_}
                    for type_ in ['info', 'success', 'warning', 'error']
                ],
                defaultValue='info',
                allowClear=False,
                style={'width': '100px'},
            ),
            fac.AntdSelect(
                id='fancy-notification-demo-position',
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
                defaultValue='top-right',
                allowClear=False,
                style={'width': '125px'},
            ),
            fac.AntdSelect(
                id='fancy-notification-demo-theme',
                options=[
                    {'label': theme, 'value': theme}
                    for theme in ['light', 'dark', 'colored']
                ],
                defaultValue='light',
                allowClear=False,
                style={'width': '100px'},
            ),
            fac.AntdButton(
                '触发通知框', id='trigger-fancy-notification-demo'
            ),
        ]
    ),
    fac.Fragment(id='fancy-notification-demo-container'),
]

...

@app.callback(
    Output('fancy-notification-demo-container', 'children'),
    Input('trigger-fancy-notification-demo', 'nClicks'),
    [
        State('fancy-notification-demo-type', 'value'),
        State('fancy-notification-demo-position', 'value'),
        State('fancy-notification-demo-theme', 'value'),
    ],
    prevent_initial_call=True,
)
def fancy_notification_demo(
    nClicks, notification_type, notification_position, notification_theme
):
    return fuc.FefferyFancyNotification(
        'FefferyFancyNotification示例',
        id='fancy-notification-demo',
        type=notification_type,
        position=notification_position,
        theme=notification_theme,
    )
"""
        }
    ]
