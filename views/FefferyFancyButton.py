from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_markdown_components as fmc

import callbacks.FefferyFancyButton
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
                            'title': 'FefferyFancyButton 美观按钮'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　另一种风格的美观按钮。')
                    ]
                ),

                html.Div(
                    [
                        fac.AntdSpace(
                            [
                                fuc.FefferyFancyButton(
                                    type_,
                                    type=type_
                                )
                                for type_ in ['primary', 'secondary', 'danger']
                            ]
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
        fuc.FefferyFancyButton(
            type_,
            type=type_
        )
        for type_ in ['primary', 'secondary', 'danger']
    ]
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

                html.Div(
                    [
                        fac.AntdSpace(
                            [
                                fuc.FefferyFancyButton(
                                    type_,
                                    type=type_,
                                    ripple=True
                                )
                                for type_ in ['primary', 'secondary', 'danger']
                            ]
                        ),

                        fac.AntdDivider(
                            '点击涟漪效果',
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
        fuc.FefferyFancyButton(
            type_,
            type=type_,
            ripple=True
        )
        for type_ in ['primary', 'secondary', 'danger']
    ]
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
                    id='点击涟漪效果',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdSpace(
                            [
                                fuc.FefferyFancyButton(
                                    '无防抖',
                                    id='fancy-button1'
                                ),
                                fac.AntdText(
                                    id='fancy-button-output1'
                                )
                            ],
                            style={
                                'marginBottom': 10
                            }
                        ),

                        html.Br(),

                        fac.AntdSpace(
                            [
                                fuc.FefferyFancyButton(
                                    '500ms防抖',
                                    id='fancy-button2',
                                    debounceWait=500
                                ),
                                fac.AntdText(
                                    id='fancy-button-output2'
                                )
                            ]
                        ),

                        fac.AntdDivider(
                            '回调示例',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                fac.AntdText(
                                    '　　使用防抖特性可以避免快速连击导致的回调频繁触发'
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
        fuc.FefferyFancyButton(
            '无防抖',
            id='fancy-button1'
        ),
        fac.AntdText(
            id='fancy-button-output1'
        )
    ],
    style={
        'marginBottom': 10
    }
),

html.Br(),

fac.AntdSpace(
    [
        fuc.FefferyFancyButton(
            '500ms防抖',
            id='fancy-button2',
            debounceWait=500
        ),
        fac.AntdText(
            id='fancy-button-output2'
        )
    ]
)

...

@app.callback(
    Output('fancy-button-output1', 'children'),
    Input('fancy-button1', 'nClicks'),
    prevent_initial_call=True
)
def fancy_button_demo1(nClicks):

    return f'nClicks: {nClicks}'

@app.callback(
    Output('fancy-button-output2', 'children'),
    Input('fancy-button2', 'nClicks'),
    prevent_initial_call=True
)
def fancy_button_demo2(nClicks):

    return f'nClicks: {nClicks}'
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
                    id='回调示例',
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
                    {'title': '点击涟漪效果', 'href': '#点击涟漪效果'},
                    {'title': '回调示例', 'href': '#回调示例'},
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
            component_name='FefferyFancyButton'
        )
    ],
    style={
        'display': 'flex'
    }
)
