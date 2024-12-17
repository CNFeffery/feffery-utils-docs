from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component, Input, Output, State

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdParagraph(
            '提示：请将鼠标移入下方示例容器后进行文本粘贴', type='secondary'
        ),
        fuc.FefferyListenPaste(
            id='listen-paste-target-container-demo',
            targetContainerId='listen-paste-target-container',
        ),
        fuc.FefferyDiv(
            id='listen-paste-target-container',
            shadow='always-shadow',
            style={'width': 300, 'height': 200, 'borderRadius': 6},
        ),
        html.Pre(id='listen-paste-target-container-demo-output'),
    ]

    return demo_contents


app.clientside_callback(
    """( pasteCount, pasteText ) => JSON.stringify({ pasteCount, pasteText }, null, 4)""",
    Output('listen-paste-target-container-demo-output', 'children'),
    Input('listen-paste-target-container-demo', 'pasteCount'),
    State('listen-paste-target-container-demo', 'pasteText'),
)


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': '''
[
    fac.AntdParagraph(
        '提示：请将鼠标移入下方示例容器后进行文本粘贴', type='secondary'
    ),
    fuc.FefferyListenPaste(
        id='listen-paste-target-container-demo',
        targetContainerId='listen-paste-target-container',
    ),
    fuc.FefferyDiv(
        id='listen-paste-target-container',
        shadow='always-shadow',
        style={'width': 300, 'height': 200, 'borderRadius': 6},
    ),
    html.Pre(id='listen-paste-target-container-demo-output'),
]

...

app.clientside_callback(
    """( pasteCount, pasteText ) => JSON.stringify({ pasteCount, pasteText }, null, 4)""",
    Output('listen-paste-target-container-demo-output', 'children'),
    Input('listen-paste-target-container-demo', 'pasteCount'),
    State('listen-paste-target-container-demo', 'pasteText'),
)
'''
        }
    ]
