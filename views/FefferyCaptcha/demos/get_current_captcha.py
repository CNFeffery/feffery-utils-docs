import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fuc.FefferyCaptcha(id='captcha-demo1'),
        fac.AntdText(id='output-demo1'),
    ]

    return demo_contents


@app.callback(
    Output('output-demo1', 'children'), Input('captcha-demo1', 'captcha')
)
def captcha_demo1(captcha):
    return f'当前验证码：{captcha}'


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
[
    fuc.FefferyCaptcha(id='captcha-demo1'),
    fac.AntdText(id='output-demo1'),
]

...

@app.callback(
    Output('output-demo1', 'children'), Input('captcha-demo1', 'captcha')
)
def captcha_demo1(captcha):
    return f'当前验证码：{captcha}'
"""
        }
    ]
