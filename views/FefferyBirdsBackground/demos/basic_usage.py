import feffery_antd_components as fac
from dash import html
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = html.Div(
        [
            html.Div(id='birds-background-container'),
            html.Pre(id='birds-background-options'),
            fac.AntdCenter(
                fac.AntdForm(
                    [
                        fac.AntdFormItem(
                            fac.AntdColorPicker(name='backgroundColor'),
                            label='backgroundColor',
                        ),
                        fac.AntdFormItem(
                            fac.AntdSlider(
                                name='backgroundAlpha',
                                min=0,
                                max=1,
                                step=0.1,
                            ),
                            label='backgroundAlpha',
                        ),
                        fac.AntdFormItem(
                            fac.AntdColorPicker(name='color1'),
                            label='color1',
                        ),
                        fac.AntdFormItem(
                            fac.AntdColorPicker(name='color2'),
                            label='color2',
                        ),
                        fac.AntdFormItem(
                            fac.AntdSelect(
                                name='colorMode',
                                options=[
                                    {'label': i, 'value': i}
                                    for i in [
                                        'lerp',
                                        'variance',
                                        'lerpGradient',
                                        'varianceGradient',
                                    ]
                                ],
                            ),
                            label='colorMode',
                        ),
                        fac.AntdFormItem(
                            fac.AntdSlider(
                                name='quantity',
                                min=1,
                                max=5,
                            ),
                            label='quantity',
                        ),
                        fac.AntdFormItem(
                            fac.AntdSlider(
                                name='birdSize',
                                min=1,
                                max=4,
                            ),
                            label='birdSize',
                        ),
                        fac.AntdFormItem(
                            fac.AntdSlider(
                                name='wingSpan',
                                min=10,
                                max=40,
                            ),
                            label='wingSpan',
                        ),
                        fac.AntdFormItem(
                            fac.AntdSlider(
                                name='speedLimit',
                                min=1,
                                max=10,
                            ),
                            label='speedLimit',
                        ),
                        fac.AntdFormItem(
                            fac.AntdSlider(
                                name='separation',
                                min=1,
                                max=100,
                            ),
                            label='separation',
                        ),
                        fac.AntdFormItem(
                            fac.AntdSlider(
                                name='alignment',
                                min=1,
                                max=100,
                            ),
                            label='alignment',
                        ),
                        fac.AntdFormItem(
                            fac.AntdSlider(
                                name='cohesion',
                                min=1,
                                max=100,
                            ),
                            label='cohesion',
                        ),
                    ],
                    id='birds-options',
                    labelCol={'span': 8},
                    wrapperCol={'span': 16},
                    enableBatchControl=True,
                    values={
                        'backgroundColor': '#000000',
                        'backgroundAlpha': 1,
                        'color1': '#ff0000',
                        'color2': '#13becf',
                        'colorMode': 'varianceGradient',
                        'quantity': 5,
                        'birdSize': 1,
                        'wingSpan': 30,
                        'speedLimit': 5,
                        'separation': 20,
                        'alignment': 20,
                        'cohesion': 20,
                    },
                    style={'width': 450, 'marginTop': '20px'},
                )
            ),
        ]
    )

    return demo_contents


app.clientside_callback(
    """
    (options) => {
        if (options) {
            return [
                {
                    "props": {
                        "children": {
                            "props": {
                                "children": "FefferyBirdsBackground",
                                "style": {
                                    "color": "white"
                                }
                            },
                            "type": "AntdCenter",
                            "namespace": "feffery_antd_components"
                        },
                        "style": {
                            "height": "30vh"
                        },
                        ...options
                    },
                    "type": "FefferyBirdsBackground",
                    "namespace": "feffery_utils_components"
                },
                String(new Date().getTime()),
                JSON.stringify(options, null, " ".repeat(2))
            ]
        }
        throw window.dash_clientside.PreventUpdate
    }
    """,
    [
        Output('birds-background-container', 'children'),
        Output('birds-background-container', 'key'),
        Output('birds-background-options', 'children'),
    ],
    Input('birds-options', 'values'),
)


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
html.Div(
    [
        html.Div(id='birds-background-container'),
        html.Pre(id='birds-background-options'),
        fac.AntdCenter(
            fac.AntdForm(
                [
                    fac.AntdFormItem(
                        fac.AntdColorPicker(name='backgroundColor'),
                        label='backgroundColor',
                    ),
                    fac.AntdFormItem(
                        fac.AntdSlider(
                            name='backgroundAlpha',
                            min=0,
                            max=1,
                            step=0.1,
                        ),
                        label='backgroundAlpha',
                    ),
                    fac.AntdFormItem(
                        fac.AntdColorPicker(name='color1'),
                        label='color1',
                    ),
                    fac.AntdFormItem(
                        fac.AntdColorPicker(name='color2'),
                        label='color2',
                    ),
                    fac.AntdFormItem(
                        fac.AntdSelect(
                            name='colorMode',
                            options=[
                                {'label': i, 'value': i}
                                for i in [
                                    'lerp',
                                    'variance',
                                    'lerpGradient',
                                    'varianceGradient',
                                ]
                            ],
                        ),
                        label='colorMode',
                    ),
                    fac.AntdFormItem(
                        fac.AntdSlider(
                            name='quantity',
                            min=1,
                            max=5,
                        ),
                        label='quantity',
                    ),
                    fac.AntdFormItem(
                        fac.AntdSlider(
                            name='birdSize',
                            min=1,
                            max=4,
                        ),
                        label='birdSize',
                    ),
                    fac.AntdFormItem(
                        fac.AntdSlider(
                            name='wingSpan',
                            min=10,
                            max=40,
                        ),
                        label='wingSpan',
                    ),
                    fac.AntdFormItem(
                        fac.AntdSlider(
                            name='speedLimit',
                            min=1,
                            max=10,
                        ),
                        label='speedLimit',
                    ),
                    fac.AntdFormItem(
                        fac.AntdSlider(
                            name='separation',
                            min=1,
                            max=100,
                        ),
                        label='separation',
                    ),
                    fac.AntdFormItem(
                        fac.AntdSlider(
                            name='alignment',
                            min=1,
                            max=100,
                        ),
                        label='alignment',
                    ),
                    fac.AntdFormItem(
                        fac.AntdSlider(
                            name='cohesion',
                            min=1,
                            max=100,
                        ),
                        label='cohesion',
                    ),
                ],
                id='birds-options',
                labelCol={'span': 8},
                wrapperCol={'span': 16},
                enableBatchControl=True,
                values={
                    'backgroundColor': '#000000',
                    'backgroundAlpha': 1,
                    'color1': '#ff0000',
                    'color2': '#13becf',
                    'colorMode': 'varianceGradient',
                    'quantity': 5,
                    'birdSize': 1,
                    'wingSpan': 30,
                    'speedLimit': 5,
                    'separation': 20,
                    'alignment': 20,
                    'cohesion': 20,
                },
                style={'width': 450, 'marginTop': '20px'},
            )
        ),
    ]
)

...

app.clientside_callback(
    '''
    (options) => {
        if (options) {
            return [
                {
                    "props": {
                        "children": {
                            "props": {
                                "children": "FefferyBirdsBackground",
                                "style": {
                                    "color": "white"
                                }
                            },
                            "type": "AntdCenter",
                            "namespace": "feffery_antd_components"
                        },
                        "style": {
                            "height": "30vh"
                        },
                        ...options
                    },
                    "type": "FefferyBirdsBackground",
                    "namespace": "feffery_utils_components"
                },
                String(new Date().getTime()),
                JSON.stringify(options, null, " ".repeat(2))
            ]
        }
        throw window.dash_clientside.PreventUpdate
    }
    ''',
    [
        Output('birds-background-container', 'children'),
        Output('birds-background-container', 'key'),
        Output('birds-background-options', 'children'),
    ],
    Input('birds-options', 'values'),
)
"""
        }
    ]
