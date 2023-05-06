from dash import html, dcc
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_markdown_components as fmc

import callbacks.FefferyLocation
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
                            'title': 'FefferyLocation 地址监听'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('用于监听与当前应用地址变化相关的信息，可作为对'),
                        fac.AntdText(
                            'dcc.Location',
                            code=True
                        ),
                        '的直接替代，并提供更多额外的事件信息监听。'
                    ],
                    style={
                        'textIndent': '2rem'
                    }
                ),

                html.Div(
                    [
                        fuc.FefferyLocation(
                            id='location-demo'
                        ),

                        fac.AntdSpace(
                            [
                                fac.AntdText(
                                    '示例链接：'
                                ),
                                dcc.Link(
                                    '/FefferyLocation#基础使用',
                                    href='/FefferyLocation#基础使用'
                                ),
                                dcc.Link(
                                    '/FefferyLocation?a=1&b=2',
                                    href='/FefferyLocation?a=1&b=2'
                                )
                            ]
                        ),

                        html.Pre(
                            id='location-demo-output'
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
fuc.FefferyLocation(
    id='location-demo'
),

fac.AntdSpace(
    [
        fac.AntdText(
            '示例链接：'
        ),
        dcc.Link(
            '/FefferyLocation#基础使用',
            href='/FefferyLocation#基础使用'
        ),
        dcc.Link(
            '/FefferyLocation?a=1&b=2',
            href='/FefferyLocation?a=1&b=2'
        )
    ]
),

html.Pre(
    id='location-demo-output'
)

...

@app.callback(
    Output('location-demo-output', 'children'),
    [Input('location-demo', 'href'),
     Input('location-demo', 'pathname'),
     Input('location-demo', 'search'),
     Input('location-demo', 'hash'),
     Input('location-demo', 'host'),
     Input('location-demo', 'hostname'),
     Input('location-demo', 'port'),
     Input('location-demo', 'protocol'),
     Input('location-demo', 'trigger')]
)
def lcoation_demo(href,
                  pathname,
                  search,
                  hash,
                  host,
                  hostname,
                  port,
                  protocol,
                  trigger):

    return json.dumps(
        dict(
            href=href,
            pathname=pathname,
            search=search,
            hash=hash,
            host=host,
            hostname=hostname,
            port=port,
            protocol=protocol,
            trigger=trigger
        ),
        indent=4,
        ensure_ascii=False
    )
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
            component_name='FefferyLocation'
        )
    ],
    style={
        'display': 'flex'
    }
)
