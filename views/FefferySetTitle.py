from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_markdown_components as fmc

import callbacks.FefferySetTitle
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
                            'title': 'FefferySetTitle 页面title更新'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　用于动态修改当前页面对应的浏览器标签title。')
                    ]
                ),

                html.Div(
                    [
                        fac.AntdInput(
                            id='set-title-demo',
                            placeholder='请输入新title信息',
                            style={
                                'maxWidth': '200px'
                            }
                        ),

                        fuc.FefferySetTitle(
                            id='set-title-demo-output'
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
fac.AntdInput(
    id='set-title-demo',
    placeholder='请输入新title信息',
    style={
        'maxWidth': '200px'
    }
),

fuc.FefferySetTitle(
    id='set-title-demo-output'
)

...

@app.callback(
    Output('set-title-demo-output', 'title'),
    Input('set-title-demo', 'value'),
    prevent_initial_call=True
)
def set_title_demo(value):

    return value or dash.no_update
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
            component_name='FefferySetTitle'
        )
    ],
    style={
        'display': 'flex'
    }
)
