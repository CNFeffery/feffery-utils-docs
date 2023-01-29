from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_markdown_components as fmc

import callbacks.FefferyCssVar
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
                            'title': 'FefferyCssVar css变量更新'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　快捷批量更新css变量。')
                    ]
                ),

                html.Div(
                    [
                        fac.AntdSpace(
                            [
                                fac.AntdSwitch(
                                    id='css-var-demo',
                                    checked=False,
                                    unCheckedChildren='🌞',
                                    checkedChildren='🌛'
                                ),

                                fuc.FefferyCssVar(
                                    id='css-var-demo-output'
                                ),

                                html.Div(
                                    'FefferyCssVar示例',
                                    style={
                                        'background': 'var(--demo-bg-color)',
                                        'color': 'var(--demo-color)',
                                        'display': 'flex',
                                        'justifyContent': 'center',
                                        'alignItems': 'center',
                                        'fontSize': '28px',
                                        'transition': '0.2s',
                                        'padding': '100px 150px',
                                        'borderRadius': '5px'
                                    }
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
                            fmc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString="""
fac.AntdSpace(
    [
        fac.AntdSwitch(
            id='css-var-demo',
            checked=False,
            unCheckedChildren='🌞',
            checkedChildren='🌛'
        ),

        fuc.FefferyCssVar(
            id='css-var-demo-output'
        ),

        html.Div(
            'FefferyCssVar示例',
            style={
                'background': 'var(--demo-bg-color)',
                'color': 'var(--demo-color)',
                'display': 'flex',
                'justifyContent': 'center',
                'alignItems': 'center',
                'fontSize': '28px',
                'transition': '0.2s',
                'padding': '100px 150px',
                'borderRadius': '5px'
            }
        )
    ],
    direction='vertical'
)

...

# 使用浏览器端回调以实现更丝滑的响应速度
app.clientside_callback(
    '''(checked) => {
        if (checked) {
            return {
                '--demo-bg-color': 'black',
                '--demo-color': 'white'
            }
        }
        return {
            '--demo-bg-color': '#fffbe6',
            '--demo-color': 'black'
        }
    }''',
    Output('css-var-demo-output', 'cssVars'),
    Input('css-var-demo', 'checked')
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
            component_name='FefferyCssVar'
        )
    ],
    style={
        'display': 'flex'
    }
)
