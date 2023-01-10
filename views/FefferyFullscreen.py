from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc

import callbacks.FefferyFullscreen
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
                            'title': 'FefferyFullscreen 全屏化'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　用于对指定的目标元素进行全屏化渲染。')
                    ]
                ),

                html.Div(
                    [
                        fuc.FefferyFullscreen(
                            id='fullscreen-demo',
                            targetId='fullscreen-target'
                        ),
                        html.Div(
                            fac.AntdButton(
                                    '全屏化',
                                    id='toggle-fullscreen',
                                    type='primary'
                                ),
                            id='fullscreen-target',
                            style={
                                'height': '200px',
                                'display': 'flex',
                                'justifyContent': 'center',
                                'alignItems': 'center',
                                'background': 'white'
                            }
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
fuc.FefferyFullscreen(
    id='fullscreen-demo',
    targetId='fullscreen-target'
),
html.Div(
    fac.AntdButton(
            '全屏化',
            id='toggle-fullscreen',
            type='primary'
        ),
    id='fullscreen-target',
    style={
        'height': '200px',
        'display': 'flex',
        'justifyContent': 'center',
        'alignItems': 'center',
        'background': 'white'
    }
)

...

@app.callback(
    [Output('fullscreen-demo', 'isFullscreen'),
    Output('toggle-fullscreen', 'children')],
    Input('toggle-fullscreen', 'nClicks'),
    State('fullscreen-demo', 'isFullscreen'),
    prevent_initial_call=True
)
def toggle_fullscreen(nClicks, isFullscreen):

    return [
        not isFullscreen,
        '全屏化' if isFullscreen else '退出全屏化'
    ]
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
            component_name='FefferyFullscreen'
        )
    ],
    style={
        'display': 'flex'
    }
)
