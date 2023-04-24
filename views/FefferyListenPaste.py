from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_markdown_components as fmc

import callbacks.FefferyListenPaste
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
                            'title': 'FefferyListenPaste 粘贴事件监听'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　用于监听全局或目标容器内发生的粘贴事件。')
                    ]
                ),

                html.Div(
                    [
                        fac.AntdParagraph(
                            '提示：请在当前页面任何地方粘贴文字内容查看示例效果',
                            type='secondary'
                        ),
                        fuc.FefferyListenPaste(
                            id='listen-paste-basic-demo',
                            enableListenPaste=True
                        ),
                        html.Pre(
                            id='listen-paste-basic-demo-output'
                        ),

                        fac.AntdDivider(
                            '基础使用',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                '在设置参数',
                                fac.AntdText(
                                    'enableListenPaste=True',
                                    code=True
                                ),
                                '后，用户在应用任何位置进行的文本粘贴行为都会被捕获到'
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
                                codeString="""
fac.AntdParagraph(
    '提示：请在当前页面任何地方粘贴文字内容查看示例效果',
    type='secondary'
),
fuc.FefferyListenPaste(
    id='listen-paste-basic-demo',
    enableListenPaste=True
),
html.Pre(
    id='listen-paste-basic-demo-output'
)

...

app.clientside_callback(
    '''( pasteCount, pasteText ) => JSON.stringify({ pasteCount, pasteText }, null, 4)''',
    Output('listen-paste-basic-demo-output', 'children'),
    Input('listen-paste-basic-demo', 'pasteCount'),
    State('listen-paste-basic-demo', 'pasteText'),
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
                        fac.AntdParagraph(
                            '提示：请将鼠标移入下方示例容器后进行文本粘贴',
                            type='secondary'
                        ),
                        fuc.FefferyListenPaste(
                            id='listen-paste-target-container-demo',
                            targetContainerId='listen-paste-target-container'
                        ),
                        fuc.FefferyDiv(
                            id='listen-paste-target-container',
                            shadow='always-shadow',
                            style={
                                'width': 300,
                                'height': 200,
                                'borderRadius': 6
                            }
                        ),
                        html.Pre(
                            id='listen-paste-target-container-demo-output'
                        ),

                        fac.AntdDivider(
                            '绑定指定容器',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                '通过设置参数',
                                fac.AntdText(
                                    'targetContainerId',
                                    code=True
                                ),
                                '可以限制仅监听目标容器内的粘贴事件'
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
                                codeString="""
fac.AntdParagraph(
    '提示：请将鼠标移入下方示例容器后进行文本粘贴',
    type='secondary'
),
fuc.FefferyListenPaste(
    id='listen-paste-target-container-demo',
    targetContainerId='listen-paste-target-container'
),
fuc.FefferyDiv(
    id='listen-paste-target-container',
    shadow='always-shadow',
    style={
        'width': 300,
        'height': 200,
        'borderRadius': 6
    }
),
html.Pre(
    id='listen-paste-target-container-demo-output'
)

...

app.clientside_callback(
    '''( pasteCount, pasteText ) => JSON.stringify({ pasteCount, pasteText }, null, 4)''',
    Output('listen-paste-target-container-demo-output', 'children'),
    Input('listen-paste-target-container-demo', 'pasteCount'),
    State('listen-paste-target-container-demo', 'pasteText'),
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
                    id='绑定指定容器',
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
                    {'title': '绑定指定容器', 'href': '#绑定指定容器'}
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
            component_name='FefferyListenPaste'
        )
    ],
    style={
        'display': 'flex'
    }
)
