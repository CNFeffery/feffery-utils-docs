import json
from dash import html
import feffery_utils_components as fuc
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fuc.FefferyResponsive(id='responsive-demo'),
        html.Pre(id='responsive-demo-output'),
    ]

    return demo_contents


@app.callback(
    Output('responsive-demo-output', 'children'),
    Input('responsive-demo', 'responsive'),
)
def responsive_demo(responsive):
    return json.dumps(responsive, ensure_ascii=False, indent=4)


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
[
    fuc.FefferyResponsive(id='responsive-demo'),
    html.Pre(id='responsive-demo-output'),
]

...

@app.callback(
    Output('responsive-demo-output', 'children'),
    Input('responsive-demo', 'responsive'),
)
def responsive_demo(responsive):
    return json.dumps(responsive, ensure_ascii=False, indent=4)
"""
        }
    ]
