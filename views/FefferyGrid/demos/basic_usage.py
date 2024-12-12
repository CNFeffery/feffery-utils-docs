import feffery_utils_components as fuc
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fuc.FefferyGrid(
        [
            fuc.FefferyGridItem(
                str(i),
                key=str(i),
                style={
                    'height': '100%',
                    'display': 'flex',
                    'justifyContent': 'center',
                    'alignItems': 'center',
                },
            )
            for i in range(10)
        ],
        layouts=[
            dict(i=str(i), x=i, y=i + 1, w=1, h=i + i % 2 + 1) for i in range(5)
        ],
        cols=5,
        rowHeight=75,
        placeholderBorderRadius='5px',
        margin=[25, 25],
        style={'border': '1px dashed #e1dfdd'},
    )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
fuc.FefferyGrid(
    [
        fuc.FefferyGridItem(
            str(i),
            key=str(i),
            style={
                'height': '100%',
                'display': 'flex',
                'justifyContent': 'center',
                'alignItems': 'center',
            },
        )
        for i in range(10)
    ],
    layouts=[
        dict(i=str(i), x=i, y=i + 1, w=1, h=i + i % 2 + 1) for i in range(5)
    ],
    cols=5,
    rowHeight=75,
    placeholderBorderRadius='5px',
    margin=[25, 25],
    style={'border': '1px dashed #e1dfdd'},
)
"""
        }
    ]
