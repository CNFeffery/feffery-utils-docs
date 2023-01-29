from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_markdown_components as fmc

import callbacks.FefferyGrid
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
                            'title': 'FefferyGrid 可拖拽网格'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText(
                            '　　配合FefferyGridItem搭建可拖拽网格布局，以实现如可视化仪表盘等典型数据应用功能。'
                        )
                    ]
                ),

                html.Div(
                    [
                        fuc.FefferyGrid(
                            [
                                fuc.FefferyGridItem(
                                    str(i),
                                    key=str(i),
                                    style={
                                        'height': '100%',
                                        'display': 'flex',
                                        'justifyContent': 'center',
                                        'alignItems': 'center'
                                    }
                                )
                                for i in range(10)
                            ],
                            layouts=[
                                dict(
                                    i=str(i),
                                    x=i,
                                    y=i+1,
                                    w=1,
                                    h=i+i % 2+1
                                )
                                for i in range(5)
                            ],
                            cols=5,
                            rowHeight=75,
                            placeholderBorderRadius='5px',
                            margin=[25, 25],
                            style={
                                'border': '1px dashed #e1dfdd'
                            }
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
fuc.FefferyGrid(
    [
        fuc.FefferyGridItem(
            str(i),
            key=str(i),
            style={
                'height': '100%',
                'display': 'flex',
                'justifyContent': 'center',
                'alignItems': 'center'
            }
        )
        for i in range(10)
    ],
    layouts=[
        dict(
            i=str(i),
            x=i,
            y=i+1,
            w=1,
            h=i+i % 2+1
        )
        for i in range(5)
    ],
    cols=5,
    rowHeight=75,
    placeholderBorderRadius='5px',
    margin=[25, 25],
    style={
        'border': '1px dashed #e1dfdd'
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
            component_name='FefferyGrid'
        )
    ],
    style={
        'display': 'flex'
    }
)
