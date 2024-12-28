import feffery_utils_components as fuc
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fuc.FefferyMotion(
            style={
                'background': '#71afe5',
                'width': '50px',
                'height': '50px',
                'marginBottom': '10px',
            },
            animate={'transform': 'translateX(200px)', 'background': '#d83b01'},
            transition={
                # 无限循环动画
                'repeat': 'infinity',
                'duration': 2,
                'type': 'spring',
            },
        ),
        fuc.FefferyMotion(
            '示例',
            style={
                'border': '1px dashed #71afe5',
                'width': '100px',
                'height': '100px',
                'display': 'flex',
                'justifyContent': 'center',
                'alignItems': 'center',
            },
            animate={
                'transform': 'translateX(300px) rotate(180deg)',
                'borderRadius': '100%',
            },
            transition={
                # 无限循环动画
                'repeat': 'infinity',
                'duration': 2,
                'type': 'spring',
            },
        ),
    ]

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
[
    fuc.FefferyMotion(
        style={
            'background': '#71afe5',
            'width': '50px',
            'height': '50px',
            'marginBottom': '10px',
        },
        animate={'transform': 'translateX(200px)', 'background': '#d83b01'},
        transition={
            # 无限循环动画
            'repeat': 'infinity',
            'duration': 2,
            'type': 'spring',
        },
    ),
    fuc.FefferyMotion(
        '示例',
        style={
            'border': '1px dashed #71afe5',
            'width': '100px',
            'height': '100px',
            'display': 'flex',
            'justifyContent': 'center',
            'alignItems': 'center',
        },
        animate={
            'transform': 'translateX(300px) rotate(180deg)',
            'borderRadius': '100%',
        },
        transition={
            # 无限循环动画
            'repeat': 'infinity',
            'duration': 2,
            'type': 'spring',
        },
    ),
]
"""
        }
    ]
