import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fuc.FefferyCookie(
            id='cookie-basic-demo',
            cookieKey='feffery-cookie-basic-demo',
            defaultValue='I~love~dash!',
        ),
        fac.AntdText(
            '请在浏览器开发者工具-应用中查看当前应用的cookies信息',
            type='secondary',
        ),
    ]

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
fuc.FefferyCookie(
    id='cookie-basic-demo',
    cookieKey='feffery-cookie-basic-demo',
    defaultValue='I~love~dash!',
)
"""
        }
    ]
