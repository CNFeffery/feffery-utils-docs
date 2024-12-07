import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdFormItem(
            fac.AntdInputNumber(
                id='json-viewer-demo2-indent',
                min=1,
                max=8,
                step=1,
                value=4,
                style={'width': '100px'},
            ),
            label='缩进空格数：',
        ),
        fuc.FefferyJsonViewer(
            id='json-viewer-demo2',
            data={
                'int示例': 999,
                'float示例': 0.999,
                'string示例': '我爱dash',
                '数组示例': [0, 1, 2, 3],
                '字典示例': {'a': 1, 'b': 2, 'c': 3},
            },
        ),
    ]

    return demo_contents


@app.callback(
    Output('json-viewer-demo2', 'indent'),
    Input('json-viewer-demo2-indent', 'value'),
)
def json_viewer_demo2(value):
    return value or 4


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
[
    fac.AntdFormItem(
        fac.AntdInputNumber(
            id='json-viewer-demo2-indent',
            min=1,
            max=8,
            step=1,
            value=4,
            style={'width': '100px'},
        ),
        label='缩进空格数：',
    ),
    fuc.FefferyJsonViewer(
        id='json-viewer-demo2',
        data={
            'int示例': 999,
            'float示例': 0.999,
            'string示例': '我爱dash',
            '数组示例': [0, 1, 2, 3],
            '字典示例': {'a': 1, 'b': 2, 'c': 3},
        },
    ),
]

...

@app.callback(
    Output('json-viewer-demo2', 'indent'),
    Input('json-viewer-demo2-indent', 'value'),
)
def json_viewer_demo2(value):
    return value or 4
"""
        }
    ]
