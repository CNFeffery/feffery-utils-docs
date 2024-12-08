import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component, Input, Output, State

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fuc.FefferyFullscreen(
            id='fullscreen-demo', targetId='fullscreen-target'
        ),
        fac.AntdCenter(
            fac.AntdButton('全屏化', id='toggle-fullscreen', type='primary'),
            id='fullscreen-target',
            style={
                'height': 200,
                'background': 'white',
            },
        ),
    ]

    return demo_contents


@app.callback(
    [
        Output('fullscreen-demo', 'isFullscreen'),
        Output('toggle-fullscreen', 'children'),
    ],
    Input('toggle-fullscreen', 'nClicks'),
    State('fullscreen-demo', 'isFullscreen'),
    prevent_initial_call=True,
)
def toggle_fullscreen(nClicks, isFullscreen):
    return [not isFullscreen, '全屏化' if isFullscreen else '退出全屏化']


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
[
    fuc.FefferyFullscreen(
        id='fullscreen-demo', targetId='fullscreen-target'
    ),
    fac.AntdCenter(
        fac.AntdButton('全屏化', id='toggle-fullscreen', type='primary'),
        id='fullscreen-target',
        style={
            'height': 200,
            'background': 'white',
        },
    ),
]

...

@app.callback(
    [
        Output('fullscreen-demo', 'isFullscreen'),
        Output('toggle-fullscreen', 'children'),
    ],
    Input('toggle-fullscreen', 'nClicks'),
    State('fullscreen-demo', 'isFullscreen'),
    prevent_initial_call=True,
)
def toggle_fullscreen(nClicks, isFullscreen):
    return [not isFullscreen, '全屏化' if isFullscreen else '退出全屏化']
"""
        }
    ]
