from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_markdown_components as fmc

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
                                    id='fancy-message-demo-type',
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
                                fac.AntdSelect(
                                    id='fancy-message-demo-position',
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
                                    defaultValue='top-center',
                                    allowClear=False,
                                    style={
                                        'width': '150px'
                                    }
                                ),
                                fac.AntdButton(
                                    '触发消息提示',
                                    id='trigger-fancy-message-demo'
                                )
                            ]
                        ),

                        html.Div(
                            id='fancy-message-demo-container'
                        ),

                        fac.AntdDivider(
                            '基础使用',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fmc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdSpace(
    [
        fac.AntdSelect(
            id='fancy-message-demo-type',
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
        fac.AntdSelect(
            id='fancy-message-demo-position',
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
            defaultValue='top-center',
            allowClear=False,
            style={
                'width': '150px'
            }
        ),
        fac.AntdButton(
            '触发消息提示',
            id='trigger-fancy-message-demo'
        )
    ]
),

html.Div(
    id='fancy-message-demo-container'
)

...

@app.callback(
    Output('fancy-message-demo-container', 'children'),
    Input('trigger-fancy-message-demo', 'nClicks'),
    [State('fancy-message-demo-type', 'value'),
     State('fancy-message-demo-position', 'value')],
    prevent_initial_call=True
)
def fancy_message_demo(nClicks, message_type, message_position):

    return fuc.FefferyFancyMessage(
        'FefferyFancyMessage示例',
        id='fancy-message-demo',
        type=message_type,
        position=message_position
    )
'''
                            ),
                            title='点击查看代码',
                            isOpen=False,
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
                    {'title': '基础使用', 'href': '#基础使用'}
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
