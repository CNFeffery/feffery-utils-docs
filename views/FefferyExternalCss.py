from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc

import callbacks.FefferyExternalCss
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
                            'title': 'FefferyExternalCss 外部css资源注入'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　用于将指定链接对应的css文件加载到应用中，或从应用中卸载。')
                    ]
                ),

                html.Div(
                    [

                        fac.AntdSpace(
                            [
                                fac.AntdButton(
                                    '挂载dark.css',
                                    id='mount-dark-css'
                                ),
                                fac.AntdButton(
                                    '卸载已有css',
                                    id='unmount-css'
                                )
                            ],
                            style={
                                'marginBottom': '15px'
                            }
                        ),

                        fuc.FefferyExternalCss(
                            id='external-css-demo'
                        ),

                        html.Div(
                            'FefferyExternalCss示例',
                            className='external-css-dark-demo'
                        ),

                        fac.AntdDivider(
                            '基础使用',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                fac.AntdText(
                                    '　　通过观察浏览器开发者工具-网络可以更清楚地了解到上述回调工作原理'
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
            '挂载dark.css',
            id='mount-dark-css'
        ),
        fac.AntdButton(
            '卸载已有css',
            id='unmount-css'
        )
    ],
    style={
        'marginBottom': '15px'
    }
),

fuc.FefferyExternalCss(
    id='external-css-demo'
),

html.Div(
    'FefferyExternalCss示例',
    className='external-css-dark-demo'
)

...

@app.callback(
    Output('external-css-demo', 'cssUrl'),
    [Input('mount-dark-css', 'nClicks'),
     Input('unmount-css', 'nClicks')],
    prevent_initial_call=True
)
def external_css_demo(*args):

    if dash.ctx.triggered_id == 'mount-dark-css':
        return '/assets/css/dark.css'

    else:
        return ''
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
            component_name='FefferyExternalCss'
        )
    ],
    style={
        'display': 'flex'
    }
)
