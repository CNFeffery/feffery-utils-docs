from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc

import callbacks.FefferyFancyNotification
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
                            'title': 'FefferyFancyNotification 美观通知'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　更美观、自定义程度更高的通知框组件。')
                    ]
                ),

                html.Div(
                    [
                        fac.AntdSpace(
                            [
                                fac.AntdSelect(
                                    id='fancy-notification-demo-type',
                                    options=[
                                        {
                                            'label': type_,
                                            'value': type_
                                        }
                                        for type_ in [
                                            'info', 'success', 'warning', 'error'
                                        ]
                                    ],
                                    defaultValue='info',
                                    allowClear=False,
                                    style={
                                        'width': '100px'
                                    }
                                ),
                                fac.AntdSelect(
                                    id='fancy-notification-demo-position',
                                    options=[
                                        {
                                            'label': position,
                                            'value': position
                                        }
                                        for position in [
                                            'top-left', 'top-center', 'top-right', 'bottom-left', 'bottom-center', 'bottom-right'
                                        ]
                                    ],
                                    defaultValue='top-right',
                                    allowClear=False,
                                    style={
                                        'width': '125px'
                                    }
                                ),
                                fac.AntdSelect(
                                    id='fancy-notification-demo-theme',
                                    options=[
                                        {
                                            'label': theme,
                                            'value': theme
                                        }
                                        for theme in [
                                            'light', 'dark', 'colored'
                                        ]
                                    ],
                                    defaultValue='light',
                                    allowClear=False,
                                    style={
                                        'width': '100px'
                                    }
                                ),
                                fac.AntdButton(
                                    '触发通知框',
                                    id='trigger-fancy-notification-demo'
                                )
                            ]
                        ),

                        html.Div(
                            id='fancy-notification-demo-container'
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
            id='fancy-notification-demo-type',
            options=[
                {
                    'label': type_,
                    'value': type_
                }
                for type_ in [
                    'info', 'success', 'warning', 'error'
                ]
            ],
            defaultValue='info',
            allowClear=False,
            style={
                'width': '100px'
            }
        ),
        fac.AntdSelect(
            id='fancy-notification-demo-position',
            options=[
                {
                    'label': position,
                    'value': position
                }
                for position in [
                    'top-left', 'top-center', 'top-right', 'bottom-left', 'bottom-center', 'bottom-right'
                ]
            ],
            defaultValue='top-right',
            allowClear=False,
            style={
                'width': '125px'
            }
        ),
        fac.AntdSelect(
            id='fancy-notification-demo-theme',
            options=[
                {
                    'label': theme,
                    'value': theme
                }
                for theme in [
                    'light', 'dark', 'colored'
                ]
            ],
            defaultValue='light',
            allowClear=False,
            style={
                'width': '100px'
            }
        ),
        fac.AntdButton(
            '触发通知框',
            id='trigger-fancy-notification-demo'
        )
    ]
),

html.Div(
    id='fancy-notification-demo-container'
)

...

@app.callback(
    Output('fancy-notification-demo-container', 'children'),
    Input('trigger-fancy-notification-demo', 'nClicks'),
    [State('fancy-notification-demo-type', 'value'),
     State('fancy-notification-demo-position', 'value'),
     State('fancy-notification-demo-theme', 'value')],
    prevent_initial_call=True
)
def fancy_notification_demo(nClicks,
                            notification_type,
                            notification_position,
                            notification_theme):

    return fuc.FefferyFancyNotification(
        'FefferyFancyNotification示例',
        id='fancy-notification-demo',
        type=notification_type,
        position=notification_position,
        theme=notification_theme
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
            component_name='FefferyFancyNotification'
        )
    ],
    style={
        'display': 'flex'
    }
)
