from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc

import callbacks.FefferyTopProgress
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
                            'title': 'FefferyTopProgress 顶端加载进度条'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText(
                            '　　监听以children中元素为Output角色的回调过程，从而渲染页面顶部进度条动画。')
                    ]
                ),

                html.Div(
                    [
                        fac.AntdButton(
                            '触发5秒耗时回调',
                            id='top-progress-trigger-demo1',
                            type='primary'
                        ),

                        fuc.FefferyTopProgress(
                            fac.AntdText(
                                id='top-progress-trigger-demo1-output'
                            )
                        ),

                        fac.AntdDivider(
                            '基础使用',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdButton(
    '触发5秒耗时回调',
    id='top-progress-trigger-demo1',
    type='primary'
),

fuc.FefferyTopProgress(
    fac.AntdText(
        id='top-progress-trigger-demo1-output'
    )
)

...

import time
from datetime import datetime

@app.callback(
    Output('top-progress-trigger-demo1-output', 'children'),
    Input('top-progress-trigger-demo1', 'nClicks'),
    prevent_initial_call=True
)
def top_progress_demo1(nClicks):

    time.sleep(5)

    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')
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
            component_name='FefferyTopProgress'
        )
    ],
    style={
        'display': 'flex'
    }
)
