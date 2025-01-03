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
        fuc.FefferyTextSelection(
            id='text-selection-demo', targetId='text-selection-demo-target'
        ),
        fac.AntdSpace(
            [
                fac.AntdParagraph(
                    '1234567890', id='text-selection-demo-target'
                ),
                html.Pre(id='text-selection-demo-output'),
            ],
            direction='vertical',
            style={'width': '100%'},
        ),
    ]

    return demo_contents


@app.callback(
    Output('text-selection-demo-output', 'children'),
    Input('text-selection-demo', 'selectedTextInfo'),
    prevent_initial_call=True,
)
def text_selection_demo(selectedTextInfo):
    return json.dumps(selectedTextInfo, ensure_ascii=False, indent=4)


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
[
    fuc.FefferyTextSelection(
        id='text-selection-demo', targetId='text-selection-demo-target'
    ),
    fac.AntdSpace(
        [
            fac.AntdParagraph(
                '1234567890', id='text-selection-demo-target'
            ),
            html.Pre(id='text-selection-demo-output'),
        ],
        direction='vertical',
        style={'width': '100%'},
    ),
]

...

@app.callback(
    Output('text-selection-demo-output', 'children'),
    Input('text-selection-demo', 'selectedTextInfo'),
    prevent_initial_call=True,
)
def text_selection_demo(selectedTextInfo):
    return json.dumps(selectedTextInfo, ensure_ascii=False, indent=4)
"""
        }
    ]
