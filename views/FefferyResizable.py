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
                            'title': 'FefferyResizable 尺寸调整'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　用于提供可自由调整尺寸大小的容器。')
                    ]
                ),

                html.Div(
                    [
                        fuc.FefferyResizable(
                            html.Div(
                                '示例内容',
                                style={
                                    'display': 'flex',
                                    'height': '100%',
                                    'justifyContent': 'center',
                                    'alignItems': 'center',
                                    'background': '#dee2e6'
                                }
                            ),
                            defaultSize={
                                'width': 200,
                                'height': 200
                            }
                        ),

                        fac.AntdDivider(
                            '基础使用',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                '默认参数下尺寸调整组件可从8个方向上进行尺寸调整'
                            ],
                            style={
                                'textIndent': '2rem'
                            }
                        ),

                        fac.AntdCollapse(
                            fmc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString='''
fuc.FefferyResizable(
    html.Div(
        '示例内容',
        style={
            'display': 'flex',
            'height': '100%',
            'justifyContent': 'center',
            'alignItems': 'center',
            'background': '#dee2e6'
        }
    ),
    defaultSize={
        'width': 200,
        'height': 200
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
                        html.Div(
                            [
                                fuc.FefferyResizable(
                                    html.Div(
                                        '示例内容',
                                        style={
                                            'display': 'flex',
                                            'height': '100%',
                                            'justifyContent': 'center',
                                            'alignItems': 'center',
                                            'background': '#dee2e6'
                                        }
                                    ),
                                    defaultSize={
                                        'width': 200,
                                        'height': 200
                                    },
                                    bounds='parent'
                                )
                            ],
                            style={
                                'height': 400,
                                'width': 400,
                                'border': '1px solid #868e96'
                            }
                        ),

                        fac.AntdDivider(
                            '限制父元素内可调',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fmc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString='''
html.Div(
    [
        fuc.FefferyResizable(
            html.Div(
                '示例内容',
                style={
                    'display': 'flex',
                    'height': '100%',
                    'justifyContent': 'center',
                    'alignItems': 'center',
                    'background': '#dee2e6'
                }
            ),
            defaultSize={
                'width': 200,
                'height': 200
            },
            bounds='parent'
        )
    ],
    style={
        'height': 400,
        'width': 400,
        'border': '1px solid #868e96'
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
                    id='限制父元素内可调',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdSpace(
                            [
                                fuc.FefferyResizable(
                                    html.Div(
                                        "direction=['right']",
                                        style={
                                            'display': 'flex',
                                            'height': '100%',
                                            'justifyContent': 'center',
                                            'alignItems': 'center',
                                            'background': '#dee2e6'
                                        }
                                    ),
                                    defaultSize={
                                        'width': 200,
                                        'height': 200
                                    },
                                    direction=['right']
                                ),
                                fuc.FefferyResizable(
                                    html.Div(
                                        "direction=['right', 'bottom', 'bottomRight']",
                                        style={
                                            'display': 'flex',
                                            'height': '100%',
                                            'justifyContent': 'center',
                                            'alignItems': 'center',
                                            'background': '#dee2e6'
                                        }
                                    ),
                                    defaultSize={
                                        'width': 300,
                                        'height': 300
                                    },
                                    direction=[
                                        'right', 'bottom', 'bottomRight'
                                    ]
                                )
                            ],
                            direction='vertical',
                            style={
                                'width': '100%'
                            }
                        ),

                        fac.AntdDivider(
                            '仅允许部分方向可调',
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
        fuc.FefferyResizable(
            html.Div(
                "direction=['right']",
                style={
                    'display': 'flex',
                    'height': '100%',
                    'justifyContent': 'center',
                    'alignItems': 'center',
                    'background': '#dee2e6'
                }
            ),
            defaultSize={
                'width': 200,
                'height': 200
            },
            direction=['right']
        ),
        fuc.FefferyResizable(
            html.Div(
                "direction=['right', 'bottom', 'bottomRight']",
                style={
                    'display': 'flex',
                    'height': '100%',
                    'justifyContent': 'center',
                    'alignItems': 'center',
                    'background': '#dee2e6'
                }
            ),
            defaultSize={
                'width': 300,
                'height': 300
            },
            direction=[
                'right', 'bottom', 'bottomRight'
            ]
        )
    ],
    direction='vertical',
    style={
        'width': '100%'
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
                    id='仅允许部分方向可调',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fuc.FefferyStyle(
                            rawStyle='''
.custom-right-resize-handle:hover, .custom-right-resize-handle:active {
    background: #007fd4;
    transition: 0.3s background;
}

.custom-right-resize-handle {
    transition: 0.3s background;
    width: 4px !important;
    right: -2px !important;
}
'''
                        ),
                        fuc.FefferyResizable(
                            html.Div(
                                "direction=['right']",
                                style={
                                    'display': 'flex',
                                    'height': '100%',
                                    'justifyContent': 'center',
                                    'alignItems': 'center',
                                    'background': '#dee2e6'
                                }
                            ),
                            defaultSize={
                                'width': 200,
                                'height': 200
                            },
                            direction=['right'],
                            handleClassNames={
                                'right': 'custom-right-resize-handle'
                            },
                            bounds='parent'
                        ),

                        fac.AntdDivider(
                            '自定义拖拽控件样式',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fmc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString="""
fuc.FefferyStyle(
    rawStyle='''
.custom-right-resize-handle:hover, .custom-right-resize-handle:active {
    background: #007fd4;
    transition: 0.3s background;
}

.custom-right-resize-handle {
    transition: 0.3s background;
    width: 4px !important;
    right: -2px !important;
}
'''
),
fuc.FefferyResizable(
    html.Div(
        "direction=['right']",
        style={
            'display': 'flex',
            'height': '100%',
            'justifyContent': 'center',
            'alignItems': 'center',
            'background': '#dee2e6'
        }
    ),
    defaultSize={
        'width': 200,
        'height': 200
    },
    direction=['right'],
    handleClassNames={
        'right': 'custom-right-resize-handle'
    },
    bounds='parent'
)
"""
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
                    id='自定义拖拽控件样式',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fuc.FefferyResizable(
                            html.Div(
                                '示例内容',
                                style={
                                    'display': 'flex',
                                    'height': '100%',
                                    'justifyContent': 'center',
                                    'alignItems': 'center',
                                    'background': '#dee2e6'
                                }
                            ),
                            defaultSize={
                                'width': 200,
                                'height': 200
                            },
                            minWidth=100,
                            minHeight=100,
                            maxWidth=400,
                            maxHeight=400
                        ),

                        fac.AntdDivider(
                            '限制可调范围',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fmc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString='''
fuc.FefferyResizable(
    html.Div(
        '示例内容',
        style={
            'display': 'flex',
            'height': '100%',
            'justifyContent': 'center',
            'alignItems': 'center',
            'background': '#dee2e6'
        }
    ),
    defaultSize={
        'width': 200,
        'height': 200
    },
    minWidth=100,
    minHeight=100,
    maxWidth=400,
    maxHeight=400
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
                    id='限制可调范围',
                    className='div-highlight'
                ),

                html.Div(style={'height': '100px'})
            ],
            style={
                'flex': 'auto',
                'padding': '25px',
                'width': 0
            }
        ),
        html.Div(
            fac.AntdAnchor(
                linkDict=[
                    {'title': '基础使用', 'href': '#基础使用'},
                    {'title': '限制父元素内可调', 'href': '#限制父元素内可调'},
                    {'title': '仅允许部分方向可调', 'href': '#仅允许部分方向可调'},
                    {'title': '自定义拖拽控件样式', 'href': '#自定义拖拽控件样式'},
                    {'title': '限制可调范围', 'href': '#限制可调范围'}
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
            component_name='FefferyResizable'
        )
    ],
    style={
        'display': 'flex'
    }
)
