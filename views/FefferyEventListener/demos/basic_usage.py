import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fuc.FefferyEventListener(
            eventName='dblclick',
            targetSelector='#event-listener-basic-demo-target',
            handler="() => alert('dblclick event')",
        ),
        fac.AntdButton(
            '请双击',
            id='event-listener-basic-demo-target',
            type='primary',
        ),
    ]

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
[
    fuc.FefferyEventListener(
        eventName='dblclick',
        targetSelector='#event-listener-basic-demo-target',
        handler="() => alert('dblclick event')",
    ),
    fac.AntdButton(
        '请双击',
        id='event-listener-basic-demo-target',
        type='primary',
    ),
]
"""
        }
    ]
