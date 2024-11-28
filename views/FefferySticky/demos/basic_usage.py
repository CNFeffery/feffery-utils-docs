from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = html.Div(
        [
            html.Div(style={'height': '200px'}),
            fuc.FefferySticky(
                fac.AntdTag(color='green', content='请向下滚动查看效果'),
                top=100,
                bottomBoundary=800,
            ),
            html.Div(style={'height': '1200px'}),
        ]
    )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
html.Div(
    [
        html.Div(style={'height': '200px'}),
        fuc.FefferySticky(
            fac.AntdTag(color='green', content='请向下滚动查看效果'),
            top=100,
            bottomBoundary=800,
        ),
        html.Div(style={'height': '1200px'}),
    ]
)
"""
        }
    ]
