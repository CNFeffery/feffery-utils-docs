from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc

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
                            'title': 'FefferyRawHTML html源码渲染'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　用于直接渲染html源码字符串为页面元素。')
                    ]
                ),

                html.Div(
                    [
                        fuc.FefferyRawHTML(
                            htmlString='''
</ style>
<div style="width: 300px;height: 150px;box-shadow: 0px 0px 12px rgba(0, 0, 0, .12); display: flex;justify-content: center;align-items: center;">
    示例
</ div>
'''
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
                                codeString="""
fuc.FefferyRawHTML(
    htmlString='''
</ style>
<div style="width: 300px;height: 150px;box-shadow: 0px 0px 12px rgba(0, 0, 0, .12); display: flex;justify-content: center;align-items: center;">
    示例
</ div>
'''
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
            component_name='FefferyRawHTML'
        )
    ],
    style={
        'display': 'flex'
    }
)
