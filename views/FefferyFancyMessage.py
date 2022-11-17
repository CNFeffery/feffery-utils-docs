from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc

import callbacks.FefferyFancyMessage
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
                            'title': 'FefferyFancyMessage 美观消息提示'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　更美观、自定义程度更高的消息提示组件。')
                    ]
                ),

                html.Div(
                    [
                        fac.AntdSpace(
                            [
                                fac.AntdSelect(
                                    id='fancy-message-demo1-type',
                                    options=[
                                        {
                                            'label': type_,
                                            'value': type_
                                        }
                                        for type_ in [
                                            'blank', 'success', 'error'
                                        ]
                                    ],
                                    defaultValue='blank',
                                    allowClear=False,
                                    style={
                                        'width': '100px'
                                    }
                                ),
                                fac.AntdButton(
                                    '触发消息提示',
                                    id='trigger-fancy-message-demo1'
                                )
                            ]
                        ),

                        html.Div(
                            id='fancy-message-demo1-container'
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
fac.AntdSpace(
    [
        fac.AntdSelect(
            id='fancy-message-demo1-type',
            options=[
                {
                    'label': type_,
                    'value': type_
                }
                for type_ in [
                    'blank', 'success', 'error'
                ]
            ],
            defaultValue='blank',
            allowClear=False,
            style={
                'width': '100px'
            }
        ),
        fac.AntdButton(
            '触发消息提示',
            id='trigger-fancy-message-demo1'
        )
    ]
),

html.Div(
    id='fancy-message-demo1-container'
)

...

@app.callback(
    Output('fancy-message-demo1-container', 'children'),
    Input('trigger-fancy-message-demo1', 'nClicks'),
    State('fancy-message-demo1-type', 'value'),
    prevent_initial_call=True
)
def fancy_message_demo1(nClicks, message_type):

    return fuc.FefferyFancyMessage(
        'FefferyFancyMessage示例',
        id='fancy-message-demo2',
        type=message_type,
        visible=True
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
                                fac.AntdSelect(
                                    id='fancy-message-demo2-position',
                                    options=[
                                        {
                                            'label': position,
                                            'value': position
                                        }
                                        for position in [
                                            'top-left', 'top-center', 'top-right',
                                            'bottom-left', 'bottom-center', 'bottom-right'
                                        ]
                                    ],
                                    defaultValue='top-left',
                                    allowClear=False,
                                    style={
                                        'width': '150px'
                                    }
                                ),
                                fac.AntdButton(
                                    '触发消息提示',
                                    id='trigger-fancy-message-demo2'
                                )
                            ]
                        ),

                        html.Div(
                            id='fancy-message-demo2-container'
                        ),

                        fac.AntdDivider(
                            '自定义弹出方位',
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
        fac.AntdSelect(
            id='fancy-message-demo2-position',
            options=[
                {
                    'label': position,
                    'value': position
                }
                for position in [
                    'top-left', 'top-center', 'top-right',
                    'bottom-left', 'bottom-center', 'bottom-right'
                ]
            ],
            defaultValue='top-left',
            allowClear=False,
            style={
                'width': '150px'
            }
        ),
        fac.AntdButton(
            '触发消息提示',
            id='trigger-fancy-message-demo2'
        )
    ]
),

html.Div(
    id='fancy-message-demo2-container'
)

...

@app.callback(
    Output('fancy-message-demo2-container', 'children'),
    Input('trigger-fancy-message-demo2', 'nClicks'),
    State('fancy-message-demo2-position', 'value'),
    prevent_initial_call=True
)
def fancy_message_demo2(nClicks, position):

    return fuc.FefferyFancyMessage(
        'FefferyFancyMessage示例',
        id='fancy-message-demo2',
        position=position,
        visible=True,
        type='success'
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
                    id='自定义弹出方位',
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
                    {'title': '自定义弹出方位', 'href': '#自定义弹出方位'},
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
            component_name='FefferyFancyMessage'
        )
    ],
    style={
        'display': 'flex'
    }
)
