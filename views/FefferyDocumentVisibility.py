from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_markdown_components as fmc

import callbacks.FefferyDocumentVisibility
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
                            'title': 'FefferyDocumentVisibility 页面可见性监听'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　用于监听当前页面是否可见。')
                    ]
                ),

                html.Div(
                    [

                        fuc.FefferyDocumentVisibility(
                            id='document-visibility-demo'
                        ),

                        fac.AntdSpin(
                            fac.AntdText(
                                'documentVisibility: visible',
                                id='document-visibility-demo-output'
                            ),
                            text='状态延时2s切换中',
                            size='small'
                        ),

                        fac.AntdDivider(
                            '基础使用',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                fac.AntdText(
                                    '　　最小化浏览器或切换到其他浏览器标签页，再切换回来以查看监听结果变化情况。'
                                )
                            ]
                        ),

                        fac.AntdCollapse(
                            fmc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString='''
fuc.FefferyDocumentVisibility(
    id='document-visibility-demo'
),

fac.AntdSpin(
    fac.AntdText(
        'documentVisibility: visible',
        id='document-visibility-demo-output'
    ),
    text='状态延时2s切换中',
    size='small'
)

...

@app.callback(
    Output('document-visibility-demo-output', 'children'),
    Input('document-visibility-demo', 'documentVisibility')
)
def document_visibility_demo(documentVisibility):

    if documentVisibility == 'visible':

        time.sleep(2)

    return f'documentVisibility: {documentVisibility}'
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
            component_name='FefferyDocumentVisibility'
        )
    ],
    style={
        'display': 'flex'
    }
)
