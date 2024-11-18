import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fuc.FefferyBurger(id='burger-demo', toggled=False),
            fac.AntdText(id='burger-demo-output'),
        ]
    )

    return demo_contents


@app.callback(
    Output('burger-demo-output', 'children'),
    Input('burger-demo', 'toggled'),
)
def show_toggled(toggled):
    return f'toggled: {toggled}'


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
fac.AntdSpace(
    [
        fuc.FefferyBurger(id='burger-demo', toggled=False),
        fac.AntdText(id='burger-demo-output'),
    ]
)

...

@app.callback(
    Output('burger-demo-output', 'children'),
    Input('burger-demo', 'toggled'),
)
def show_toggled(toggled):
    return f'toggled: {toggled}'
"""
        }
    ]
