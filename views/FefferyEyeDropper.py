from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc

import callbacks.FefferyEyeDropper
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
                            'title': 'FefferyEyeDropper 色彩拾取'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　全屏幕色彩拾取。')
                    ]
                ),

                html.Div(
                    [
                        fac.AntdSpace(
                            [
                                fac.AntdButton(
                                    '开启拾取',
                                    id='enable-eye-dropper',
                                    type='primary'
                                ),

                                fuc.FefferyEyeDropper(
                                    id='eye-dropper-demo'
                                ),

                                html.Div(
                                    id='eye-dropper-demo-output',
                                    style={
                                        'width': '200px',
                                        'height': '200px',
                                        'display': 'flex',
                                        'alignItems': 'center',
                                        'justifyContent': 'center',
                                        'borderRadius': '5px',
                                        'boxShadow': '0px 0px 12px rgba(0, 0, 0, .12)',
                                        'transition': '0.25s'
                                    }
                                )
                            ],
                            size='large'
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
fac.AntdSpace(
    [
        fac.AntdButton(
            '开启拾取',
            id='enable-eye-dropper',
            type='primary'
        ),

        fuc.FefferyEyeDropper(
            id='eye-dropper-demo'
        ),

        html.Div(
            id='eye-dropper-demo-output',
            style={
                'width': '200px',
                'height': '200px',
                'display': 'flex',
                'alignItems': 'center',
                'justifyContent': 'center',
                'borderRadius': '5px',
                'boxShadow': '0px 0px 12px rgba(0, 0, 0, .12)',
                'transition': '0.25s'
            }
        )
    ],
    size='large'
)

...

@app.callback(
    Output('eye-dropper-demo', 'enable'),
    Input('enable-eye-dropper', 'nClicks'),
    prevent_initial_call=True
)
def enable_eye_dropper_demo(nClicks):

    return True


@app.callback(
    Output('eye-dropper-demo-output', 'style'),
    Input('eye-dropper-demo', 'color'),
    State('eye-dropper-demo-output', 'style'),
    prevent_initial_call=True
)
def eye_dropper_demo(color, old_style):

    return {
        **old_style,
        'background': color
    }
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
            component_name='FefferyEyeDropper'
        )
    ],
    style={
        'display': 'flex'
    }
)
