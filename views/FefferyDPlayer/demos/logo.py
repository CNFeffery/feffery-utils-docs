import feffery_utils_components as fuc
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fuc.FefferyDPlayer(
        video={
            'url': 'https://vjs.zencdn.net/v/oceans.mp4',
            'type': 'auto',
        },
        logo='/assets/imgs/fuc-logo.svg',
        style={'width': '100%'},
    )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
fuc.FefferyDPlayer(
    video={
        'url': 'https://vjs.zencdn.net/v/oceans.mp4',
        'type': 'auto',
    },
    logo='/assets/imgs/fuc-logo.svg',
    style={'width': '100%'},
)
"""
        }
    ]
