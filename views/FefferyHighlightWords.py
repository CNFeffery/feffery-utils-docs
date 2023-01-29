from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_markdown_components as fmc

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
                            'title': 'FefferyHighlightWords 关键词高亮'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　用于对原始字符串中符合匹配规则的内容施加高亮效果。')
                    ]
                ),

                html.Div(
                    [
                        fuc.FefferyHighlightWords(
                            textToHighlight="""　　从来就没有什么救世主，
也不靠神仙皇帝。
要创造人类的幸福，
全靠我们自己。
我们要夺回劳动果实，
让思想冲破牢笼。
快把那炉火烧得通红，
趁热打铁才能成功！
这是最后的斗争，
团结起来，到明天，
英特纳雄耐尔就一定要实现。""",
                            searchWords=['我们', '团结']
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
fuc.FefferyHighlightWords(
    textToHighlight="""　　从来就没有什么救世主，
也不靠神仙皇帝。
要创造人类的幸福，
全靠我们自己。
我们要夺回劳动果实，
让思想冲破牢笼。
快把那炉火烧得通红，
趁热打铁才能成功！
这是最后的斗争，
团结起来，到明天，
英特纳雄耐尔就一定要实现。""",
    searchWords=['我们', '团结']
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
                        fac.AntdDivider(
                            '例：高亮包含“我们”的句子',
                            innerTextOrientation='left'
                        ),

                        fuc.FefferyHighlightWords(
                            textToHighlight="""　　从来就没有什么救世主，
也不靠神仙皇帝。
要创造人类的幸福，
全靠我们自己。
我们要夺回劳动果实，
让思想冲破牢笼。
快把那炉火烧得通红，
趁热打铁才能成功！
这是最后的斗争，
团结起来，到明天，
英特纳雄耐尔就一定要实现。""",
                            searchWords=[
                                '([\u4e00-\u9fa5]*我们[\u4e00-\u9fa5]*)'],
                            useRegex=True
                        ),

                        fac.AntdDivider(
                            '使用正则表达式',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fmc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdDivider(
    '例：高亮包含“我们”的句子',
    innerTextOrientation='left'
),

fuc.FefferyHighlightWords(
    textToHighlight="""　　从来就没有什么救世主，
也不靠神仙皇帝。
要创造人类的幸福，
全靠我们自己。
我们要夺回劳动果实，
让思想冲破牢笼。
快把那炉火烧得通红，
趁热打铁才能成功！
这是最后的斗争，
团结起来，到明天，
英特纳雄耐尔就一定要实现。""",
    searchWords=['([\u4e00-\u9fa5]*我们[\u4e00-\u9fa5]*)'],
    useRegex=True
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
                    id='使用正则表达式',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fuc.FefferyHighlightWords(
                            textToHighlight="""　　从来就没有什么救世主，
也不靠神仙皇帝。
要创造人类的幸福，
全靠我们自己。
我们要夺回劳动果实，
让思想冲破牢笼。
快把那炉火烧得通红，
趁热打铁才能成功！
这是最后的斗争，
团结起来，到明天，
英特纳雄耐尔就一定要实现。""",
                            searchWords=['我们', '团结'],
                            highlightStyle={
                                'background': 'linear-gradient(90deg,#ff75c3,#ffa647,#ffe83f,#9fff5b,#70e2ff,#cd93ff)',
                                'padding': 0,
                                'color': 'white'
                            }
                        ),

                        html.Br(),

                        fuc.FefferyHighlightWords(
                            textToHighlight="""　　从来就没有什么救世主，
也不靠神仙皇帝。
要创造人类的幸福，
全靠我们自己。
我们要夺回劳动果实，
让思想冲破牢笼。
快把那炉火烧得通红，
趁热打铁才能成功！
这是最后的斗争，
团结起来，到明天，
英特纳雄耐尔就一定要实现。""",
                            searchWords=['我们', '团结'],
                            highlightStyle={
                                'fontWeight': 'bold',
                                'backgroundColor': 'transparent',
                                'padding': 0,
                                'color': 'red'
                            },
                            unhighlightStyle={
                                'color': '#bfbfbf'
                            }
                        ),

                        fac.AntdDivider(
                            '自定义高亮/非高亮内容样式',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fmc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString='''
fuc.FefferyHighlightWords(
    textToHighlight="""　　从来就没有什么救世主，
也不靠神仙皇帝。
要创造人类的幸福，
全靠我们自己。
我们要夺回劳动果实，
让思想冲破牢笼。
快把那炉火烧得通红，
趁热打铁才能成功！
这是最后的斗争，
团结起来，到明天，
英特纳雄耐尔就一定要实现。""",
    searchWords=['我们', '团结'],
    highlightStyle={
        'background': 'linear-gradient(90deg,#ff75c3,#ffa647,#ffe83f,#9fff5b,#70e2ff,#cd93ff)',
        'padding': 0,
        'color': 'white'
    }
),

html.Br(),

fuc.FefferyHighlightWords(
    textToHighlight="""　　从来就没有什么救世主，
也不靠神仙皇帝。
要创造人类的幸福，
全靠我们自己。
我们要夺回劳动果实，
让思想冲破牢笼。
快把那炉火烧得通红，
趁热打铁才能成功！
这是最后的斗争，
团结起来，到明天，
英特纳雄耐尔就一定要实现。""",
    searchWords=['我们', '团结'],
    highlightStyle={
        'fontWeight': 'bold',
        'backgroundColor': 'transparent',
        'padding': 0,
        'color': 'red'
    },
    unhighlightStyle={
        'color': '#bfbfbf'
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
                    id='自定义高亮/非高亮内容样式',
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
                    {'title': '使用正则表达式', 'href': '#使用正则表达式'},
                    {'title': '自定义高亮/非高亮内容样式', 'href': '#自定义高亮/非高亮内容样式'},
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
            component_name='FefferyHighlightWords'
        )
    ],
    style={
        'display': 'flex'
    }
)
