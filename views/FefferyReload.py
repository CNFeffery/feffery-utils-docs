from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_markdown_components as fmc

import callbacks.FefferyReload
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
                            'title': 'FefferyReload 页面重载'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　用于快捷实现页面的重载或延时重载。')
                    ]
                ),

                html.Div(
                    [
                        fac.AntdSpace(
                            [
                                fac.AntdButton(
                                    '立即重载',
                                    id='trigger-reload-demo',
                                    type='primary'
                                ),
                                fac.AntdButton(
                                    '2秒后重载',
                                    id='trigger-reload-delay-demo',
                                    type='primary'
                                )
                            ],
                            addSplitLine=True
                        ),

                        fuc.FefferyReload(
                            id='trigger-reload-demo-output'
                        ),

                        fuc.FefferyReload(
                            id='trigger-reload-delay-demo-output',
                            delay=2000
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
                                codeString='''
fac.AntdSpace(
    [
        fac.AntdButton(
            '立即重载',
            id='trigger-reload-demo',
            type='primary'
        ),
        fac.AntdButton(
            '2秒后重载',
            id='trigger-reload-delay-demo',
            type='primary'
        )
    ],
    addSplitLine=True
),

fuc.FefferyReload(
    id='trigger-reload-demo-output'
),

fuc.FefferyReload(
    id='trigger-reload-delay-demo-output',
    delay=2000
)

...

@app.callback(
    Output('trigger-reload-demo-output', 'reload'),
    Input('trigger-reload-demo', 'nClicks'),
    prevent_initial_call=True
)
def reload_demo(nClicks):

    return True


@app.callback(
    Output('trigger-reload-delay-demo-output', 'reload'),
    Input('trigger-reload-delay-demo', 'nClicks'),
    prevent_initial_call=True
)
def reload_delay_demo(nClicks):

    return True

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
            component_name='FefferyReload'
        )
    ],
    style={
        'display': 'flex'
    }
)
