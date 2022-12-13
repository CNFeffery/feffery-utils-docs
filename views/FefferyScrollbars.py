from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc

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
                            'title': 'FefferyScrollbars 滚动条容器'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　更美观的局部滚动条容器方案。')
                    ]
                ),

                html.Div(
                    [
                        fuc.FefferyScrollbars(
                            fac.AntdParagraph(
                                '请将鼠标移入本区域进行滚动\n'*100,
                                style={
                                    'whiteSpace': 'pre'
                                }
                            ),
                            style={
                                'maxHeight': '150px',
                                'maxWidth': '200px',
                                'border': '1px dashed #e1dfdd'
                            }
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
fuc.FefferyScrollbars(
    fac.AntdParagraph(
        '请将鼠标移入本区域进行滚动\\n'*100,
        style={
            'whiteSpace': 'pre'
        }
    ),
    style={
        'maxHeight': '150px',
        'maxWidth': '200px',
        'border': '1px dashed #e1dfdd'
    }
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
                        fuc.FefferyScrollbars(
                            [
                                fac.AntdParagraph(
                                    '请将鼠标移入本区域进行滚动'*5,
                                    style={
                                        'whiteSpace': 'pre'
                                    }
                                )
                            ] * 5,
                            style={
                                'maxHeight': '150px',
                                'maxWidth': '200px',
                                'border': '1px dashed #e1dfdd'
                            }
                        ),

                        fac.AntdDivider(
                            '水平方向',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString='''
fuc.FefferyScrollbars(
    [
        fac.AntdParagraph(
            '请将鼠标移入本区域进行滚动'*5,
            style={
                'whiteSpace': 'pre'
            }
        )
    ] * 5,
    style={
        'maxHeight': '150px',
        'maxWidth': '200px',
        'border': '1px dashed #e1dfdd'
    }
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
                    id='水平方向',
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
                    {'title': '水平方向', 'href': '#水平方向'}
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
            component_name='FefferyScrollbars'
        )
    ],
    style={
        'display': 'flex'
    }
)
