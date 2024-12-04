import time
from dash import html
from datetime import datetime
import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = html.Div(
        [
            fac.AntdText('请向下滚动'),
            html.Div(style={'height': '800px'}),
            fuc.FefferyLazyLoad(
                fac.AntdSkeleton(
                    html.Div(
                        id='lazy-load-demo-output',
                        style={
                            'height': '100px',
                            'border': '1px dashed #c8c6c4',
                        },
                    ),
                    active=True,
                ),
                id='lazy-load-demo',
                height=100,
                throttle=0,
            ),
        ],
        style={'maxHeight': '300px', 'overflow': 'auto'},
    )

    return demo_contents


@app.callback(
    Output('lazy-load-demo-output', 'children'),
    Input('lazy-load-demo', 'visible'),
    prevent_initial_call=True,
)
def lazy_load_demo(visible):
    if visible:
        time.sleep(2)
        return '当前内容渲染时间：{}'.format(
            datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        )


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
html.Div(
    [
        fac.AntdText('请向下滚动'),
        html.Div(style={'height': '800px'}),
        fuc.FefferyLazyLoad(
            fac.AntdSkeleton(
                html.Div(
                    id='lazy-load-demo-output',
                    style={
                        'height': '100px',
                        'border': '1px dashed #c8c6c4',
                    },
                ),
                active=True,
            ),
            id='lazy-load-demo',
            height=100,
            throttle=0,
        ),
    ],
    style={'maxHeight': '300px', 'overflow': 'auto'},
)

...

@app.callback(
    Output('lazy-load-demo-output', 'children'),
    Input('lazy-load-demo', 'visible'),
    prevent_initial_call=True,
)
def lazy_load_demo(visible):
    if visible:
        time.sleep(2)
        return '当前内容渲染时间：{}'.format(
            datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        )
"""
        }
    ]
