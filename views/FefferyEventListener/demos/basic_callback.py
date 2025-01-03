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
        fuc.FefferyEventListener(
            id='event-listener-demo',
            eventName='dblclick',
            targetSelector='#event-listener-demo-target',
            handler='() => ({ timestamp: Date.now() })',
        ),
        fac.AntdSpace(
            [
                fac.AntdButton(
                    '请双击',
                    id='event-listener-demo-target',
                    type='primary',
                ),
                html.Pre(id='event-listener-demo-output'),
            ],
            direction='vertical',
            style={'width': '100%'},
        ),
    ]

    return demo_contents


@app.callback(
    Output('event-listener-demo-output', 'children'),
    Input('event-listener-demo', 'result'),
    prevent_initial_call=True,
)
def event_listener_demo(result):
    return json.dumps(result, ensure_ascii=False, indent=4)


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
[
    fuc.FefferyEventListener(
        id='event-listener-demo',
        eventName='dblclick',
        targetSelector='#event-listener-demo-target',
        handler='() => ({ timestamp: Date.now() })',
    ),
    fac.AntdSpace(
        [
            fac.AntdButton(
                '请双击',
                id='event-listener-demo-target',
                type='primary',
            ),
            html.Pre(id='event-listener-demo-output'),
        ],
        direction='vertical',
        style={'width': '100%'},
    ),
]

...

@app.callback(
    Output('event-listener-demo-output', 'children'),
    Input('event-listener-demo', 'result'),
    prevent_initial_call=True,
)
def event_listener_demo(result):
    return json.dumps(result, ensure_ascii=False, indent=4)
"""
        }
    ]
