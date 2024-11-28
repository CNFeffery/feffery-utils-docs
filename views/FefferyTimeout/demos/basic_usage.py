import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component, Input, Output, State

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdFormItem(
            fac.AntdSpace(
                [
                    fac.AntdInputNumber(
                        id='timeout-demo-delay',
                        value=2000,
                        style={'maxWidth': '300px'},
                    ),
                    fac.AntdButton(
                        '开始', id='timeout-demo-start', type='primary'
                    ),
                ]
            ),
            label='设置定时时长（毫秒）',
        ),
        fuc.FefferyTimeout(id='timeout-demo'),
        fuc.FefferyExecuteJs(id='timeout-demo-output'),
    ]

    return demo_contents


@app.callback(
    Output('timeout-demo', 'delay'),
    Input('timeout-demo-start', 'nClicks'),
    State('timeout-demo-delay', 'value'),
    prevent_initial_call=True,
)
def start_new_timeout(nClicks, value):
    if value > 0:
        return value


@app.callback(
    Output('timeout-demo-output', 'jsString'),
    Input('timeout-demo', 'timeoutCount'),
    prevent_initial_call=True,
)
def after_timeout(timeoutCount):
    return 'alert(`timeoutCount=${%s}`)' % timeoutCount


@app.callback(
    Output('timeout-demo-start', 'loading'), Input('timeout-demo', 'delay')
)
def enable_start_new(delay):
    return bool(delay)


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
[
    fac.AntdFormItem(
        fac.AntdSpace(
            [
                fac.AntdInputNumber(
                    id='timeout-demo-delay',
                    value=2000,
                    style={'maxWidth': '300px'},
                ),
                fac.AntdButton(
                    '开始', id='timeout-demo-start', type='primary'
                ),
            ]
        ),
        label='设置定时时长（毫秒）',
    ),
    fuc.FefferyTimeout(id='timeout-demo'),
    fuc.FefferyExecuteJs(id='timeout-demo-output'),
]

...

@app.callback(
    Output('timeout-demo', 'delay'),
    Input('timeout-demo-start', 'nClicks'),
    State('timeout-demo-delay', 'value'),
    prevent_initial_call=True,
)
def start_new_timeout(nClicks, value):
    if value > 0:
        return value


@app.callback(
    Output('timeout-demo-output', 'jsString'),
    Input('timeout-demo', 'timeoutCount'),
    prevent_initial_call=True,
)
def after_timeout(timeoutCount):
    return 'alert(`timeoutCount=${%s}`)' % timeoutCount


@app.callback(
    Output('timeout-demo-start', 'loading'), Input('timeout-demo', 'delay')
)
def enable_start_new(delay):
    return bool(delay)
"""
        }
    ]
