from dash import html, dcc
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_markdown_components as fmc

import callbacks.FefferyCookie
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
                            'title': 'FefferyCookie cookie控制'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        '用于对指定的cookie进行控制'
                    ],
                    style={
                        'textIndent': '2rem'
                    }
                ),

                html.Div(
                    [
                        fuc.FefferyCookie(
                            id='cookie-basic-demo',
                            cookieKey='feffery-cookie-basic-demo',
                            defaultValue='I~love~dash!'
                        ),

                        fac.AntdParagraph(
                            '请在浏览器开发者工具-应用中查看当前应用的cookies信息',
                            type='secondary',
                            style={
                                'textIndent': '2rem'
                            }
                        ),

                        fac.AntdDivider(
                            '基础使用',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                '若当前指定的cookie键值对在浏览器中原先不存在，则可以通过设置',
                                fac.AntdText(
                                    'defaultValue',
                                    code=True
                                ),
                                '参数实现对应cookie值的初始化'
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
fuc.FefferyCookie(
    id='cookie-basic-demo',
    cookieKey='feffery-cookie-basic-demo',
    defaultValue='I~love~dash!'
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
                        fuc.FefferyCookie(
                            id='cookie-init-get-value-demo',
                            cookieKey='feffery-cookie-basic-demo'
                        ),

                        fac.AntdText(
                            id='cookie-init-get-value-demo-output'
                        ),

                        fac.AntdDivider(
                            '初始化获取cookie值',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                '当指定了参数',
                                fac.AntdText(
                                    'cookieKey',
                                    code=True
                                ),
                                '且未设置参数',
                                fac.AntdText(
                                    'value',
                                    code=True
                                ),
                                '时，可以在当前组件初始化时捕获到对应cookie当下的有效值'
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
fuc.FefferyCookie(
    id='cookie-init-get-value-demo',
    cookieKey='feffery-cookie-basic-demo'
),

fac.AntdText(
    id='cookie-init-get-value-demo-output'
)

...

@app.callback(
    Output('cookie-init-get-value-demo-output', 'children'),
    Input('cookie-init-get-value-demo', 'value')
)
def cookie_init_get_value(value):

    return f'feffery-cookie-basic-demo: {value}'
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
                    id='初始化获取cookie值',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fuc.FefferyCookie(
                            id='cookie-dynamic-update-value-demo',
                            cookieKey='feffery-cookie-dynamic-update-demo',
                            defaultValue='1'
                        ),

                        fac.AntdCompact(
                            [
                                fac.AntdButton(
                                    'cookie值自增1',
                                    id='cookie-dynamic-update-value-demo-add-one'
                                ),
                                fac.AntdButton(
                                    '获取最新cookie值',
                                    id='cookie-dynamic-update-value-demo-update-output'
                                )
                            ]
                        ),

                        fac.AntdParagraph(
                            id='cookie-dynamic-update-value-demo-output'
                        ),

                        fac.AntdDivider(
                            '动态更新cookie值',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                '这里以配合',
                                fac.AntdText(
                                    'flask',
                                    strong=True
                                ),
                                '在回调函数中捕获cookies为例进行相关功能演示'
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
fuc.FefferyCookie(
    id='cookie-dynamic-update-value-demo',
    cookieKey='feffery-cookie-dynamic-update-demo',
    defaultValue='1'
),

fac.AntdCompact(
    [
        fac.AntdButton(
            'cookie值自增1',
            id='cookie-dynamic-update-value-demo-add-one'
        ),
        fac.AntdButton(
            '获取最新cookie值',
            id='cookie-dynamic-update-value-demo-update-output'
        )
    ]
),

fac.AntdParagraph(
    id='cookie-dynamic-update-value-demo-output'
)

...

from flask import request

...

@app.callback(
    Output('cookie-dynamic-update-value-demo', 'value'),
    Input('cookie-dynamic-update-value-demo-add-one', 'nClicks'),
    State('cookie-dynamic-update-value-demo', 'value'),
    prevent_initial_call=True
)
def cookie_dynamic_update_value_demo_add_one(nClicks, value):

    return str(int(value) + 1)


@app.callback(
    Output('cookie-dynamic-update-value-demo-output', 'children'),
    Input('cookie-dynamic-update-value-demo-update-output', 'nClicks')
)
def cookie_dynamic_update_value_demo_output(nClicks):

    return 'feffery-cookie-dynamic-update-demo: {}'.format(
        request.cookies.get('feffery-cookie-dynamic-update-demo')
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
                    id='动态更新cookie值',
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
                    {'title': '初始化获取cookie值', 'href': '#初始化获取cookie值'},
                    {'title': '动态更新cookie值', 'href': '#动态更新cookie值'},
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
            component_name='FefferyCookie'
        )
    ],
    style={
        'display': 'flex'
    }
)
