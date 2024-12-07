import feffery_utils_components as fuc
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fuc.FefferyJsonViewer(
        data={
            'int示例': 999,
            'float示例': 0.999,
            'string示例': '我爱dash',
            '数组示例': [0, 1, 2, 3],
            '字典示例': {'a': 1, 'b': 2, 'c': 3},
        },
        rootName='root',
    )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
fuc.FefferyJsonViewer(
    data={
        'int示例': 999,
        'float示例': 0.999,
        'string示例': '我爱dash',
        '数组示例': [0, 1, 2, 3],
        '字典示例': {'a': 1, 'b': 2, 'c': 3},
    },
    rootName='root',
)
"""
        }
    ]
