from dash import html
import feffery_utils_components as fuc
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fuc.FefferyListenScroll(id='listen-scroll-demo'),
        html.Pre(id='listen-scroll-demo-output'),
    ]

    return demo_contents


app.clientside_callback(
    """( position ) => JSON.stringify(position)""",
    Output('listen-scroll-demo-output', 'children'),
    Input('listen-scroll-demo', 'position'),
)


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': '''
[
    fuc.FefferyListenScroll(id='listen-scroll-demo'),
    html.Pre(id='listen-scroll-demo-output'),
]

...

app.clientside_callback(
    """( position ) => JSON.stringify(position)""",
    Output('listen-scroll-demo-output', 'children'),
    Input('listen-scroll-demo', 'position'),
)
'''
        }
    ]
