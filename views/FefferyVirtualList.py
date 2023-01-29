import uuid
from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_markdown_components as fmc

import callbacks.FefferyVirtualList
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
                                'title': 'FefferyVirtualList 虚拟滚动列表'
                            }
                        ]
                    ),

                    fac.AntdDivider(isDashed=True),

                    fac.AntdParagraph(
                        [
                            fac.AntdText(
                                '　　用于在设定的区域高度范围内高性能地展示大量（建议不要高于10000个，否则可能会引发一些问题）重复格式的子元素，原理是仅渲染划入范围的元素。'
                            )
                        ]
                    ),

                    html.Div(
                        [
                            fuc.FefferyVirtualList(
                                id='virtual-list-demo',
                                height=400,
                                itemHeight=40
                            ),

                            fac.AntdDivider(
                                '基础使用',
                                lineColor='#f0f0f0',
                                innerTextOrientation='left'
                            ),

                            fac.AntdParagraph(
                                [
                                    fac.AntdText(
                                        '　　为节省服务器带宽，这里使用浏览器端回调进行1000个子元素的装填。'
                                    )
                                ]
                            ),

                            fac.AntdCollapse(
                                fmc.FefferySyntaxHighlighter(
                                    showLineNumbers=True,
                                    language='python',
                                    codeTheme='coy-without-shadows',
                                    codeString="""
fuc.FefferyVirtualList(
    id='virtual-list-demo',
    height=400,
    itemHeight=40
)

...

app.clientside_callback(
    '''(pathname) => {
        let childrenList = [];
        for (let i = 0;i<1000;i++) {
            childrenList.push(
                {
                    'props': {
                        'message': `演示列表子元素${i}`,
                        'showIcon': true,
                        'type': 'info'
                    },
                    'type': 'AntdAlert',
                    'namespace': 'feffery_antd_components'
                }
            );
        }

        return childrenList;
    }''',
    Output('virtual-list-demo', 'children'),
    Input('url', 'pathname')
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
                component_name='FefferyVirtualList'
            )
        ],
        style={
            'display': 'flex'
        }
    )
