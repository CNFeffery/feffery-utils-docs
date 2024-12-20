import time
import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fuc.FefferyDocumentVisibility(id='document-visibility-demo'),
        fac.AntdSpin(
            fac.AntdText(
                'documentVisibility: visible',
                id='document-visibility-demo-output',
            ),
            text='状态延时2s切换中',
            size='small',
        ),
    ]

    return demo_contents


@app.callback(
    Output('document-visibility-demo-output', 'children'),
    Input('document-visibility-demo', 'documentVisibility'),
)
def document_visibility_demo(documentVisibility):
    if documentVisibility == 'visible':
        time.sleep(2)

    return f'documentVisibility: {documentVisibility}'


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
[
    fuc.FefferyDocumentVisibility(id='document-visibility-demo'),
    fac.AntdSpin(
        fac.AntdText(
            'documentVisibility: visible',
            id='document-visibility-demo-output',
        ),
        text='状态延时2s切换中',
        size='small',
    ),
]

...

@app.callback(
    Output('document-visibility-demo-output', 'children'),
    Input('document-visibility-demo', 'documentVisibility'),
)
def document_visibility_demo(documentVisibility):
    if documentVisibility == 'visible':
        time.sleep(2)

    return f'documentVisibility: {documentVisibility}'
"""
        }
    ]
