from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc

import callbacks.FefferyWindowSize
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
                            'title': 'FefferyIdle 闲置状态监听'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　用于监听当前应用是否进入闲置状态。')
                    ]
                ),

                html.Div(
                    [

                        fuc.FefferyWindowSize(
                            id='window-size-demo'
                        ),

                        fac.AntdText(
                            id='window-size-demo-output'
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
                                codeString='''
fuc.FefferyWindowSize(
    id='window-size-demo'
),

fac.AntdText(
    id='window-size-demo-output'
)

...

@app.callback(
    Output('window-size-demo-output', 'children'),
    [Input('window-size-demo', '_width'),
     Input('window-size-demo', '_height')]
)
def window_size_demo(_width, _height):

    return f'_width: {_width}  _height: {_height}'
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
            component_name='FefferyWindowSize'
        )
    ],
    style={
        'display': 'flex'
    }
)
