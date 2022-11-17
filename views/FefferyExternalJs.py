from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc

import callbacks.FefferyExternalJs
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
                            'title': 'FefferyExternalJs 外部js资源注入'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　用于将指定链接对应的js脚本加载到应用中。')
                    ]
                ),

                html.Div(
                    [
                        fac.AntdSpace(
                            [
                                fac.AntdButton(
                                    '挂载party.js',
                                    id='mount-js'
                                ),
                                fac.AntdButton(
                                    '点我试试',
                                    id='effect-when-mount',
                                    type='primary'
                                )
                            ]
                        ),

                        fuc.FefferyExternalJs(
                            id='external-js-demo'
                        ),

                        fuc.FefferyExecuteJs(
                            id='execute-party-effect'
                        ),

                        fac.AntdDivider(
                            '基础使用',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                fac.AntdText(
                                    '　　以基于party.js的庆祝特效渲染为例，通过观察浏览器开发者工具-网络可以更清楚地了解到上述回调工作原理'
                                )
                            ]
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString="""
fac.AntdSpace(
    [
        fac.AntdButton(
            '挂载party.js',
            id='mount-js'
        ),
        fac.AntdButton(
            '点我试试',
            id='effect-when-mount',
            type='primary'
        )
    ]
),

fuc.FefferyExternalJs(
    id='external-js-demo'
),

fuc.FefferyExecuteJs(
    id='execute-party-effect'
)

...

@app.callback(
    [Output('external-js-demo', 'jsUrl'),
     Output('execute-party-effect', 'jsString')],
    Input('mount-js', 'nClicks'),
    prevent_initial_call=True
)
def external_js_demo(nClicks):

    if nClicks and nClicks == 1:
        return [
            'https://fastly.jsdelivr.net/npm/party-js@latest/bundle/party.min.js',
            '''
document.querySelector("#effect-when-mount").addEventListener("click", function (e) {
    party.confetti(this);
});
'''
        ]

    return dash.no_update
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
            component_name='FefferyExternalJs'
        )
    ],
    style={
        'display': 'flex'
    }
)
