import uuid
from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_markdown_components as fmc

import callbacks.FefferyLazyLoad
from views.side_props import render_side_props_layout


def docs_content():

    return html.Div(
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
                                'title': 'FefferyLazyLoad 懒加载容器'
                            }
                        ]
                    ),

                    fac.AntdDivider(isDashed=True),

                    fac.AntdParagraph(
                        [
                            fac.AntdText('　　用于实现内部元素的懒加载及相关检测。')
                        ]
                    ),

                    html.Div(
                        [
                            html.Div(
                                [
                                    fac.AntdText('请向下滚动'),
                                    html.Div(
                                        style={
                                            'height': '800px'
                                        }
                                    ),
                                    fuc.FefferyLazyLoad(
                                        html.Div(
                                            html.Img(
                                                src='https://fac.feffery.tech/assets/imgs/fac-logo.svg?token=' +
                                                str(uuid.uuid4()),
                                                style={
                                                    'height': '100%'
                                                }
                                            ),
                                            style={
                                                'height': '100px',
                                                'border': '1px dashed #c8c6c4'
                                            }
                                        ),
                                        height=100
                                    )
                                ],
                                style={
                                    'maxHeight': '300px',
                                    'overflow': 'auto'
                                }
                            ),

                            fac.AntdDivider(
                                '基础使用',
                                lineColor='#f0f0f0',
                                innerTextOrientation='left'
                            ),

                            fac.AntdParagraph(
                                [
                                    fac.AntdText(
                                        '　　最基础的用法，包裹在内的子元素在达到出现判定条件之前不会加载到页面DOM中。'
                                    )
                                ]
                            ),

                            fac.AntdCollapse(
                                fmc.FefferySyntaxHighlighter(
                                    showLineNumbers=True,
                                    language='python',
                                    codeTheme='coy-without-shadows',
                                    codeString='''
html.Div(
    [
        fac.AntdText('请向下滚动'),
        html.Div(
            style={
                'height': '800px'
            }
        ),
        fuc.FefferyLazyLoad(
            html.Div(
                html.Img(
                    src='https://fac.feffery.tech/assets/imgs/fac-logo.svg?token=' +
                    str(uuid.uuid4()),
                    style={
                        'height': '100%'
                    }
                ),
                style={
                    'height': '100px',
                    'border': '1px dashed #c8c6c4'
                }
            ),
            height=100
        )
    ],
    style={
        'maxHeight': '300px',
        'overflow': 'auto'
    }
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
                            html.Div(
                                [
                                    fac.AntdText('请向下滚动'),
                                    html.Div(
                                        style={
                                            'height': '800px'
                                        }
                                    ),
                                    fuc.FefferyLazyLoad(
                                        fac.AntdSkeleton(
                                            html.Div(
                                                id='lazy-load-demo-output',
                                                style={
                                                    'height': '100px',
                                                    'border': '1px dashed #c8c6c4'
                                                }
                                            ),
                                            active=True
                                        ),
                                        id='lazy-load-demo',
                                        height=100,
                                        throttle=0
                                    )
                                ],
                                style={
                                    'maxHeight': '300px',
                                    'overflow': 'auto'
                                }
                            ),

                            fac.AntdDivider(
                                '回调示例',
                                lineColor='#f0f0f0',
                                innerTextOrientation='left'
                            ),

                            fac.AntdParagraph(
                                [
                                    fac.AntdText(
                                        '　　也可通过监听懒加载容器出现与否进行可控的内容加载'
                                    )
                                ]
                            ),

                            fac.AntdCollapse(
                                fmc.FefferySyntaxHighlighter(
                                    showLineNumbers=True,
                                    language='python',
                                    codeTheme='coy-without-shadows',
                                    codeString='''
html.Div(
    [
        fac.AntdText('请向下滚动'),
        html.Div(
            style={
                'height': '800px'
            }
        ),
        fuc.FefferyLazyLoad(
            fac.AntdSkeleton(
                html.Div(
                    id='lazy-load-demo-output',
                    style={
                        'height': '100px',
                        'border': '1px dashed #c8c6c4'
                    }
                ),
                active=True
            ),
            id='lazy-load-demo',
            height=100,
            throttle=0
        )
    ],
    style={
        'maxHeight': '300px',
        'overflow': 'auto'
    }
)

...

@app.callback(
    Output('lazy-load-demo-output', 'children'),
    Input('lazy-load-demo', 'visible'),
    prevent_initial_call=True
)
def lazy_load_demo(visible):

    if visible:
        time.sleep(2)
        return '当前内容渲染时间：{}'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
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
                        id='回调示例',
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
                        {'title': '回调示例', 'href': '#回调示例'}
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
                component_name='FefferyLazyLoad'
            )
        ],
        style={
            'display': 'flex'
        }
    )
