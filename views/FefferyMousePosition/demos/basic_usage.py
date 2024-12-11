from dash import html
import feffery_utils_components as fuc
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fuc.FefferyMousePosition(id='mouse-position-demo'),
        html.Pre(id='mouse-position-demo-output'),
    ]

    return demo_contents


app.clientside_callback(
    """( position ) => JSON.stringify(position, null, 4)""",
    Output('mouse-position-demo-output', 'children'),
    Input('mouse-position-demo', 'position'),
)


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': '''
[
    fuc.FefferyMousePosition(id='mouse-position-demo'),
    html.Pre(id='mouse-position-demo-output'),
]

...

app.clientside_callback(
    """( position ) => JSON.stringify(position, null, 4)""",
    Output('mouse-position-demo-output', 'children'),
    Input('mouse-position-demo', 'position'),
)
'''
        }
    ]
