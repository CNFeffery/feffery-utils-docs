import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdFormItem(
            fac.AntdSelect(
                id='json-viewer-demo1-theme',
                options=[
                    {'label': theme, 'value': theme}
                    for theme in [
                        'summerfruit:inverted',
                        'apathy',
                        'apathy:inverted',
                        'ashes',
                        'bespin',
                        'bright:inverted',
                        'bright',
                        'chalk',
                        'codeschool',
                        'colors',
                        'eighties',
                        'embers',
                        'flat',
                        'google',
                        'grayscale',
                        'grayscale:inverted',
                        'greenscreen',
                        'harmonic',
                        'hopscotch',
                        'isotope',
                        'marrakesh',
                        'mocha',
                        'monokai',
                        'ocean',
                        'paraiso',
                        'pop',
                        'railscasts',
                        'rjv-default',
                        'shapeshifter',
                        'shapeshifter:inverted',
                        'solarized',
                        'summerfruit',
                        'threezerotwofour',
                        'tomorrow',
                        'tube',
                        'twilight',
                        'brewer',
                    ]
                ],
                value='summerfruit:inverted',
                allowClear=False,
                placement='topLeft',
                style={'width': '200px'},
            ),
            label='主题选择：',
        ),
        fuc.FefferyJsonViewer(
            id='json-viewer-demo1',
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
    Output('json-viewer-demo1', 'theme'),
    Input('json-viewer-demo1-theme', 'value'),
)
def json_viewer_demo1(value):
    return value


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
[
    fac.AntdFormItem(
        fac.AntdSelect(
            id='json-viewer-demo1-theme',
            options=[
                {'label': theme, 'value': theme}
                for theme in [
                    'summerfruit:inverted',
                    'apathy',
                    'apathy:inverted',
                    'ashes',
                    'bespin',
                    'bright:inverted',
                    'bright',
                    'chalk',
                    'codeschool',
                    'colors',
                    'eighties',
                    'embers',
                    'flat',
                    'google',
                    'grayscale',
                    'grayscale:inverted',
                    'greenscreen',
                    'harmonic',
                    'hopscotch',
                    'isotope',
                    'marrakesh',
                    'mocha',
                    'monokai',
                    'ocean',
                    'paraiso',
                    'pop',
                    'railscasts',
                    'rjv-default',
                    'shapeshifter',
                    'shapeshifter:inverted',
                    'solarized',
                    'summerfruit',
                    'threezerotwofour',
                    'tomorrow',
                    'tube',
                    'twilight',
                    'brewer',
                ]
            ],
            value='summerfruit:inverted',
            allowClear=False,
            placement='topLeft',
            style={'width': '200px'},
        ),
        label='主题选择：',
    ),
    fuc.FefferyJsonViewer(
        id='json-viewer-demo1',
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
    Output('json-viewer-demo1', 'theme'),
    Input('json-viewer-demo1-theme', 'value'),
)
def json_viewer_demo1(value):
    return value
"""
        }
    ]
