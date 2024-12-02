import feffery_utils_components as fuc
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fuc.FefferyRawHTML(
        htmlString="""
<div style="width: 300px;height: 150px;box-shadow: 0px 0px 12px rgba(0, 0, 0, .12); display: flex;justify-content: center;align-items: center;">
    示例
</ div>
"""
    )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': '''
fuc.FefferyRawHTML(
    htmlString="""
<div style="width: 300px;height: 150px;box-shadow: 0px 0px 12px rgba(0, 0, 0, .12); display: flex;justify-content: center;align-items: center;">
    示例
</ div>
"""
)
'''
        }
    ]
