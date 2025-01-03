import json
from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fuc.FefferySliderCaptcha(
                id='slider-captcha-demo',
                imgSrc='/assets/imgs/components/FefferySliderCaptcha/demo.jpg',
                # 按照图片实际尺寸设定
                imgWidth=520,
                imgHeight=304,
                mode='float',
            ),
            html.Pre(
                id='slider-captcha-demo-output',
            ),
        ],
        direction='vertical',
        style={'width': '100%'},
    )

    return demo_contents


@app.callback(
    Output('slider-captcha-demo-output', 'children'),
    Input('slider-captcha-demo', 'verifyResult'),
    prevent_initial_call=True,
)
def slider_captcha_demo(verifyResult):
    return json.dumps(verifyResult, ensure_ascii=False, indent=4)


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
fac.AntdSpace(
    [
        fuc.FefferySliderCaptcha(
            id='slider-captcha-demo',
            imgSrc='/assets/imgs/components/FefferySliderCaptcha/demo.jpg',
            # 按照图片实际尺寸设定
            imgWidth=520,
            imgHeight=304,
            mode='float',
        ),
        html.Pre(
            id='slider-captcha-demo-output',
        ),
    ],
    direction='vertical',
    style={'width': '100%'},
)

...

@app.callback(
    Output('slider-captcha-demo-output', 'children'),
    Input('slider-captcha-demo', 'verifyResult'),
    prevent_initial_call=True,
)
def slider_captcha_demo(verifyResult):
    return json.dumps(verifyResult, ensure_ascii=False, indent=4)
"""
        }
    ]
