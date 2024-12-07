import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fuc.FefferyDiv(
            '鼠标移入此区域后进行图片粘贴',
            id='image-paste-container',
            shadow='hover-shadow',
            enableEvents=['hover'],
            style={
                'height': '200px',
                'display': 'flex',
                'justifyContent': 'center',
                'alignItems': 'center',
                'borderRadius': '6px',
                'border': '1px solid #f0f0f0',
                'marginBottom': '10px',
            },
        ),
        fuc.FefferyImagePaste(id='image-paste-demo', disabled=True),
        fac.AntdImage(id='image-paste-output', preview=True),
    ]

    return demo_contents


app.clientside_callback(
    """(isHovering) => !isHovering;""",
    Output('image-paste-demo', 'disabled'),
    Input('image-paste-container', 'isHovering'),
    prevent_initial_call=True,
)


app.clientside_callback(
    """(imageInfo) => imageInfo.base64;""",
    Output('image-paste-output', 'src'),
    Input('image-paste-demo', 'imageInfo'),
    prevent_initial_call=True,
)


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': '''
[
    fuc.FefferyDiv(
        '鼠标移入此区域后进行图片粘贴',
        id='image-paste-container',
        shadow='hover-shadow',
        enableEvents=['hover'],
        style={
            'height': '200px',
            'display': 'flex',
            'justifyContent': 'center',
            'alignItems': 'center',
            'borderRadius': '6px',
            'border': '1px solid #f0f0f0',
            'marginBottom': '10px',
        },
    ),
    fuc.FefferyImagePaste(id='image-paste-demo', disabled=True),
    fac.AntdImage(id='image-paste-output', preview=True),
]

...

app.clientside_callback(
    """(isHovering) => !isHovering;""",
    Output('image-paste-demo', 'disabled'),
    Input('image-paste-container', 'isHovering'),
    prevent_initial_call=True,
)


app.clientside_callback(
    """(imageInfo) => imageInfo.base64;""",
    Output('image-paste-output', 'src'),
    Input('image-paste-demo', 'imageInfo'),
    prevent_initial_call=True,
)
'''
        }
    ]
