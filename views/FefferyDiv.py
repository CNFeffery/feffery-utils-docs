from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc

import callbacks.FefferyDiv
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
                            'title': 'FefferyDiv 进阶div容器'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　拥有更多进阶功能的div容器组件。')
                    ]
                ),

                html.Div(
                    [

                        fuc.FefferyDiv(
                            id='div-demo1',
                            style={
                                'height': '200px',
                                'background': 'grey',
                                'borderRadius': '8px',
                                'color': 'white',
                                'padding': '20px'
                            }
                        ),

                        fac.AntdDivider(
                            '监听自身尺寸变化',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString='''
fuc.FefferyDiv(
    id='div-demo1',
    style={
        'height': '200px',
        'background': 'grey',
        'borderRadius': '8px',
        'color': 'white',
        'padding': '20px'
    }
)

...

@app.callback(
    Output('div-demo1', 'children'),
    [Input('div-demo1', '_width'),
     Input('div-demo1', '_height')],
    prevent_initial_call=True
)
def div_demo1(_width, _height):

    return f'_width: {_width}  _height: {_height}'

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
                    id='监听自身尺寸变化',
                    className='div-highlight'
                ),


                html.Div(
                    [

                        fuc.FefferyDiv(
                            id='div-demo2',
                            style={
                                'height': '200px',
                                'background': 'grey',
                                'borderRadius': '8px',
                                'color': 'white',
                                'padding': '20px'
                            }
                        ),

                        fac.AntdDivider(
                            '监听鼠标移入移出',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString='''
fuc.FefferyDiv(
    id='div-demo2',
    style={
        'height': '200px',
        'background': 'grey',
        'borderRadius': '8px',
        'color': 'white',
        'padding': '20px'
    }
)

...

@app.callback(
    Output('div-demo2', 'children'),
    [Input('div-demo2', 'mouseEnterCount'),
     Input('div-demo2', 'mouseLeaveCount')]
)
def div_demo2(mouseEnterCount, mouseLeaveCount):

    return f'mouseEnterCount: {mouseEnterCount} mouseLeaveCount: {mouseLeaveCount}'
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
                    id='监听鼠标移入移出',
                    className='div-highlight'
                ),

                html.Div(
                    [

                        fuc.FefferyDiv(
                            id='div-demo3',
                            style={
                                'height': '200px',
                                'background': 'grey',
                                'borderRadius': '8px',
                                'color': 'white',
                                'padding': '20px',
                                'userSelect': 'none'
                            }
                        ),

                        fac.AntdDivider(
                            '监听单击、双击事件',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString='''
fuc.FefferyDiv(
    id='div-demo3',
    style={
        'height': '200px',
        'background': 'grey',
        'borderRadius': '8px',
        'color': 'white',
        'padding': '20px',
        'userSelect': 'none'
    }
)

...

@app.callback(
    Output('div-demo3', 'children'),
    [Input('div-demo3', 'nClicks'),
     Input('div-demo3', 'nDoubleClicks')]
)
def div_demo3(nClicks, nDoubleClicks):

    return f'nClicks: {nClicks} nDoubleClicks: {nDoubleClicks}'
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
                    id='监听单击、双击事件',
                    className='div-highlight'
                ),

                html.Div(
                    [

                        fuc.FefferyDiv(
                            id='div-demo4',
                            enableListenContextMenu=True,
                            style={
                                'height': '300px',
                                'background': 'grey',
                                'borderRadius': '8px',
                                'color': 'white',
                                'padding': '20px',
                                'userSelect': 'none'
                            }
                        ),

                        fac.AntdDivider(
                            '监听右键事件',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString='''
fuc.FefferyDiv(
    id='div-demo4',
    enableListenContextMenu=True,
    style={
        'height': '300px',
        'background': 'grey',
        'borderRadius': '8px',
        'color': 'white',
        'padding': '20px',
        'userSelect': 'none'
    }
)

...

@app.callback(
    Output('div-demo4', 'children'),
    Input('div-demo4', 'contextMenuEvent'),
    prevent_initial_call=True
)
def div_demo4(contextMenuEvent):

    return html.Pre(
        json.dumps(
            contextMenuEvent,
            ensure_ascii=False,
            indent=4
        )
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
                    id='监听右键事件',
                    className='div-highlight'
                ),

                html.Div(
                    [

                        fuc.FefferyDiv(
                            id='div-demo5',
                            style={
                                'height': '200px',
                                'background': 'grey',
                                'borderRadius': '8px',
                                'color': 'white',
                                'padding': '20px',
                                'userSelect': 'none'
                            }
                        ),

                        fac.AntdDivider(
                            '监听鼠标悬停状态',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString='''
fuc.FefferyDiv(
    id='div-demo5',
    style={
        'height': '200px',
        'background': 'grey',
        'borderRadius': '8px',
        'color': 'white',
        'padding': '20px',
        'userSelect': 'none'
    }
)

...

@app.callback(
    Output('div-demo5', 'children'),
    Input('div-demo5', 'isHovering')
)
def div_demo5(isHovering):

    return f'isHovering: {isHovering}'
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
                    id='监听鼠标悬停状态',
                    className='div-highlight'
                ),

                html.Div(
                    [

                        fuc.FefferyDiv(
                            id='div-demo6',
                            enableClickAway=True,
                            style={
                                'height': '200px',
                                'background': 'grey',
                                'borderRadius': '8px',
                                'color': 'white',
                                'padding': '20px',
                                'userSelect': 'none'
                            }
                        ),

                        fac.AntdDivider(
                            '监听容器外点击事件',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString='''
fuc.FefferyDiv(
    id='div-demo6',
    enableClickAway=True,
    style={
        'height': '200px',
        'background': 'grey',
        'borderRadius': '8px',
        'color': 'white',
        'padding': '20px',
        'userSelect': 'none'
    }
)

...

@app.callback(
    Output('div-demo6', 'children'),
    Input('div-demo6', 'clickAwayCount')
)
def div_demo6(clickAwayCount):

    return f'clickAwayCount: {clickAwayCount}'
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
                    id='监听容器外点击事件',
                    className='div-highlight'
                ),

                html.Div(
                    [

                        fac.AntdSpace(
                            [

                                fuc.FefferyDiv(
                                    '默认',
                                    style={
                                        'width': '200px',
                                        'height': '100px',
                                        'borderRadius': '6px',
                                        'border': '1px solid #f1f2f6',
                                        'display': 'flex',
                                        'justifyContent': 'center',
                                        'alignItems': 'center'
                                    }
                                ),

                                fuc.FefferyDiv(
                                    'shadow="hover-shadow"',
                                    shadow='hover-shadow',
                                    style={
                                        'width': '200px',
                                        'height': '100px',
                                        'borderRadius': '6px',
                                        'border': '1px solid #f1f2f6',
                                        'display': 'flex',
                                        'justifyContent': 'center',
                                        'alignItems': 'center'
                                    }
                                ),

                                fuc.FefferyDiv(
                                    'shadow="always-shadow"',
                                    shadow='always-shadow',
                                    style={
                                        'width': '200px',
                                        'height': '100px',
                                        'borderRadius': '6px',
                                        'border': '1px solid #f1f2f6',
                                        'display': 'flex',
                                        'justifyContent': 'center',
                                        'alignItems': 'center'
                                    }
                                )
                            ]
                        ),

                        fac.AntdDivider(
                            '不同的内置阴影效果',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdSpace(
    [

        fuc.FefferyDiv(
            '默认',
            style={
                'width': '200px',
                'height': '100px',
                'borderRadius': '6px',
                'border': '1px solid #f1f2f6',
                'display': 'flex',
                'justifyContent': 'center',
                'alignItems': 'center'
            }
        ),

        fuc.FefferyDiv(
            'shadow="hover-shadow"',
            shadow='hover-shadow',
            style={
                'width': '200px',
                'height': '100px',
                'borderRadius': '6px',
                'border': '1px solid #f1f2f6',
                'display': 'flex',
                'justifyContent': 'center',
                'alignItems': 'center'
            }
        ),

        fuc.FefferyDiv(
            'shadow="always-shadow"',
            shadow='always-shadow',
            style={
                'width': '200px',
                'height': '100px',
                'borderRadius': '6px',
                'border': '1px solid #f1f2f6',
                'display': 'flex',
                'justifyContent': 'center',
                'alignItems': 'center'
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
                    id='不同的内置阴影效果',
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
                    {'title': '监听自身尺寸变化', 'href': '#监听自身尺寸变化'},
                    {'title': '监听鼠标移入移出', 'href': '#监听鼠标移入移出'},
                    {'title': '监听单击、双击事件', 'href': '#监听单击、双击事件'},
                    {'title': '监听右键事件', 'href': '#监听右键事件'},
                    {'title': '监听鼠标悬停状态', 'href': '#监听鼠标悬停状态'},
                    {'title': '监听容器外点击事件', 'href': '#监听容器外点击事件'},
                    {'title': '不同的内置阴影效果', 'href': '#不同的内置阴影效果'}
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
            component_name='FefferyDiv'
        )
    ],
    style={
        'display': 'flex'
    }
)
