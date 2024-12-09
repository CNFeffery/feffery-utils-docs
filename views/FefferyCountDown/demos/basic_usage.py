import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdButton(
                '倒计时10秒', id='trigger-count-down-demo1', type='primary'
            ),
            fac.AntdText(id='count-down-demo1-output'),
            fuc.FefferyCountDown(id='count-down-demo1'),
        ],
        direction='vertical',
    )

    return demo_contents


@app.callback(
    Output('count-down-demo1', 'delay'),
    Input('trigger-count-down-demo1', 'nClicks'),
    prevent_initial_call=True,
)
def countdown_demo1_trigger(nClicks):
    return 10


@app.callback(
    Output('count-down-demo1-output', 'children'),
    Input('count-down-demo1', 'countdown'),
    prevent_initial_call=True,
)
def countdown_demo1_update(countdown):
    if countdown == 0:
        return

    return f'还剩{countdown}秒'


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
fac.AntdSpace(
    [
        fac.AntdButton(
            '倒计时10秒', id='trigger-count-down-demo1', type='primary'
        ),
        fac.AntdText(id='count-down-demo1-output'),
        fuc.FefferyCountDown(id='count-down-demo1'),
    ],
    direction='vertical',
)

...

@app.callback(
    Output('count-down-demo1', 'delay'),
    Input('trigger-count-down-demo1', 'nClicks'),
    prevent_initial_call=True,
)
def countdown_demo1_trigger(nClicks):
    return 10


@app.callback(
    Output('count-down-demo1-output', 'children'),
    Input('count-down-demo1', 'countdown'),
    prevent_initial_call=True,
)
def countdown_demo1_update(countdown):
    if countdown == 0:
        return

    return f'还剩{countdown}秒'
"""
        }
    ]
