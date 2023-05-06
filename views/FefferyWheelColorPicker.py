from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_markdown_components as fmc

import callbacks.FefferyWheelColorPicker
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
                            'title': 'FefferyWheelColorPicker Wheel风格色彩选择器'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　Wheel风格色彩选择器。')
                    ]
                ),

                html.Div(
                    [
                        fac.AntdSpace(
                            [
                                fuc.FefferyWheelColorPicker(
                                    id='wheel-color-picker-demo'
                                ),

                                html.Div(
                                    id='wheel-color-picker-demo-output',
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
                            fmc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdSpace(
    [
        fuc.FefferyWheelColorPicker(
            id='wheel-color-picker-demo'
        ),

        html.Div(
            id='wheel-color-picker-demo-output',
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
    [Output('wheel-color-picker-demo-output', 'style'),
     Output('wheel-color-picker-demo-output', 'children')],
    Input('wheel-color-picker-demo', 'color'),
    State('wheel-color-picker-demo-output', 'style')
)
def wheel_color_picker_demo(color, old_style):

    return [
        {
            **old_style,
            'background': color
        },
        color
    ]

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
            component_name='FefferyWheelColorPicker'
        )
    ],
    style={
        'display': 'flex'
    }
)
