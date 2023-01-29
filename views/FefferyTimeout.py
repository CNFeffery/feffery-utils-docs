from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_markdown_components as fmc

import callbacks.FefferyTimeout
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
                            'title': 'FefferyTimeout 定时器'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　用于设置指定时长的触发器。')
                    ]
                ),

                html.Div(
                    [
                        fac.AntdForm(
                            [
                                fac.AntdFormItem(
                                    fac.AntdSpace(
                                        [
                                            fac.AntdInputNumber(
                                                id='timeout-demo-delay',
                                                value=2000,
                                                style={
                                                    'maxWidth': '300px'
                                                }
                                            ),
                                            fac.AntdButton(
                                                '开始',
                                                id='timeout-demo-start',
                                                type='primary'
                                            )
                                        ]
                                    ),
                                    label='设置定时时长（毫秒）'
                                )
                            ]
                        ),
                        
                        fuc.FefferyTimeout(
                            id='timeout-demo'
                        ),

                        fuc.FefferyExecuteJs(
                            id='timeout-demo-output'
                        ),

                        fac.AntdDivider(
                            '基础使用',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                fac.AntdText(
                                    '　　每一次更新delay参数后，在定时结束时都可以利用timeoutCount的更新来触发其他逻辑。'
                                )
                            ]
                        ),

                        fac.AntdCollapse(
                            fmc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdForm(
    [
        fac.AntdFormItem(
            fac.AntdSpace(
                [
                    fac.AntdInputNumber(
                        id='timeout-demo-delay',
                        value=2000,
                        style={
                            'maxWidth': '300px'
                        }
                    ),
                    fac.AntdButton(
                        '开始',
                        id='timeout-demo-start',
                        type='primary'
                    )
                ]
            ),
            label='设置定时时长（毫秒）'
        )
    ]
),

fuc.FefferyTimeout(
    id='timeout-demo'
),

fuc.FefferyExecuteJs(
    id='timeout-demo-output'
)

...

@app.callback(
    Output('timeout-demo', 'delay'),
    Input('timeout-demo-start', 'nClicks'),
    State('timeout-demo-delay', 'value'),
    prevent_initial_call=True
)
def start_new_timeout(nClicks, value):

    if value > 0:
        return value


@app.callback(
    Output('timeout-demo-output', 'jsString'),
    Input('timeout-demo', 'timeoutCount'),
    prevent_initial_call=True
)
def after_timeout(timeoutCount):

    return 'alert(`timeoutCount=${%s}`)' % timeoutCount


@app.callback(
    Output('timeout-demo-start', 'loading'),
    Input('timeout-demo', 'delay')
)
def enable_start_new(delay):

    return bool(delay)
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
            component_name='FefferyTimeout'
        )
    ],
    style={
        'display': 'flex'
    }
)
