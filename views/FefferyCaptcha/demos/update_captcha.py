import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdButton('刷新', id='refresh-captcha', type='primary'),
            fuc.FefferyCaptcha(id='captcha-demo2'),
        ],
        direction='vertical',
    )

    return demo_contents


@app.callback(
    Output('captcha-demo2', 'refresh'),
    Input('refresh-captcha', 'nClicks'),
    prevent_initial_call=True,
)
def captcha_demo2(nClicks):
    return True


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
fac.AntdSpace(
    [
        fac.AntdButton('刷新', id='refresh-captcha', type='primary'),
        fuc.FefferyCaptcha(id='captcha-demo2'),
    ],
    direction='vertical',
)

...

@app.callback(
    Output('captcha-demo2', 'refresh'),
    Input('refresh-captcha', 'nClicks'),
    prevent_initial_call=True,
)
def captcha_demo2(nClicks):
    return True
"""
        }
    ]
