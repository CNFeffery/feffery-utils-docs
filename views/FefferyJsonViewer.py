from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc

import callbacks.FefferyJsonViewer
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
                            'title': 'FefferyJsonViewer json数据展示'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　用于展示和交互式编辑json数据。')
                    ]
                ),

                html.Div(
                    [
                        fuc.FefferyJsonViewer(
                            data={
                                'int示例': 999,
                                'float示例': 0.999,
                                'string示例': '我爱dash',
                                '数组示例': [0, 1, 2, 3],
                                '字典示例': {
                                    'a': 1,
                                    'b': 2,
                                    'c': 3
                                }
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
fuc.FefferyJsonViewer(
    data={
        'int示例': 999,
        'float示例': 0.999,
        'string示例': '我爱dash',
        '数组示例': [0, 1, 2, 3],
        '字典示例': {
            'a': 1,
            'b': 2,
            'c': 3
        }
    }
)
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

                html.Div(
                    [
                        fac.AntdForm(
                            [
                                fac.AntdFormItem(
                                    fac.AntdSelect(
                                        id='json-viewer-demo1-theme',
                                        options=[
                                            {
                                                'label': theme,
                                                'value': theme
                                            }
                                            for theme in [
                                                'summerfruit:inverted', 'apathy', 'apathy:inverted', 'ashes', 'bespin',
                                                'bright:inverted', 'bright', 'chalk', 'codeschool', 'colors',
                                                'eighties', 'embers', 'flat', 'google', 'grayscale',
                                                'grayscale:inverted', 'greenscreen', 'harmonic', 'hopscotch',
                                                'isotope', 'marrakesh', 'mocha', 'monokai', 'ocean', 'paraiso',
                                                'pop', 'railscasts', 'rjv-default', 'shapeshifter',
                                                'shapeshifter:inverted', 'solarized', 'summerfruit',
                                                'threezerotwofour', 'tomorrow',
                                                'tube', 'twilight', 'brewer'
                                            ]
                                        ],
                                        value='summerfruit:inverted',
                                        allowClear=False,
                                        placement='topLeft',
                                        style={
                                            'width': '200px'
                                        }
                                    ),
                                    label='主题选择：'
                                )
                            ]
                        ),
                        fuc.FefferyJsonViewer(
                            id='json-viewer-demo1',
                            data={
                                'int示例': 999,
                                'float示例': 0.999,
                                'string示例': '我爱dash',
                                '数组示例': [0, 1, 2, 3],
                                '字典示例': {
                                    'a': 1,
                                    'b': 2,
                                    'c': 3
                                }
                            }
                        ),

                        fac.AntdDivider(
                            '使用不同的主题',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdForm(
    [
        fac.AntdFormItem(
            fac.AntdSelect(
                id='json-viewer-demo1-theme',
                options=[
                    {
                        'label': theme,
                        'value': theme
                    }
                    for theme in [
                        'summerfruit:inverted', 'apathy', 'apathy:inverted', 'ashes', 'bespin',
                        'bright:inverted', 'bright', 'chalk', 'codeschool', 'colors',
                        'eighties', 'embers', 'flat', 'google', 'grayscale',
                        'grayscale:inverted', 'greenscreen', 'harmonic', 'hopscotch',
                        'isotope', 'marrakesh', 'mocha', 'monokai', 'ocean', 'paraiso',
                        'pop', 'railscasts', 'rjv-default', 'shapeshifter',
                        'shapeshifter:inverted', 'solarized', 'summerfruit',
                        'threezerotwofour', 'tomorrow',
                        'tube', 'twilight', 'brewer'
                    ]
                ],
                value='summerfruit:inverted',
                allowClear=False,
                placement='topLeft',
                style={
                    'width': '200px'
                }
            ),
            label='主题选择：'
        )
    ]
),
fuc.FefferyJsonViewer(
    id='json-viewer-demo1',
    data={
        'int示例': 999,
        'float示例': 0.999,
        'string示例': '我爱dash',
        '数组示例': [0, 1, 2, 3],
        '字典示例': {
            'a': 1,
            'b': 2,
            'c': 3
        }
    }
)

...

@app.callback(
    Output('json-viewer-demo1', 'theme'),
    Input('json-viewer-demo1-theme', 'value')
)
def json_viewer_demo1(value):

    return value
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
                    id='使用不同的主题',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdForm(
                            [
                                fac.AntdFormItem(
                                    fac.AntdInputNumber(
                                        id='json-viewer-demo2-indent',
                                        min=1,
                                        max=8,
                                        step=1,
                                        value=4,
                                        style={
                                            'width': '100px'
                                        }
                                    ),
                                    label='缩进空格数：'
                                )
                            ]
                        ),
                        fuc.FefferyJsonViewer(
                            id='json-viewer-demo2',
                            data={
                                'int示例': 999,
                                'float示例': 0.999,
                                'string示例': '我爱dash',
                                '数组示例': [0, 1, 2, 3],
                                '字典示例': {
                                    'a': 1,
                                    'b': 2,
                                    'c': 3
                                }
                            }
                        ),

                        fac.AntdDivider(
                            '修改缩进大小',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdForm(
    [
        fac.AntdFormItem(
            fac.AntdInputNumber(
                id='json-viewer-demo2-indent',
                min=1,
                max=8,
                step=1,
                value=4,
                style={
                    'width': '100px'
                }
            ),
            label='缩进空格数：'
        )
    ]
),
fuc.FefferyJsonViewer(
    id='json-viewer-demo2',
    data={
        'int示例': 999,
        'float示例': 0.999,
        'string示例': '我爱dash',
        '数组示例': [0, 1, 2, 3],
        '字典示例': {
            'a': 1,
            'b': 2,
            'c': 3
        }
    }
)

...

@app.callback(
    Output('json-viewer-demo2', 'indent'),
    Input('json-viewer-demo2-indent', 'value')
)
def json_viewer_demo2(value):

    return value or 4
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
                    id='修改缩进大小',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fuc.FefferyJsonViewer(
                            data={
                                'int示例': 999,
                                'float示例': 0.999,
                                'string示例': '我爱dash',
                                '数组示例': [0, 1, 2, 3],
                                '字典示例': {
                                    'a': 1,
                                    'b': 2,
                                    'c': 3
                                }
                            },
                            editable=True,
                            addible=True,
                            deletable=True
                        ),

                        fac.AntdDivider(
                            '开启编辑、追加、删除功能',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                fac.AntdText(
                                    '　　对数据的编辑、追加、删除操作会随即更新data属性，你可以通过回调来捕获data最新的状态'
                                )
                            ]
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString='''
fuc.FefferyJsonViewer(
    data={
        'int示例': 999,
        'float示例': 0.999,
        'string示例': '我爱dash',
        '数组示例': [0, 1, 2, 3],
        '字典示例': {
            'a': 1,
            'b': 2,
            'c': 3
        }
    },
    editable=True,
    addible=True,
    deletable=True
)
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
                    id='开启编辑、追加、删除功能',
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
                    {'title': '使用不同的主题', 'href': '#使用不同的主题'},
                    {'title': '修改缩进大小', 'href': '#修改缩进大小'},
                    {'title': '开启编辑、追加、删除功能', 'href': '#开启编辑、追加、删除功能'},
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
            component_name='FefferyJsonViewer'
        )
    ],
    style={
        'display': 'flex'
    }
)
