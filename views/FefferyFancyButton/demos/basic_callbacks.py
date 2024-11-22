import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdSpace(
                [
                    fuc.FefferyFancyButton('default', id='fancy-button1'),
                    fac.AntdText(id='fancy-button-output1'),
                ],
                style={'marginBottom': 10},
            ),
            fac.AntdSpace(
                [
                    fuc.FefferyFancyButton(
                        'debounceWait=500', id='fancy-button2', debounceWait=500
                    ),
                    fac.AntdText(id='fancy-button-output2'),
                ]
            ),
        ],
        direction='vertical',
        style={'width': '100%'},
    )

    return demo_contents


@app.callback(
    Output('fancy-button-output1', 'children'),
    Input('fancy-button1', 'nClicks'),
    prevent_initial_call=True,
)
def fancy_button_demo1(nClicks):
    return f'nClicks: {nClicks}'


@app.callback(
    Output('fancy-button-output2', 'children'),
    Input('fancy-button2', 'nClicks'),
    prevent_initial_call=True,
)
def fancy_button_demo2(nClicks):
    return f'nClicks: {nClicks}'


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
fac.AntdSpace(
    [
        fac.AntdSpace(
            [
                fuc.FefferyFancyButton('default', id='fancy-button1'),
                fac.AntdText(id='fancy-button-output1'),
            ],
            style={'marginBottom': 10},
        ),
        fac.AntdSpace(
            [
                fuc.FefferyFancyButton(
                    'debounceWait=500', id='fancy-button2', debounceWait=500
                ),
                fac.AntdText(id='fancy-button-output2'),
            ]
        ),
    ],
    direction='vertical',
    style={'width': '100%'},
)

...

@app.callback(
    Output('fancy-button-output1', 'children'),
    Input('fancy-button1', 'nClicks'),
    prevent_initial_call=True,
)
def fancy_button_demo1(nClicks):
    return f'nClicks: {nClicks}'


@app.callback(
    Output('fancy-button-output2', 'children'),
    Input('fancy-button2', 'nClicks'),
    prevent_initial_call=True,
)
def fancy_button_demo2(nClicks):
    return f'nClicks: {nClicks}'
"""
        }
    ]
