from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc

import callbacks.FefferyScroll
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
                            'title': 'FefferyScroll 滚动动作'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　用于快捷执行常用的几种滚动动作。')
                    ]
                ),

                html.Div(
                    [
                        fac.AntdSpace(
                            [
                                fac.AntdButton(
                                    '滚动至页面底部',
                                    id='scroll-to-bottom-demo',
                                    type='primary'
                                ),
                                fac.AntdButton(
                                    '滚动至距离顶部800px处',
                                    id='scroll-top-offset-demo',
                                    type='primary'
                                ),
                                fac.AntdButton(
                                    '相对当前位置向下滚动300px',
                                    id='scroll-relative-offset-demo',
                                    type='primary'
                                ),
                                fac.AntdButton(
                                    '滚动至示例元素处',
                                    id='scroll-target-demo',
                                    type='primary'
                                )
                            ],
                            wrap=True,
                            size='small'
                        ),

                        html.Div(
                            [
                                fac.AntdParagraph(
                                    '示例目标元素',
                                    id='scroll-target-element'
                                ),
                                fac.AntdButton(
                                    '滚动至页面顶部',
                                    id='scroll-to-top-demo',
                                    type='primary'
                                ),
                            ],
                            style={
                                'padding': '1400px 0 800px 0',
                                'background': 'linear-gradient(180deg,#1890ff80,#fff)'
                            }
                        ),

                        html.Div(
                            id='scroll-demo-output'
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
fac.AntdSpace(
    [
        fac.AntdButton(
            '滚动至页面底部',
            id='scroll-to-bottom-demo',
            type='primary'
        ),
        fac.AntdButton(
            '滚动至距离顶部800px处',
            id='scroll-top-offset-demo',
            type='primary'
        ),
        fac.AntdButton(
            '相对当前位置向下滚动300px',
            id='scroll-relative-offset-demo',
            type='primary'
        ),
        fac.AntdButton(
            '滚动至示例元素处',
            id='scroll-target-demo',
            type='primary'
        )
    ],
    wrap=True,
    size='small'
),

html.Div(
    [
        fac.AntdParagraph(
            '示例目标元素',
            id='scroll-target-element'
        ),
        fac.AntdButton(
            '滚动至页面顶部',
            id='scroll-to-top-demo',
            type='primary'
        ),
    ],
    style={
        'padding': '1400px 0 800px 0',
        'background': 'linear-gradient(180deg,#1890ff80,#fff)'
    }
),

html.Div(
    id='scroll-demo-output'
)

...

@app.callback(
    Output('scroll-demo-output', 'children'),
    [Input('scroll-to-top-demo', 'nClicks'),
     Input('scroll-to-bottom-demo', 'nClicks'),
     Input('scroll-top-offset-demo', 'nClicks'),
     Input('scroll-relative-offset-demo', 'nClicks'),
     Input('scroll-target-demo', 'nClicks')],
    prevent_initial_call=True
)
def scroll_demo(*args):

    # 基于dash的上下文功能获知当前回调由谁触发
    trigger_id = dash.ctx.triggered_id

    if trigger_id == 'scroll-to-top-demo':
        return fuc.FefferyScroll(
            executeScroll=True,
            scrollMode='to-top'
        )

    elif trigger_id == 'scroll-to-bottom-demo':
        return fuc.FefferyScroll(
            executeScroll=True,
            scrollMode='to-bottom'
        )

    elif trigger_id == 'scroll-top-offset-demo':
        return fuc.FefferyScroll(
            executeScroll=True,
            scrollMode='top-offset',
            scrollTopOffset=800
        )

    elif trigger_id == 'scroll-relative-offset-demo':
        return fuc.FefferyScroll(
            executeScroll=True,
            scrollMode='relative-offset',
            scrollRelativeOffset=300
        )

    elif trigger_id == 'scroll-target-demo':
        return fuc.FefferyScroll(
            executeScroll=True,
            scrollMode='target',
            scrollTargetId='scroll-target-element'
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
            component_name='FefferyScroll'
        )
    ],
    style={
        'display': 'flex'
    }
)
