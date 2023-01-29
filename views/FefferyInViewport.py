from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_markdown_components as fmc

import callbacks.FefferyInViewport
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
                            'title': 'FefferyInViewport 元素可见性监听'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　用于监听目标元素是否在视口中可见。')
                    ]
                ),

                html.Div(
                    [
                        fuc.FefferyInViewport(
                            html.Div(
                                '向下滑动观察可见性变化',
                                style={
                                    'width': '300px',
                                    'height': '100px',
                                    'background': 'grey',
                                    'color': 'white',
                                    'display': 'flex',
                                    'justifyContent': 'center',
                                    'alignItems': 'center',
                                    'marginBottom': '300px'
                                }
                            ),
                            id='in-viewport-demo1'
                        ),

                        fac.AntdTitle(
                            id='in-viewport-demo1-output',
                            level=5,
                            style={
                                'marginBottom': '300px'
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
fuc.FefferyInViewport(
    html.Div(
        '向下滑动观察可见性变化',
        style={
            'width': '300px',
            'height': '100px',
            'background': 'grey',
            'color': 'white',
            'display': 'flex',
            'justifyContent': 'center',
            'alignItems': 'center',
            'marginBottom': '300px'
        }
    ),
    id='in-viewport-demo1'
),

fac.AntdTitle(
    id='in-viewport-demo1-output',
    level=5,
    style={
        'marginBottom': '300px'
    }
)

...

@app.callback(
    Output('in-viewport-demo1-output', 'children'),
    Input('in-viewport-demo1', 'inViewport')
)
def in_viewport_demo1(inViewport):

    return f'inViewport: {inViewport}'
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
                        fuc.FefferyInViewport(
                            fac.AntdSpace(
                                [
                                    html.Div(
                                        style={
                                            'width': '300px',
                                            'height': '150px',
                                            'background': 'green'
                                        }
                                    ),
                                    html.Div(
                                        style={
                                            'width': '300px',
                                            'height': '150px',
                                            'background': 'red'
                                        }
                                    )
                                ],
                                direction='vertical',
                                size=0
                            ),
                            id='in-viewport-demo2',
                            threshold=0.5
                        ),

                        fac.AntdTitle(
                            id='in-viewport-demo2-output',
                            level=5,
                            style={
                                'margin': '500px 0'
                            }
                        ),

                        fac.AntdDivider(
                            '设置显示比例阈值',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fmc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString='''
fuc.FefferyInViewport(
    fac.AntdSpace(
        [
            html.Div(
                style={
                    'width': '300px',
                    'height': '150px',
                    'background': 'green'
                }
            ),
            html.Div(
                style={
                    'width': '300px',
                    'height': '150px',
                    'background': 'red'
                }
            )
        ],
        direction='vertical',
        size=0
    ),
    id='in-viewport-demo2',
    threshold=0.5
),

fac.AntdTitle(
    id='in-viewport-demo2-output',
    level=5,
    style={
        'margin': '500px 0'
    }
)

...

@app.callback(
    Output('in-viewport-demo2-output', 'children'),
    Input('in-viewport-demo2', 'inViewport')
)
def in_viewport_demo2(inViewport):

    return f'inViewport: {inViewport}'
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
                    id='设置显示比例阈值',
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
                    {'title': '设置显示比例阈值', 'href': '#设置显示比例阈值'},
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
            component_name='FefferyInViewport'
        )
    ],
    style={
        'display': 'flex'
    }
)
