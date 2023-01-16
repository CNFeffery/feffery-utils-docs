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
                            'title': 'FefferySticky 粘性布局'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　用于快捷实现基础及进阶的粘性布局效果。')
                    ]
                ),

                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    style={
                                        'height': '200px'
                                    }
                                ),
                                fuc.FefferySticky(
                                    fac.AntdTag(
                                        color='green',
                                        content='请向下滚动查看效果'
                                    ),
                                    top=25,
                                    bottomBoundary=800
                                ),
                                html.Div(
                                    style={
                                        'height': '1200px'
                                    }
                                )
                            ]
                        ),

                        fac.AntdDivider(
                            '基础使用',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                fac.AntdText(
                                    '在这个例子中，示例元素受参数top设置的影响，在距离页面顶端25px时进入粘性状态，随着继续下滑，在参数bottomBoundary设置的影响下，距离文档顶端绝对距离超出800px时随之解除粘性状态'
                                )
                            ],
                            style={
                                'textIndent': '2rem'
                            }
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString='''
html.Div(
    [
        html.Div(
            style={
                'height': '200px'
            }
        ),
        fuc.FefferySticky(
            fac.AntdTag(
                color='green',
                content='请向下滚动查看效果'
            ),
            top=25,
            bottomBoundary=800
        ),
        html.Div(
            style={
                'height': '1200px'
            }
        )
    ]
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
                                fac.AntdRow(
                                    [
                                        fac.AntdCol(
                                            fuc.FefferySticky(
                                                fac.AntdTitle(
                                                    f'章节{i}',
                                                    level=4,
                                                    style={
                                                        'textAlign': 'center'
                                                    }
                                                ),
                                                top=100,
                                                bottomBoundary=f'#sticky-target-block{i}',
                                                zIndex=999-i
                                            ),
                                            flex='none',
                                            style={
                                                'width': '140px'
                                            }
                                        ),

                                        fac.AntdCol(
                                            html.Div(
                                                id=f'sticky-target-block{i}',
                                                style={
                                                    'height': '800px',
                                                    'background': '#f2f3f5',
                                                    'marginBottom': '25px'
                                                }
                                            ),
                                            flex='auto'
                                        )
                                    ]
                                )
                                for i in range(5)
                            ],
                            direction='vertical',
                            style={
                                'width': '100%'
                            }
                        ),

                        fac.AntdDivider(
                            '以具体元素为参照物',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                fac.AntdText(
                                    '通过向top或bottomBoundary参数传入css选择器规则，配合zIndex参数以实现更为灵活的页面布局效果'
                                )
                            ],
                            style={
                                'textIndent': '2rem'
                            }
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdSpace(
    [
        fac.AntdRow(
            [
                fac.AntdCol(
                    fuc.FefferySticky(
                        fac.AntdTitle(
                            f'章节{i}',
                            level=4,
                            style={
                                'textAlign': 'center'
                            }
                        ),
                        top=100,
                        bottomBoundary=f'#sticky-target-block{i}',
                        zIndex=999-i
                    ),
                    flex='none',
                    style={
                        'width': '140px'
                    }
                ),

                fac.AntdCol(
                    html.Div(
                        id=f'sticky-target-block{i}',
                        style={
                            'height': '800px',
                            'background': '#f2f3f5',
                            'marginBottom': '25px'
                        }
                    ),
                    flex='auto'
                )
            ]
        )
        for i in range(5)
    ],
    direction='vertical',
    style={
        'width': '100%'
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
                    id='以具体元素为参照物',
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
                    {'title': '以具体元素为参照物', 'href': '#以具体元素为参照物'}
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
            component_name='FefferySticky'
        )
    ],
    style={
        'display': 'flex'
    }
)
