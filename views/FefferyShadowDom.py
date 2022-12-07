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
                            'title': 'FefferyShadowDom Shadow DOM组件'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　用于构建具有样式隔离功能的节点。')
                    ]
                ),

                html.Div(
                    [
                        fac.AntdSpace(
                            [
                                fuc.FefferyShadowDom(
                                    [
                                        fuc.FefferyStyle(
                                            rawStyle='''
.style-demo {
    width: 300px;
    height: 150px;
    background: linear-gradient(135deg,#fce38a,#f38181);
    border-radius: 5px;
    display: flex;
    justify-content: center;
    align-items: center;
}
'''
                                        ),
                                        html.Div(
                                            '节点1',
                                            className='style-demo'
                                        )
                                    ]
                                ),

                                fuc.FefferyShadowDom(
                                    [
                                        fuc.FefferyStyle(
                                            rawStyle='''
.style-demo {
    width: 300px;
    height: 150px;
    background: linear-gradient(135deg,#17ead9,#6078ea);
    border-radius: 5px;
    display: flex;
    justify-content: center;
    align-items: center;
}
'''
                                        ),
                                        html.Div(
                                            '节点2',
                                            className='style-demo'
                                        )
                                    ]
                                )
                            ],
                            direction='vertical'
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
fac.AntdSpace(
    [
        fuc.FefferyShadowDom(
            [
                fuc.FefferyStyle(
                    rawStyle='''
.style-demo {
width: 300px;
height: 150px;
background: linear-gradient(135deg,#fce38a,#f38181);
border-radius: 5px;
display: flex;
justify-content: center;
align-items: center;
}
'''
                ),
                html.Div(
                    '节点1',
                    className='style-demo'
                )
            ]
        ),

        fuc.FefferyShadowDom(
            [
                fuc.FefferyStyle(
                    rawStyle='''
.style-demo {
width: 300px;
height: 150px;
background: linear-gradient(135deg,#17ead9,#6078ea);
border-radius: 5px;
display: flex;
justify-content: center;
align-items: center;
}
'''
                ),
                html.Div(
                    '节点2',
                    className='style-demo'
                )
            ]
        )
    ],
    direction='vertical'
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
            component_name='FefferyShadowDom'
        )
    ],
    style={
        'display': 'flex'
    }
)
