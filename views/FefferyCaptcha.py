from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc

import callbacks.FefferyCaptcha
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
                            'title': 'FefferyCaptcha 验证码'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　用于快捷构建图片验证码。')
                    ]
                ),

                html.Div(
                    [
                        fac.AntdSpace(
                            [
                                fuc.FefferyCaptcha(),
                                fuc.FefferyCaptcha(
                                    charNum=6
                                ),
                                fuc.FefferyCaptcha(
                                    width=150
                                ),
                                fuc.FefferyCaptcha(
                                    height=80
                                )
                            ],
                            direction='vertical'
                        ),

                        fac.AntdDivider(
                            '基础使用',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                fac.AntdText(
                                    '　　验证码组件的常规用法，点击可自动更换验证码'
                                )
                            ]
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdSpace(
    [
        fuc.FefferyCaptcha(),
        fuc.FefferyCaptcha(
            charNum=6
        ),
        fuc.FefferyCaptcha(
            width=150
        ),
        fuc.FefferyCaptcha(
            height=80
        )
    ],
    direction='vertical'
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
                        fuc.FefferyCaptcha(
                            id='captcha-demo1'
                        ),

                        fac.AntdText(
                            id='output-demo1'
                        ),

                        fac.AntdDivider(
                            '回调获取当前验证码',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString='''
fuc.FefferyCaptcha(
    id='captcha-demo1'
),

fac.AntdText(
    id='output-demo1'
)

...

@app.callback(
    Output('output-demo1', 'children'),
    Input('captcha-demo1', 'captcha')
)
def captcha_demo1(captcha):

    return f'当前验证码：{captcha}'
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
                    id='回调获取当前验证码',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdSpace(
                            [
                                fac.AntdButton(
                                    '刷新',
                                    id='refresh-captcha',
                                    type='primary'
                                ),

                                fuc.FefferyCaptcha(
                                    id='captcha-demo2'
                                )
                            ],
                            direction='vertical'
                        ),

                        fac.AntdDivider(
                            '手动控制验证码刷新',
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
        fac.AntdButton(
            '刷新',
            id='refresh-captcha',
            type='primary'
        ),

        fuc.FefferyCaptcha(
            id='captcha-demo2'
        )
    ],
    direction='vertical'
)

...

@app.callback(
    Output('captcha-demo2', 'refresh'),
    Input('refresh-captcha', 'nClicks'),
    prevent_initial_call=True
)
def captcha_demo2(nClicks):

    return True
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
                    id='手动控制验证码刷新',
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
                    {'title': '回调获取当前验证码', 'href': '#回调获取当前验证码'},
                    {'title': '手动控制验证码刷新', 'href': '#手动控制验证码刷新'},
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
            component_name='FefferyCaptcha'
        )
    ],
    style={
        'display': 'flex'
    }
)
