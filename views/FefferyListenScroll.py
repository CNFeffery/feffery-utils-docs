from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_markdown_components as fmc

import callbacks.FefferyListenScroll
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
                            'title': 'FefferyListenScroll 滚动条监听'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　用于监听目标容器或整个页面的当前滚动条位置。')
                    ]
                ),

                html.Div(
                    [
                        fuc.FefferyListenScroll(
                            id='listen-scroll-demo'
                        ),

                        html.Pre(
                            id='listen-scroll-demo-output'
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
                                codeString="""
fuc.FefferyListenScroll(
    id='listen-scroll-demo'
),

html.Pre(
    id='listen-scroll-demo-output'
)

...

app.clientside_callback(
    '''( position ) => JSON.stringify(position)''',
    Output('listen-scroll-demo-output', 'children'),
    Input('listen-scroll-demo', 'position')
)
"""
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
                        fuc.FefferyListenScroll(
                            id='listen-scroll-target-demo',
                            target='listen-scroll-target-container'
                        ),

                        html.Div(
                            html.Div(
                                style={
                                    'width': 10000,
                                    'height': 10000
                                }
                            ),
                            id='listen-scroll-target-container',
                            style={
                                'border': '1px solid #dee2e6',
                                'width': 200,
                                'height': 150,
                                'overflow': 'auto'
                            }
                        ),

                        html.Pre(
                            id='listen-scroll-target-demo-output'
                        ),

                        fac.AntdDivider(
                            '绑定目标容器',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fmc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString="""
fuc.FefferyListenScroll(
    id='listen-scroll-target-demo',
    target='listen-scroll-target-container'
),

html.Div(
    html.Div(
        style={
            'width': 10000,
            'height': 10000
        }
    ),
    id='listen-scroll-target-container',
    style={
        'border': '1px solid #dee2e6',
        'width': 200,
        'height': 150,
        'overflow': 'auto'
    }
),

html.Pre(
    id='listen-scroll-target-demo-output'
)

...

app.clientside_callback(
    '''( position ) => JSON.stringify(position)''',
    Output('listen-scroll-demo-output', 'children'),
    Input('listen-scroll-demo', 'position')
)


app.clientside_callback(
    '''( position ) => JSON.stringify(position)''',
    Output('listen-scroll-target-demo-output', 'children'),
    Input('listen-scroll-target-demo', 'position')
)
"""
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
                    id='绑定目标容器',
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
                    {'title': '绑定目标容器', 'href': '#绑定目标容器'},
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
            component_name='FefferyExecuteJs'
        )
    ],
    style={
        'display': 'flex'
    }
)
