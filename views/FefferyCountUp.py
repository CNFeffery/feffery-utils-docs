from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_markdown_components as fmc

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
                            'title': 'FefferyCountUp 数字递增'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　用于渲染以指定数值为目标的递增动画效果。')
                    ]
                ),

                html.Div(
                    [
                        fac.AntdSpace(
                            [
                                fuc.FefferyCountUp(
                                    end=99999
                                ),

                                fuc.FefferyCountUp(
                                    end=-99999
                                )
                            ],
                            style={
                                'fontSize': 18
                            }
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
        fuc.FefferyCountUp(
            end=99999
        ),

        fuc.FefferyCountUp(
            end=-99999
        )
    ],
    style={
        'fontSize': 18
    }
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
                                fuc.FefferyCountUp(
                                    end=99999,
                                    duration=5
                                ),

                                fuc.FefferyCountUp(
                                    end=-99999,
                                    duration=5
                                )
                            ],
                            style={
                                'fontSize': 18
                            }
                        ),

                        fac.AntdDivider(
                            '增大动画时长',
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
        fuc.FefferyCountUp(
            end=99999,
            duration=5
        ),

        fuc.FefferyCountUp(
            end=-99999,
            duration=5
        )
    ],
    style={
        'fontSize': 18
    }
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
                    id='增大动画时长',
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
                    {'title': '增大动画时长', 'href': '#增大动画时长'},
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
            component_name='FefferyCountUp'
        )
    ],
    style={
        'display': 'flex'
    }
)
