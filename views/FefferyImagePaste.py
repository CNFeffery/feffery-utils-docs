from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_markdown_components as fmc

import callbacks.FefferyImagePaste
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
                            'title': 'FefferyImagePaste 图片粘贴捕获'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　用于监听图片粘贴事件并获取对应图片的base64格式数据。')
                    ]
                ),

                html.Div(
                    [
                        fuc.FefferyDiv(
                            '鼠标移入此区域后进行图片粘贴',
                            id='image-paste-container',
                            shadow='hover-shadow',
                            style={
                                'height': '200px',
                                'display': 'flex',
                                'justifyContent': 'center',
                                'alignItems': 'center',
                                'borderRadius': '6px',
                                'border': '1px solid #f0f0f0',
                                'marginBottom': '10px'
                            }
                        ),

                        fuc.FefferyImagePaste(
                            id='image-paste-demo',
                            disabled=True
                        ),

                        fac.AntdImage(
                            id='image-paste-output',
                            preview=True
                        ),

                        fac.AntdDivider(
                            '基础使用',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                fac.AntdText('　　推荐的用法是配合'),
                                fac.AntdText('fuc.FefferyDiv', strong=True),
                                fac.AntdText(
                                    '的鼠标悬停监听功能，实现鼠标在指定容器内时才启用图片粘贴捕获功能'
                                )
                            ]
                        ),

                        fac.AntdCollapse(
                            fmc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString="""
fuc.FefferyDiv(
    '鼠标移入此区域后进行图片粘贴',
    id='image-paste-container',
    shadow='hover-shadow',
    style={
        'height': '200px',
        'display': 'flex',
        'justifyContent': 'center',
        'alignItems': 'center',
        'borderRadius': '6px',
        'border': '1px solid #f0f0f0',
        'marginBottom': '10px'
    }
),

fuc.FefferyImagePaste(
    id='image-paste-demo',
    disabled=True
),

fac.AntdImage(
    id='image-paste-output',
    preview=True
)

...

app.clientside_callback(
    '''(isHovering) => !isHovering;''',
    Output('image-paste-demo', 'disabled'),
    Input('image-paste-container', 'isHovering')
)


app.clientside_callback(
    '''(imageInfo) => imageInfo.base64;''',
    Output('image-paste-output', 'src'),
    Input('image-paste-demo', 'imageInfo'),
    prevent_initial_call=True
)
"""
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
            component_name='FefferyImagePaste'
        )
    ],
    style={
        'display': 'flex'
    }
)
