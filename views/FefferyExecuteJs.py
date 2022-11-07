from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc

import callbacks.FefferyExecuteJs
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
                            'title': 'FefferyExecuteJs js执行'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　用于直接执行指定的javascript代码。')
                    ]
                ),

                html.Div(
                    [
                        fac.AntdSpace(
                            [
                                fac.AntdButton(
                                    '执行示例',
                                    id='execute-js-demo',
                                    type='primary'
                                ),

                                fuc.FefferyExecuteJs(
                                    id='execute-js-demo-output'
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
                                    '　　通过回调函数将你需要在浏览器中直接执行的javascript代码输出给参数jsString即可。'
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
        fac.AntdButton(
            '执行示例',
            id='execute-js-demo',
            type='primary'
        ),

        fuc.FefferyExecuteJs(
            id='execute-js-demo-output'
        )
    ],
    direction='vertical'
)

...

@app.callback(
    Output('execute-js-demo-output', 'jsString'),
    Input('execute-js-demo', 'nClicks'),
    prevent_initial_call=True
)
def execute_js_demo(nClicks):

    return 'alert("FefferyExecuteJs示例");'
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
            component_name='FefferyExecuteJs'
        )
    ],
    style={
        'display': 'flex'
    }
)
