from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_markdown_components as fmc

import callbacks.FefferyKeyPress
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
                            'title': 'FefferyKeyPress 按键行为监听'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　用于监听指定的按键行为，常用的按键别名有：'),
                        *[
                            fac.AntdText(
                                [
                                    fac.AntdText(
                                        key_name,
                                        keyboard=True
                                    ),
                                    '、'
                                ]
                            )
                            for key_name in [
                                'backspace', 'tab', 'enter', 'shift', 'ctrl',
                                'alt', 'pausebreak', 'capslock', 'esc', 'space',
                                'pageup', 'pagedown', 'end', 'home', 'leftarrow',
                                'uparrow', 'rightarrow', 'downarrow', 'insert',
                                'delete', 'leftwindowkey', 'rightwindowkey'
                            ]
                        ]
                    ]
                ),

                html.Div(
                    [
                        fuc.FefferyKeyPress(
                            id='key-press-demo',
                            keys='ctrl.s'
                        ),

                        fac.AntdParagraph(
                            id='key-press-demo-output'
                        ),

                        fac.AntdDivider(
                            '基础使用',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                '　　以监听',
                                fac.AntdText(
                                    'ctrl+s',
                                    keyboard=True
                                ),
                                '按键行为为例'
                            ]
                        ),

                        fac.AntdCollapse(
                            fmc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString='''
fuc.FefferyKeyPress(
    id='key-press-demo',
    keys='ctrl.s'
),

fac.AntdParagraph(
    id='key-press-demo-output'
)

...

@app.callback(
    Output('key-press-demo-output', 'children'),
    Input('key-press-demo', 'pressedCounts')
)
def key_press_demo(pressedCounts):

    return f'pressedCounts: {pressedCounts}'
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
                    {'title': '基础使用', 'href': '#基础使用'}
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
            component_name='FefferyKeyPress'
        )
    ],
    style={
        'display': 'flex'
    }
)
