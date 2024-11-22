import time
from datetime import datetime
import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdSpace(
            [
                fuc.FefferyWheelColorPicker(
                    id='top-progress-color', color='#e74c3c'
                ),
                fac.AntdButton(
                    '触发5秒耗时回调',
                    id='top-progress-trigger-demo1',
                    type='primary',
                ),
            ]
        ),
        fuc.FefferyTopProgress(
            fac.AntdText(id='top-progress-trigger-demo1-output'),
            id='top-progress-demo',
            listenPropsMode='exclude',
            excludeProps=['top-progress-demo.color'],
        ),
    ]

    return demo_contents


@app.callback(
    Output('top-progress-demo', 'color'), Input('top-progress-color', 'color')
)
def top_progress_demo_update_color(color):
    return color


@app.callback(
    Output('top-progress-trigger-demo1-output', 'children'),
    Input('top-progress-trigger-demo1', 'nClicks'),
    prevent_initial_call=True,
)
def top_progress_demo(nClicks):
    time.sleep(5)

    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
[
    fac.AntdSpace(
        [
            fuc.FefferyWheelColorPicker(
                id='top-progress-color', color='#e74c3c'
            ),
            fac.AntdButton(
                '触发5秒耗时回调',
                id='top-progress-trigger-demo1',
                type='primary',
            ),
        ]
    ),
    fuc.FefferyTopProgress(
        fac.AntdText(id='top-progress-trigger-demo1-output'),
        id='top-progress-demo',
        listenPropsMode='exclude',
        excludeProps=['top-progress-demo.color'],
    ),
]

...

@app.callback(
    Output('top-progress-demo', 'color'), Input('top-progress-color', 'color')
)
def top_progress_demo_update_color(color):
    return color


@app.callback(
    Output('top-progress-trigger-demo1-output', 'children'),
    Input('top-progress-trigger-demo1', 'nClicks'),
    prevent_initial_call=True,
)
def top_progress_demo(nClicks):
    time.sleep(5)

    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')
"""
        }
    ]
