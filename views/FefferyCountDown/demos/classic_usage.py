import uuid
from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdButton(
            '刷新示例', id='refresh-count-down-demo2', type='primary'
        ),
        html.Div(id='count-down-demo2-container'),
    ]

    return demo_contents


@app.callback(
    Output('count-down-demo2-container', 'children'),
    Input('refresh-count-down-demo2', 'nClicks'),
    prevent_initial_call=True,
)
def countdown_demo2_refresh(nClicks):
    return html.Div(
        [
            html.Div(
                '用户须知：' + '巴拉巴拉' * 200,
                style={
                    'borderBottom': '1px solid #bfbfbf',
                    'paddingBottom': '15px',
                    'maxHeight': '400px',
                    'overflowY': 'auto',
                },
            ),
            fac.AntdButton(
                '我已知晓用户须知内容',
                id='count-down-demo2-output',
                type='primary',
                block=True,
                disabled=True,
                style={'marginTop': '15px'},
            ),
            fuc.FefferyCountDown(id='count-down-demo2', delay=10),
        ],
        # 强制刷新用
        id=str(uuid.uuid4()),
        style={
            'border': '1px solid #bfbfbf',
            'padding': '20px',
            'width': '300px',
        },
    )


@app.callback(
    [
        Output('count-down-demo2-output', 'children'),
        Output('count-down-demo2-output', 'disabled'),
    ],
    Input('count-down-demo2', 'countdown'),
)
def countdown_demo2(countdown):
    if countdown == 0:
        return ['我已知晓用户须知内容', False]

    return [f'我已知晓用户须知内容（{countdown}s）', True]


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
[
    fac.AntdButton(
        '刷新示例', id='refresh-count-down-demo2', type='primary'
    ),
    html.Div(id='count-down-demo2-container'),
]

...

@app.callback(
    Output('count-down-demo2-container', 'children'),
    Input('refresh-count-down-demo2', 'nClicks'),
    prevent_initial_call=True,
)
def countdown_demo2_refresh(nClicks):
    return html.Div(
        [
            html.Div(
                '用户须知：' + '巴拉巴拉' * 200,
                style={
                    'borderBottom': '1px solid #bfbfbf',
                    'paddingBottom': '15px',
                    'maxHeight': '400px',
                    'overflowY': 'auto',
                },
            ),
            fac.AntdButton(
                '我已知晓用户须知内容',
                id='count-down-demo2-output',
                type='primary',
                block=True,
                disabled=True,
                style={'marginTop': '15px'},
            ),
            fuc.FefferyCountDown(id='count-down-demo2', delay=10),
        ],
        # 强制刷新用
        id=str(uuid.uuid4()),
        style={
            'border': '1px solid #bfbfbf',
            'padding': '20px',
            'width': '300px',
        },
    )


@app.callback(
    [
        Output('count-down-demo2-output', 'children'),
        Output('count-down-demo2-output', 'disabled'),
    ],
    Input('count-down-demo2', 'countdown'),
)
def countdown_demo2(countdown):
    if countdown == 0:
        return ['我已知晓用户须知内容', False]

    return [f'我已知晓用户须知内容（{countdown}s）', True]
"""
        }
    ]
