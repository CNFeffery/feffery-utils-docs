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
                fac.AntdButton(
                    '立即重载', id='trigger-reload-demo', type='primary'
                ),
                fac.AntdButton(
                    '2秒后重载',
                    id='trigger-reload-delay-demo',
                    type='primary',
                    autoSpin=True,
                    loadingChildren='等待重载中',
                ),
            ],
        ),
        fuc.FefferyReload(id='trigger-reload-demo-output'),
        fuc.FefferyReload(id='trigger-reload-delay-demo-output', delay=2000),
    ]

    return demo_contents


@app.callback(
    Output('trigger-reload-demo-output', 'reload'),
    Input('trigger-reload-demo', 'nClicks'),
    prevent_initial_call=True,
)
def reload_demo(nClicks):
    return True


@app.callback(
    Output('trigger-reload-delay-demo-output', 'reload'),
    Input('trigger-reload-delay-demo', 'nClicks'),
    prevent_initial_call=True,
)
def reload_delay_demo(nClicks):
    return True


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
[
    fac.AntdSpace(
        [
            fac.AntdButton(
                '立即重载', id='trigger-reload-demo', type='primary'
            ),
            fac.AntdButton(
                '2秒后重载',
                id='trigger-reload-delay-demo',
                type='primary',
                autoSpin=True,
                loadingChildren='等待重载中',
            ),
        ],
    ),
    fuc.FefferyReload(id='trigger-reload-demo-output'),
    fuc.FefferyReload(id='trigger-reload-delay-demo-output', delay=2000),
]

...

@app.callback(
    Output('trigger-reload-demo-output', 'reload'),
    Input('trigger-reload-demo', 'nClicks'),
    prevent_initial_call=True,
)
def reload_demo(nClicks):
    return True


@app.callback(
    Output('trigger-reload-delay-demo-output', 'reload'),
    Input('trigger-reload-delay-demo', 'nClicks'),
    prevent_initial_call=True,
)
def reload_delay_demo(nClicks):
    return True
"""
        }
    ]
