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
                            'title': 'FefferyQRCode 二维码生成'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　用于生成展示常规的二维码。')
                    ]
                ),

                html.Div(
                    [
                        fac.AntdSpace(
                            [
                                fuc.FefferyQRCode(
                                    value='FefferyQRCode示例'
                                ),
                                fuc.FefferyQRCode(
                                    value='FefferyQRCode示例',
                                    size=64
                                ),
                                fuc.FefferyQRCode(
                                    value='FefferyQRCode示例',
                                    size=256
                                )
                            ],
                            direction='vertical'
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
        fuc.FefferyQRCode(
            value='FefferyQRCode示例'
        ),
        fuc.FefferyQRCode(
            value='FefferyQRCode示例',
            size=64
        ),
        fuc.FefferyQRCode(
            value='FefferyQRCode示例',
            size=256
        )
    ],
    direction='vertical'
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
                                fac.AntdDivider(
                                    '默认level="L"',
                                    innerTextOrientation='left'
                                ),
                                fuc.FefferyQRCode(
                                    value='FefferyQRCode示例'
                                ),
                                fac.AntdDivider(
                                    'level="M"',
                                    innerTextOrientation='left'
                                ),
                                fuc.FefferyQRCode(
                                    value='FefferyQRCode示例',
                                    level='M'
                                ),
                                fac.AntdDivider(
                                    'level="Q"',
                                    innerTextOrientation='left'
                                ),
                                fuc.FefferyQRCode(
                                    value='FefferyQRCode示例',
                                    level='Q'
                                ),
                                fac.AntdDivider(
                                    'level="H"',
                                    innerTextOrientation='left'
                                ),
                                fuc.FefferyQRCode(
                                    value='FefferyQRCode示例',
                                    level='H'
                                )
                            ],
                            direction='vertical',
                            style={
                                'width': '100%'
                            }
                        ),

                        fac.AntdDivider(
                            '不同的精确水平',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                fac.AntdText(
                                    '　　更高的精确水平意味着更复杂的二维码，以及更多的生成耗时，常规使用场景下，默认的'
                                ),
                                fac.AntdText('"L"', code=True),
                                fac.AntdText('足矣')
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
        fac.AntdDivider(
            '默认level="L"',
            innerTextOrientation='left'
        ),
        fuc.FefferyQRCode(
            value='FefferyQRCode示例'
        ),
        fac.AntdDivider(
            'level="M"',
            innerTextOrientation='left'
        ),
        fuc.FefferyQRCode(
            value='FefferyQRCode示例',
            level='M'
        ),
        fac.AntdDivider(
            'level="Q"',
            innerTextOrientation='left'
        ),
        fuc.FefferyQRCode(
            value='FefferyQRCode示例',
            level='Q'
        ),
        fac.AntdDivider(
            'level="H"',
            innerTextOrientation='left'
        ),
        fuc.FefferyQRCode(
            value='FefferyQRCode示例',
            level='H'
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
                    id='不同的精确水平',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdSpace(
                            [
                                fuc.FefferyQRCode(
                                    value='https://fuc.feffery.tech',
                                    imageSettings={
                                        'src': '/assets/imgs/fuc-logo.svg',
                                        'width': 30,
                                        'height': 30
                                    }
                                ),
                                fuc.FefferyQRCode(
                                    value='https://fac.feffery.tech',
                                    imageSettings={
                                        'src': 'https://fac.feffery.tech/assets/imgs/fac-logo.svg',
                                        'width': 50,
                                        'height': 50
                                    },
                                    size=256
                                )
                            ],
                            direction='vertical'
                        ),

                        fac.AntdDivider(
                            '嵌入图片',
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
        fuc.FefferyQRCode(
            value='https://fuc.feffery.tech',
            imageSettings={
                'src': '/assets/imgs/fuc-logo.svg',
                'width': 30,
                'height': 30
            }
        ),
        fuc.FefferyQRCode(
            value='https://fac.feffery.tech',
            imageSettings={
                'src': 'https://fac.feffery.tech/assets/imgs/fac-logo.svg',
                'width': 50,
                'height': 50
            },
            size=256
        )
    ],
    direction='vertical'
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
                    id='嵌入图片',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdSpace(
                            [
                                fac.AntdDivider(
                                    '默认renderer="svg"',
                                    innerTextOrientation='left'
                                ),
                                fuc.FefferyQRCode(
                                    value='renderer="svg"'
                                ),
                                fac.AntdDivider(
                                    '默认renderer="canvas"',
                                    innerTextOrientation='left'
                                ),
                                fuc.FefferyQRCode(
                                    value='renderer="canvas"',
                                    renderer='canvas'
                                )
                            ],
                            direction='vertical',
                            style={
                                'width': '100%'
                            }
                        ),

                        fac.AntdDivider(
                            '不同的渲染模式',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                fac.AntdText('　　当渲染模式为'),
                                fac.AntdText('"canvas"', code=True),
                                fac.AntdText('时，可像常规图片那样对二维码右键复制或另存为图片')
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
        fac.AntdDivider(
            '默认renderer="svg"',
            innerTextOrientation='left'
        ),
        fuc.FefferyQRCode(
            value='renderer="svg"'
        ),
        fac.AntdDivider(
            '默认renderer="canvas"',
            innerTextOrientation='left'
        ),
        fuc.FefferyQRCode(
            value='renderer="canvas"',
            renderer='canvas'
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
                    id='不同的渲染模式',
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
                    {'title': '不同的精确水平', 'href': '#不同的精确水平'},
                    {'title': '嵌入图片', 'href': '#嵌入图片'},
                    {'title': '不同的渲染模式', 'href': '#不同的渲染模式'},
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
            component_name='FefferyQRCode'
        )
    ],
    style={
        'display': 'flex'
    }
)
