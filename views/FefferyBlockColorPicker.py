from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_markdown_components as fmc

import callbacks.FefferyBlockColorPicker
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
                            'title': 'FefferyBlockColorPicker Block风格色彩选择器'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　Block风格的16进制色彩选择器。')
                    ]
                ),

                html.Div(
                    [
                        fac.AntdSpace(
                            [
                                fuc.FefferyBlockColorPicker(),

                                fuc.FefferyBlockColorPicker(
                                    triangle='hide'
                                ),

                                fuc.FefferyBlockColorPicker(
                                    colors=[
                                        '#fff4ce', '#797673', '#fed9cc',
                                        '#d83b01', '#fde7e9', '#a80000',
                                        '#dff6dd', '#107c10'
                                    ]
                                )
                            ]
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
        fuc.FefferyBlockColorPicker(),

        fuc.FefferyBlockColorPicker(
            triangle='hide'
        ),

        fuc.FefferyBlockColorPicker(
            colors=[
                '#fff4ce', '#797673', '#fed9cc',
                '#d83b01', '#fde7e9', '#a80000',
                '#dff6dd', '#107c10'
            ]
        )
    ]
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

                html.Div(
                    [
                        fac.AntdSpace(
                            [
                                fuc.FefferyBlockColorPicker(
                                    id='block-color-picker-demo'
                                ),

                                html.Div(
                                    id='block-color-picker-demo-output',
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
                            '回调示例',
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
        fuc.FefferyBlockColorPicker(
            id='block-color-picker-demo'
        ),

        html.Div(
            id='block-color-picker-demo-output',
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
    Output('block-color-picker-demo-output', 'style'),
    Input('block-color-picker-demo', 'color'),
    State('block-color-picker-demo-output', 'style')
)
def block_color_picker_demo(color, old_style):

    return {
        **old_style,
        'background': color
    }
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
                    id='回调示例',
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
                    {'title': '基础使用', 'href': '#基础使用'},
                    {'title': '回调示例', 'href': '#回调示例'}
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
            component_name='FefferyBlockColorPicker'
        )
    ],
    style={
        'display': 'flex'
    }
)
