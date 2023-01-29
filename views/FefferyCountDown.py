from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_markdown_components as fmc

import callbacks.FefferyCountDown
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
                            'title': 'FefferyCountDown 倒计时'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　构建以指定时长为结束终点的倒计时功能。')
                    ]
                ),

                html.Div(
                    [
                        fac.AntdSpace(
                            [
                                fac.AntdButton(
                                    '倒计时10秒',
                                    id='trigger-count-down-demo1',
                                    type='primary'
                                ),

                                fac.AntdText(
                                    id='count-down-demo1-output'
                                ),

                                fuc.FefferyCountDown(
                                    id='count-down-demo1'
                                )
                            ],
                            direction='vertical'
                        ),

                        fac.AntdDivider(
                            '基础使用',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                fac.AntdText(
                                    '　　每次有效的delay被设置后，且目标倒计时组件没有正在进行中的倒计时过程时，都会启动新的倒计时过程。'
                                )
                            ]
                        ),

                        fac.AntdCollapse(
                            fmc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdSpace(
    [
        fac.AntdButton(
            '倒计时10秒',
            id='trigger-count-down-demo1',
            type='primary'
        ),

        fac.AntdText(
            id='count-down-demo1-output'
        ),

        fuc.FefferyCountDown(
            id='count-down-demo1'
        )
    ],
    direction='vertical'
)        

...

@app.callback(
    Output('count-down-demo1', 'delay'),
    Input('trigger-count-down-demo1', 'nClicks'),
    prevent_initial_call=True
)
def countdown_demo1_trigger(nClicks):

    return 10


@app.callback(
    Output('count-down-demo1-output', 'children'),
    Input('count-down-demo1', 'countdown'),
    prevent_initial_call=True
)
def countdown_demo1_update(countdown):

    if countdown == 0:
        return

    return f'还剩{countdown}秒'
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
                        fac.AntdButton(
                            '刷新示例',
                            id='refresh-count-down-demo2',
                            type='primary'
                        ),
                        html.Div(
                            id='count-down-demo2-container'
                        ),

                        fac.AntdDivider(
                            '典型应用场景',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fmc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdButton(
    '刷新示例',
    id='refresh-count-down-demo2',
    type='primary'
),
html.Div(
    id='count-down-demo2-container'
)

...

@app.callback(
    Output('count-down-demo2-container', 'children'),
    Input('refresh-count-down-demo2', 'nClicks'),
    prevent_initial_call=True
)
def countdown_demo2_refresh(nClicks):

    return html.Div(
        [
            html.Div(
                '用户须知：'+'巴拉巴拉'*200,
                style={
                    'borderBottom': '1px solid #bfbfbf',
                    'paddingBottom': '15px',
                    'maxHeight': '400px',
                    'overflowY': 'auto'
                }
            ),
            fac.AntdButton(
                '我已知晓用户须知内容',
                id='count-down-demo2-output',
                type='primary',
                block=True,
                disabled=True,
                style={
                    'marginTop': '15px'
                }
            ),
            fuc.FefferyCountDown(
                id='count-down-demo2',
                delay=10
            )
        ],
        # 强制刷新用
        id=str(uuid.uuid4()),
        style={
            'border': '1px solid #bfbfbf',
            'padding': '20px',
            'width': '300px'
        }
    )


@app.callback(
    [Output('count-down-demo2-output', 'children'),
     Output('count-down-demo2-output', 'disabled')],
    Input('count-down-demo2', 'countdown')
)
def countdown_demo2(countdown):

    if countdown == 0:
        return [
            '我已知晓用户须知内容',
            False
        ]

    return [
        f'我已知晓用户须知内容（{countdown}s）',
        True
    ]
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
                    id='典型应用场景',
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
                    {'title': '典型应用场景', 'href': '#典型应用场景'}
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
            component_name='FefferyCountDown'
        )
    ],
    style={
        'display': 'flex'
    }
)
