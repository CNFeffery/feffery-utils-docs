import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fuc.FefferyTopProgress(id='top-progress-manual-demo', manual=True),
        fac.AntdSwitch(id='top-progress-manual-demo-toggle'),
    ]

    return demo_contents


@app.callback(
    Output('top-progress-manual-demo', 'spinning'),
    Input('top-progress-manual-demo-toggle', 'checked'),
    prevent_initial_call=True,
)
def toggle_top_progress_manual_demo(checked):
    return checked


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
[
    fuc.FefferyTopProgress(id='top-progress-manual-demo', manual=True),
    fac.AntdSwitch(id='top-progress-manual-demo-toggle'),
]

...

@app.callback(
    Output('top-progress-manual-demo', 'spinning'),
    Input('top-progress-manual-demo-toggle', 'checked'),
    prevent_initial_call=True,
)
def toggle_top_progress_manual_demo(checked):
    return checked
"""
        }
    ]
