from dash import html
from datetime import datetime
import feffery_antd_components as fac
import feffery_utils_components as fuc

import callbacks.FefferyExtraSpinner
from views.side_props import render_side_props_layout

docs_content = html.Div(
    [
        html.Div(
            [
                fac.AntdBackTop(
                    duration=0.3
                ),

                fac.AntdBreadcrumb(
                    items=[
                        {
                            'title': '通用组件'
                        },
                        {
                            'title': 'FefferyExtraSpinner 额外加载动画'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText(
                            '　　提供丰富的动画效果，可配合fac.AntdSpin或fac.AntdSkeleton使用。'
                        )
                    ]
                ),

                html.Div(
                    [
                        fac.AntdRow(
                            [
                                fac.AntdCol(
                                    html.Div(
                                        [
                                            fuc.FefferyExtraSpinner(
                                                type=_type
                                            ),
                                            fac.AntdText(
                                                _type,
                                                copyable=True
                                            )
                                        ],
                                        style={
                                            'textAlign': 'center'
                                        }
                                    ),
                                    xs=24,
                                    sm=12,
                                    md=8,
                                    lg=6,
                                    xl=4,
                                    xxl=4,
                                    style={
                                        'padding': '10px'
                                    }
                                )
                                for _type in [
                                    "ball", "swap", "bars", "grid", "wave", "push", "firework",
                                    "stage", "ring", "heart", "guard", "rotate", "spiral", "pulse",
                                    "swish", "sequence", "impulse", "cube", "magic", "flag", "fill",
                                    "sphere", "domino", "goo", "comb", "pong", "rainbow", "hoop",
                                    "flapper", "jellyfish", "trace", "classic", "whisper", "metro"
                                ]
                            ],
                            wrap=True
                        ),

                        fac.AntdDivider(
                            '基础使用',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdRow(
    [
        fac.AntdCol(
            html.Div(
                [
                    fuc.FefferyExtraSpinner(
                        type=_type
                    ),
                    fac.AntdText(
                        _type,
                        copyable=True
                    )
                ],
                style={
                    'textAlign': 'center'
                }
            ),
            xs=24,
            sm=12,
            md=8,
            lg=6,
            xl=4,
            xxl=4,
            style={
                'padding': '10px'
            }
        )
        for _type in [
            "ball", "swap", "bars", "grid", "wave", "push", "firework",
            "stage", "ring", "heart", "guard", "rotate", "spiral", "pulse",
            "swish", "sequence", "impulse", "cube", "magic", "flag", "fill",
            "sphere", "domino", "goo", "comb", "pong", "rainbow", "hoop",
            "flapper", "jellyfish", "trace", "classic", "whisper", "metro"
        ]
    ],
    wrap=True
)
'''
                            ),
                            title='点击查看代码',
                            is_open=False,
                            ghost=True
                        )
                    ],
                    style={
                        'marginBottom': '40px',
                        'padding': '10px 10px 20px 10px',
                        'border': '1px solid #f0f0f0'
                    },
                    id='基础使用',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdSpace(
                            [
                                fac.AntdSpace(
                                    [
                                        fac.AntdSelect(
                                            id='extra-spinner-demo-type',
                                            options=[
                                                {
                                                    'label': _type,
                                                    'value': _type
                                                }
                                                for _type in [
                                                    "ball", "swap", "bars", "grid", "wave", "push", "firework",
                                                    "stage", "ring", "heart", "guard", "rotate", "spiral", "pulse",
                                                    "swish", "sequence", "impulse", "cube", "magic", "flag", "fill",
                                                    "sphere", "domino", "goo", "comb", "pong", "rainbow", "hoop",
                                                    "flapper", "jellyfish", "trace", "classic", "whisper", "metro"
                                                ]
                                            ],
                                            allowClear=False,
                                            defaultValue='ball',
                                            style={
                                                'width': '100px'
                                            }
                                        ),
                                        fac.AntdButton(
                                            '触发时长5秒回调',
                                            id='extra-spinner-demo'
                                        )
                                    ]
                                ),

                                fac.AntdSpin(
                                    html.Div(
                                        datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                        id='extra-spinner-demo-output',
                                        style={
                                            'width': '100%',
                                            'height': '200px',
                                            'display': 'flex',
                                            'justifyContent': 'center',
                                            'alignItems': 'center',
                                            'boxShadow': '0px 0px 12px rgba(0, 0, 0, .12)',
                                            'borderRadius': '5px'
                                        }
                                    ),
                                    id='extra-spinner-demo-spin',
                                    delay=300,
                                    style={
                                        'display': 'flex',
                                        'justifyContent': 'center',
                                        'alignItems': 'center'
                                    }
                                )
                            ],
                            direction='vertical'
                        ),

                        fac.AntdDivider(
                            '配合fac.AntdSpin',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdSpace(
    [
        fac.AntdSpace(
            [
                fac.AntdSelect(
                    id='extra-spinner-demo-type',
                    options=[
                        {
                            'label': _type,
                            'value': _type
                        }
                        for _type in [
                            "ball", "swap", "bars", "grid", "wave", "push", "firework",
                            "stage", "ring", "heart", "guard", "rotate", "spiral", "pulse",
                            "swish", "sequence", "impulse", "cube", "magic", "flag", "fill",
                            "sphere", "domino", "goo", "comb", "pong", "rainbow", "hoop",
                            "flapper", "jellyfish", "trace", "classic", "whisper", "metro"
                        ]
                    ],
                    allowClear=False,
                    defaultValue='ball',
                    style={
                        'width': '100px'
                    }
                ),
                fac.AntdButton(
                    '触发时长5秒回调',
                    id='extra-spinner-demo'
                )
            ]
        ),

        fac.AntdSpin(
            html.Div(
                datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                id='extra-spinner-demo-output',
                style={
                    'width': '100%',
                    'height': '200px',
                    'display': 'flex',
                    'justifyContent': 'center',
                    'alignItems': 'center',
                    'boxShadow': '0px 0px 12px rgba(0, 0, 0, .12)',
                    'borderRadius': '5px'
                }
            ),
            id='extra-spinner-demo-spin',
            delay=300,
            style={
                'display': 'flex',
                'justifyContent': 'center',
                'alignItems': 'center'
            }
        )
    ],
    direction='vertical'
)

...

import time
from datetime import datetime

@app.callback(
    Output('extra-spinner-demo-output', 'children'),
    Input('extra-spinner-demo', 'nClicks'),
    prevent_initial_call=True
)
def extra_spinner_demo(nClicks):

    time.sleep(5)

    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


@app.callback(
    Output('extra-spinner-demo-spin', 'indicator'),
    Input('extra-spinner-demo-type', 'value')
)
def extra_spinner_demo_indicator(value):

    return fuc.FefferyExtraSpinner(
        type=value
    )
'''
                            ),
                            title='点击查看代码',
                            is_open=False,
                            ghost=True
                        )
                    ],
                    style={
                        'marginBottom': '40px',
                        'padding': '10px 10px 20px 10px',
                        'border': '1px solid #f0f0f0'
                    },
                    id='配合fac.AntdSpin',
                    className='div-highlight'
                ),

                html.Div(style={'height': '100px'})
            ],
            style={
                'flex': 'auto',
                'padding': '25px'
            }
        ),
        html.Div(
            fac.AntdAnchor(
                linkDict=[
                    {'title': '基础使用', 'href': '#基础使用'},
                    {'title': '配合fac.AntdSpin', 'href': '#配合fac.AntdSpin'},
                ],
                offsetTop=0
            ),
            style={
                'flex': 'none',
                'padding': '25px'
            }
        ),
        # 侧边参数栏
        render_side_props_layout(
            component_name='FefferyExtraSpinner'
        )
    ],
    style={
        'display': 'flex'
    }
)
