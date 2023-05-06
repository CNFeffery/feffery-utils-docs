import dash
from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_markdown_components as fmc

import callbacks.FefferyListenUnload
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
                            'title': 'FefferyListenUnload 页面关闭监听'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　用于监听当前应用所在的浏览器标签页是否被用户关闭或刷新。')
                    ]
                ),

                html.Div(
                    [
                        fuc.FefferyListenUnload(
                            id='listen-unload-demo'
                        ),

                        # 使用FefferyListenUnload时，任意选择Output即可
                        html.Div(
                            id='listen-unload-demo-output'
                        ),

                        fac.AntdImage(
                            src=dash.get_asset_url('imgs/FefferyListenUnload演示.gif')
                        ),

                        fac.AntdDivider(
                            '基础使用',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                fac.AntdText(
                                    'FefferyListenUnload',
                                    strong=True
                                ),
                                '在回调中的使用比较特殊，由于它是用来监听当前浏览器标签页的关闭或重载事件，',
                                '而此类事件的发生则意味着当前标签页内运行的应用被清除销毁或重载，因此',
                                fac.AntdText(
                                    'FefferyListenUnload',
                                    strong=True
                                ),
                                '可用于为当前应用“清理战场”，典型场景如：'
                            ],
                            style={
                                'textIndent': '2rem'
                            }
                        ),

                        fac.AntdParagraph(
                            [
                                '针对需要用户上传文件进行运算的工具类应用，基于',
                                fac.AntdText(
                                    'FefferyListenUnload',
                                    strong=True
                                ),
                                '可以实现应用关闭或重载后，删除清理服务器上已落盘文件的功能。'
                            ],
                            type='secondary',
                            italic=True,
                            style={
                                'borderLeft': '3px solid #e9ecef',
                                'paddingLeft': 8
                            }
                        ),

                        fac.AntdCollapse(
                            fmc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString='''
fuc.FefferyListenUnload(
    id='listen-unload-demo'
),

# 使用FefferyListenUnload时，任意选择Output即可
html.Div(
    id='listen-unload-demo-output'
)

...

@app.callback(
    Output('listen-unload-demo-output', 'children'),
    Input('listen-unload-demo', 'unloaded'),
    prevent_initial_call=True
)
def listen_unload_demo(unloaded):

    print(f'unloaded: {unloaded}')
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
            component_name='FefferyListenUnload'
        )
    ],
    style={
        'display': 'flex'
    }
)
