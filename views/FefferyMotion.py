from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_markdown_components as fmc

import callbacks.FefferyMotion
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
                            'title': 'FefferyMotion 动画编排'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　用于轻松灵活的创建各种样式过渡动画效果。')
                    ]
                ),

                html.Div(
                    [
                        fuc.FefferyMotion(
                            style={
                                'background': '#71afe5',
                                'width': '50px',
                                'height': '50px',
                                'marginBottom': '10px'
                            },
                            animate={
                                'transform': 'translateX(200px)',
                                'background': '#d83b01'
                            },
                            transition={
                                # 无限循环动画
                                'repeat': 'infinity',
                                'duration': 2
                            }
                        ),

                        fuc.FefferyMotion(
                            '示例',
                            style={
                                'border': '1px dashed #71afe5',
                                'width': '100px',
                                'height': '100px',
                                'display': 'flex',
                                'justifyContent': 'center',
                                'alignItems': 'center'
                            },
                            animate={
                                'transform': 'translateX(300px) rotate(180deg)',
                                'borderRadius': '100%'
                            },
                            transition={
                                # 无限循环动画
                                'repeat': 'infinity',
                                'duration': 2
                            }
                        ),

                        fac.AntdDivider(
                            '基础使用',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                fac.AntdText('FefferyMotion()', code=True),
                                fac.AntdText('本质上是'),
                                fac.AntdText('Div', strong=True),
                                fac.AntdText(
                                    '容器，既可以作为动画编排的本体，也可以充当容器对内部元素编排动画效果')
                            ],
                            style={
                                'textIndent': '2rem'
                            }
                        ),

                        fac.AntdCollapse(
                            fmc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString='''
fuc.FefferyMotion(
    style={
        'background': '#71afe5',
        'width': '50px',
        'height': '50px',
        'marginBottom': '10px'
    },
    animate={
        'transform': 'translateX(200px)',
        'background': '#d83b01'
    },
    transition={
        # 无限循环动画
        'repeat': 'infinity',
        'duration': 2
    }
),

fuc.FefferyMotion(
    '示例',
    style={
        'border': '1px dashed #71afe5',
        'width': '100px',
        'height': '100px',
        'display': 'flex',
        'justifyContent': 'center',
        'alignItems': 'center'
    },
    animate={
        'transform': 'translateX(300px) rotate(180deg)',
        'borderRadius': '100%'
    },
    transition={
        # 无限循环动画
        'repeat': 'infinity',
        'duration': 2
    }
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
                        html.Div(
                            [
                                fuc.FefferyMotion(
                                    style={
                                        'background': '#71afe5',
                                        'width': '50px',
                                        'height': '50px',
                                        'marginBottom': '75px'
                                    },
                                    animate={
                                        'x': [50, 50, 0, 0, 50],
                                        'y': [0, 50, 50, 0, 0],
                                        'background': ['#d83b01', '#fff100', '#d83b01', '#fff100', '#d83b01']
                                    },
                                    transition={
                                        # 无限循环动画
                                        'repeat': 'infinity',
                                        'duration': 2
                                    }
                                ),
                                fuc.FefferyMotion(
                                    style={
                                        'background': '#605e5c',
                                        'width': '25px',
                                        'height': '25px',
                                        'borderRadius': '100%',
                                        'marginLeft': '25px'
                                    },
                                    animate={
                                        'scale': [2, 1, 2],
                                        'background': ['#e1dfdd', '#605e5c', '#e1dfdd']
                                    },
                                    transition={
                                        # 无限循环动画
                                        'repeat': 'infinity',
                                        'duration': 2,
                                        'times': [0.1, 0.9, 1]
                                    }
                                )
                            ],
                            style={
                                'width': '200px',
                                'height': '200px'
                            }
                        ),

                        fac.AntdDivider(
                            '配置多段动画',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                fac.AntdText(
                                    '配置目标样式时设置为等长度的数组，可以编排出连贯的多段动画实现循环播放效果'
                                )
                            ],
                            style={
                                'textIndent': '2rem'
                            }
                        ),

                        fac.AntdCollapse(
                            fmc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString='''
html.Div(
    [
        fuc.FefferyMotion(
            style={
                'background': '#71afe5',
                'width': '50px',
                'height': '50px',
                'marginBottom': '75px'
            },
            animate={
                'x': [50, 50, 0, 0, 50],
                'y': [0, 50, 50, 0, 0],
                'background': ['#d83b01', '#fff100', '#d83b01', '#fff100', '#d83b01']
            },
            transition={
                # 无限循环动画
                'repeat': 'infinity',
                'duration': 2
            }
        ),
        fuc.FefferyMotion(
            style={
                'background': '#605e5c',
                'width': '25px',
                'height': '25px',
                'borderRadius': '100%',
                'marginLeft': '25px'
            },
            animate={
                'scale': [2, 1, 2],
                'background': ['#e1dfdd', '#605e5c', '#e1dfdd']
            },
            transition={
                # 无限循环动画
                'repeat': 'infinity',
                'duration': 2,
                'times': [0.1, 0.9, 1]
            }
        )
    ],
    style={
        'width': '200px',
        'height': '200px'
    }
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
                    id='配置多段动画',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdSpace(
                            [
                                fuc.FefferyMotion(
                                    '鼠标悬停',
                                    style={
                                        'width': '75px',
                                        'borderRadius': '12px',
                                        'background': '#71afe5',
                                        'textAlign': 'center',
                                        'cursor': 'pointer'
                                    },
                                    whileHover={
                                        'scale': 1.5
                                    }
                                ),
                                fuc.FefferyMotion(
                                    '鼠标点按',
                                    style={
                                        'width': '75px',
                                        'borderRadius': '12px',
                                        'background': '#ff8c00',
                                        'textAlign': 'center',
                                        'cursor': 'pointer'
                                    },
                                    whileTap={
                                        'scale': 1.5
                                    }
                                ),
                                html.Div(
                                    [
                                        fac.AntdText('向下滑动'),
                                        fuc.FefferyMotion(
                                            style={
                                                'width': '50px',
                                                'height': '50px',
                                                'background': '#000000',
                                                'opacity': 0,
                                                'marginBottom': 400,
                                                'marginTop': 400
                                            },
                                            whileInView={
                                                'opacity': 1,
                                                'borderRadius': '100%'
                                            },
                                            transition={
                                                'duration': 3
                                            },
                                            viewport={
                                                'once': False
                                            }
                                        )
                                    ],
                                    style={
                                        'border': '1px dashed #323130',
                                        'maxHeight': '150px',
                                        'overflow': 'auto',
                                        'padding': 25,
                                    }
                                )
                            ],
                            direction='vertical',
                            size=25,
                            style={
                                'paddingLeft': '25px',
                                'width': '100%'
                            }
                        ),

                        fac.AntdDivider(
                            '使用状态动画',
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
        fuc.FefferyMotion(
            '鼠标悬停',
            style={
                'width': '75px',
                'borderRadius': '12px',
                'background': '#71afe5',
                'textAlign': 'center',
                'cursor': 'pointer'
            },
            whileHover={
                'scale': 1.5
            }
        ),
        fuc.FefferyMotion(
            '鼠标点按',
            style={
                'width': '75px',
                'borderRadius': '12px',
                'background': '#ff8c00',
                'textAlign': 'center',
                'cursor': 'pointer'
            },
            whileTap={
                'scale': 1.5
            }
        ),
        html.Div(
            [
                fac.AntdText('向下滑动'),
                fuc.FefferyMotion(
                    style={
                        'width': '50px',
                        'height': '50px',
                        'background': '#000000',
                        'opacity': 0,
                        'marginBottom': 400,
                        'marginTop': 400
                    },
                    whileInView={
                        'opacity': 1,
                        'borderRadius': '100%'
                    },
                    transition={
                        'duration': 3
                    },
                    viewport={
                        'once': False
                    }
                )
            ],
            style={
                'border': '1px dashed #323130',
                'maxHeight': '150px',
                'overflow': 'auto',
                'padding': 25,
            }
        )
    ],
    direction='vertical',
    size=25,
    style={
        'paddingLeft': '25px',
        'width': '100%'
    }
)
"""
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
                    id='使用状态动画',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fuc.FefferyMotion(
                            style={
                                'background': '#71afe5',
                                'width': '50px',
                                'height': '50px',
                                'marginBottom': '10px'
                            },
                            animate={
                                'transform': 'translateX(200px)',
                                'background': '#d83b01'
                            },
                            transition={
                                # 无限循环动画
                                'repeat': 'infinity',
                                'duration': 2,
                                'type': 'spring'
                            }
                        ),

                        fuc.FefferyMotion(
                            '示例',
                            style={
                                'border': '1px dashed #71afe5',
                                'width': '100px',
                                'height': '100px',
                                'display': 'flex',
                                'justifyContent': 'center',
                                'alignItems': 'center'
                            },
                            animate={
                                'transform': 'translateX(300px) rotate(180deg)',
                                'borderRadius': '100%'
                            },
                            transition={
                                # 无限循环动画
                                'repeat': 'infinity',
                                'duration': 2,
                                'type': 'spring'
                            }
                        ),

                        fac.AntdDivider(
                            '使用弹簧物理动画',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                fac.AntdText('通过设置参数'),
                                fac.AntdText(
                                    'transition.type="spring"', code=True),
                                fac.AntdText(
                                    '可以实现更适用于部分场景更自然的物理效果'
                                )
                            ],
                            style={
                                'textIndent': '2rem'
                            }
                        ),

                        fac.AntdCollapse(
                            fmc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString='''
fuc.FefferyMotion(
    style={
        'background': '#71afe5',
        'width': '50px',
        'height': '50px',
        'marginBottom': '10px'
    },
    animate={
        'transform': 'translateX(200px)',
        'background': '#d83b01'
    },
    transition={
        # 无限循环动画
        'repeat': 'infinity',
        'duration': 2,
        'type': 'spring'
    }
),

fuc.FefferyMotion(
    '示例',
    style={
        'border': '1px dashed #71afe5',
        'width': '100px',
        'height': '100px',
        'display': 'flex',
        'justifyContent': 'center',
        'alignItems': 'center'
    },
    animate={
        'transform': 'translateX(300px) rotate(180deg)',
        'borderRadius': '100%'
    },
    transition={
        # 无限循环动画
        'repeat': 'infinity',
        'duration': 2,
        'type': 'spring'
    }
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
                    id='使用弹簧物理动画',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdSpace(
                            [
                                fac.AntdSegmented(
                                    id='motion-fade-in-demo',
                                    options=[
                                        {
                                            'label': f'选项{i}',
                                            'value': f'选项{i}'
                                        }
                                        for i in range(1, 6)
                                    ],
                                    block=True,
                                    value='选项1'
                                ),

                                html.Div(
                                    id='motion-fade-in-demo-output'
                                )
                            ],
                            direction='vertical',
                            style={
                                'width': '100%'
                            }
                        ),

                        fac.AntdDivider(
                            '实现元素挂载特效',
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
        fac.AntdSegmented(
            id='motion-fade-in-demo',
            options=[
                {
                    'label': f'选项{i}',
                    'value': f'选项{i}'
                }
                for i in range(1, 6)
            ],
            block=True,
            value='选项1'
        ),

        html.Div(
            id='motion-fade-in-demo-output'
        )
    ],
    direction='vertical',
    style={
        'width': '100%'
    }
)

...

@app.callback(
    Output('motion-fade-in-demo-output', 'children'),
    Input('motion-fade-in-demo', 'value')
)
def motion_fade_in_demo(value):

    if value == '选项1':
        return fuc.FefferyMotion(
            f'淡入特效',
            id='motion-fade-in-demo-item1',
            style={
                'height': '200px',
                'background': '#00b294',
                'color': 'white',
                'display': 'flex',
                'justifyContent': 'center',
                'alignItems': 'center'
            },
            initial={
                'opacity': 0
            },
            animate={
                'opacity': 1
            },
            transition={
                'duration': 0.3
            }
        )

    elif value == '选项2':
        return fuc.FefferyMotion(
            f'上升+淡入特效',
            id='motion-fade-in-demo-item2',
            style={
                'height': '200px',
                'background': '#00b294',
                'color': 'white',
                'display': 'flex',
                'justifyContent': 'center',
                'alignItems': 'center'
            },
            initial={
                'opacity': 0,
                'marginTop': 25
            },
            animate={
                'opacity': 1,
                'marginTop': 0
            },
            transition={
                'duration': 0.3
            }
        )

    elif value == '选项3':
        return fuc.FefferyMotion(
            f'从右进场+淡入特效',
            id='motion-fade-in-demo-item3',
            style={
                'height': '200px',
                'background': '#00b294',
                'color': 'white',
                'display': 'flex',
                'justifyContent': 'center',
                'alignItems': 'center'
            },
            initial={
                'opacity': 0,
                'marginLeft': 25
            },
            animate={
                'opacity': 1,
                'marginLeft': 0
            },
            transition={
                'duration': 0.3
            }
        )

    elif value == '选项4':
        return fuc.FefferyMotion(
            f'从左进场+淡入特效',
            id='motion-fade-in-demo-item4',
            style={
                'height': '200px',
                'background': '#00b294',
                'color': 'white',
                'display': 'flex',
                'justifyContent': 'center',
                'alignItems': 'center'
            },
            initial={
                'opacity': 0,
                'marginRight': 25
            },
            animate={
                'opacity': 1,
                'marginRight': 0
            },
            transition={
                'duration': 0.3
            }
        )

    elif value == '选项5':
        return fuc.FefferyMotion(
            f'上升+3D+淡入特效',
            id='motion-fade-in-demo-item5',
            style={
                'height': '200px',
                'background': '#00b294',
                'color': 'white',
                'display': 'flex',
                'justifyContent': 'center',
                'alignItems': 'center'
            },
            initial={
                'opacity': 0,
                'marginTop': 25,
                'rotateX': '45deg'
            },
            animate={
                'opacity': 1,
                'marginTop': 0,
                'rotateX': '0deg'
            },
            transition={
                'duration': 0.75
            }
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
                    id='实现元素挂载特效',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        html.Div(
                            fuc.FefferyMotion(
                                html.Img(
                                    src='/assets/imgs/fuc-logo.svg',
                                    width=150
                                ),
                                animate='漂浮效果',
                                variants={
                                    '漂浮效果': {
                                        'y': [25, -25, 25],
                                        'rotateZ': ['-15deg', '15deg', '-15deg'],
                                        'scale': 1
                                    }
                                },
                                transition={
                                    'duration': 3,
                                    'repeat': 'infinity',
                                    'type': 'spring'
                                }
                            ),
                            style={
                                'display': 'flex',
                                'justifyContent': 'center',
                                'padding': '50px 0'
                            }
                        ),

                        fac.AntdDivider(
                            '使用具有别名的样式组',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fmc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString='''
html.Div(
    fuc.FefferyMotion(
        html.Img(
            src='/assets/imgs/fuc-logo.svg',
            width=150
        ),
        animate='漂浮效果',
        variants={
            '漂浮效果': {
                'y': [25, -25, 25],
                'rotateZ': ['-15deg', '15deg', '-15deg'],
                'scale': 1
            }
        },
        transition={
            'duration': 3,
            'repeat': 'infinity',
            'type': 'spring'
        }
    ),
    style={
        'display': 'flex',
        'justifyContent': 'center',
        'padding': '50px 0'
    }
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
                    id='使用具有别名的样式组',
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
                    {'title': '配置多段动画', 'href': '#配置多段动画'},
                    {'title': '使用状态动画', 'href': '#使用状态动画'},
                    {'title': '使用弹簧物理动画', 'href': '#使用弹簧物理动画'},
                    {'title': '实现元素挂载特效', 'href': '#实现元素挂载特效'},
                    {'title': '使用具有别名的样式组', 'href': '#使用具有别名的样式组'},
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
            component_name='FefferyMotion'
        )
    ],
    style={
        'display': 'flex'
    }
)
