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
            '提示：请在当前页面任何地方粘贴文字内容查看示例效果',
            type='secondary',
        ),
        fuc.FefferyListenPaste(
            id='listen-paste-basic-demo', enableListenPaste=True
        ),
        html.Pre(id='listen-paste-basic-demo-output'),
    ]

    return demo_contents


app.clientside_callback(
    """( pasteCount, pasteText ) => JSON.stringify({ pasteCount, pasteText }, null, 4)""",
    Output('listen-paste-basic-demo-output', 'children'),
    Input('listen-paste-basic-demo', 'pasteCount'),
    State('listen-paste-basic-demo', 'pasteText'),
)


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': '''
[
    fac.AntdParagraph(
        '提示：请在当前页面任何地方粘贴文字内容查看示例效果',
        type='secondary',
    ),
    fuc.FefferyListenPaste(
        id='listen-paste-basic-demo', enableListenPaste=True
    ),
    html.Pre(id='listen-paste-basic-demo-output'),
]

...

app.clientside_callback(
    """( pasteCount, pasteText ) => JSON.stringify({ pasteCount, pasteText }, null, 4)""",
    Output('listen-paste-basic-demo-output', 'children'),
    Input('listen-paste-basic-demo', 'pasteCount'),
    State('listen-paste-basic-demo', 'pasteText'),
)
'''
        }
    ]
