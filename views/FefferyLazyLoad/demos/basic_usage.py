import uuid
from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = html.Div(
        [
            fac.AntdText('请向下滚动'),
            html.Div(style={'height': '800px'}),
            fuc.FefferyLazyLoad(
                html.Div(
                    html.Img(
                        src='/assets/imgs/fuc-logo.svg?token='
                        + str(uuid.uuid4()),
                        style={'height': '100%'},
                    ),
                    style={'height': '100px', 'border': '1px dashed #c8c6c4'},
                ),
                height=100,
            ),
        ],
        style={'maxHeight': '300px', 'overflow': 'auto'},
    )

    return demo_contents


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
            html.Div(
                html.Img(
                    src='/assets/imgs/fuc-logo.svg?token='
                    + str(uuid.uuid4()),
                    style={'height': '100%'},
                ),
                style={'height': '100px', 'border': '1px dashed #c8c6c4'},
            ),
            height=100,
        ),
    ],
    style={'maxHeight': '300px', 'overflow': 'auto'},
)
"""
        }
    ]
