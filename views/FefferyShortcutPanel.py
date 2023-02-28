from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_markdown_components as fmc

from views.side_props import render_side_props_layout

# 绑定回调
import callbacks.FefferyShortcutPanel

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
                            'title': 'FefferyShortcutPanel 快捷指令面板'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　用于构建现代化的快捷指令操作面板，从而赋予应用更多操作性。')
                    ]
                ),

                html.Div(
                    [
                        fac.AntdParagraph(
                            [
                                fac.AntdText('提示：按下快捷组合键'),
                                fac.AntdText('ctrl+h', keyboard=True),
                                fac.AntdText('唤出本示例中的快捷指令面板')
                            ]
                        ),
                        fuc.FefferyShortcutPanel(
                            openHotkey='cmd+h,ctrl+h',
                            data=[
                                {
                                    'id': '指令1',
                                    'title': '指令1',
                                    'handler': '() => alert("指令1触发")',
                                    'section': '模拟js指令'
                                },
                                {
                                    'id': '指令2',
                                    'title': '指令2',
                                    'handler': '() => alert("指令2触发")',
                                    'section': '模拟js指令'
                                },
                                {
                                    'id': '跳转到首页',
                                    'title': '跳转到首页',
                                    'handler': '''() => {
                                        window.location = "/"
                                    }''',
                                    'section': '模拟js指令'
                                },
                                {
                                    'id': '指令3',
                                    'title': '指令3',
                                    'children': ['指令3-1', '指令3-2'],
                                    'section': '多层指令菜单项'
                                },
                                {
                                    'id': '指令3-1',
                                    'title': '指令3-1',
                                    'parent': '指令3'
                                },
                                {
                                    'id': '指令3-2',
                                    'title': '指令3-2',
                                    'parent': '指令3'
                                }
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
                                codeString="""
fac.AntdParagraph(
    [
        fac.AntdText('提示：按下快捷组合键'),
        fac.AntdText('ctrl+h', keyboard=True),
        fac.AntdText('唤出本示例中的快捷指令面板')
    ]
),
fuc.FefferyShortcutPanel(
    openHotkey='cmd+h,ctrl+h',
    data=[
        {
            'id': '指令1',
            'title': '指令1',
            'handler': '() => alert("指令1触发")',
            'section': '模拟js指令'
        },
        {
            'id': '指令2',
            'title': '指令2',
            'handler': '() => alert("指令2触发")',
            'section': '模拟js指令'
        },
        {
            'id': '跳转到首页',
            'title': '跳转到首页',
            'handler': '''() => {
                window.location = "/"
            }''',
            'section': '模拟js指令'
        },
        {
            'id': '指令3',
            'title': '指令3',
            'children': ['指令3-1', '指令3-2'],
            'section': '多层指令菜单项'
        },
        {
            'id': '指令3-1',
            'title': '指令3-1',
            'parent': '指令3'
        },
        {
            'id': '指令3-2',
            'title': '指令3-2',
            'parent': '指令3'
        }
    ]
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

                html.Div(
                    [
                        fac.AntdParagraph(
                            [
                                fac.AntdText('提示：按下快捷组合键'),
                                fac.AntdText('ctrl+s', keyboard=True),
                                fac.AntdText('唤出本示例中的快捷指令面板，在搜索框中输入内容进行远程选项搜索')
                            ]
                        ),
                        fuc.FefferyShortcutPanel(
                            id='shortcut-panel-demo',
                            openHotkey='cmd+s,ctrl+s',
                            data=[]
                        ),

                        fac.AntdDivider(
                            '远程搜索',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fmc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString="""
fac.AntdParagraph(
    [
        fac.AntdText('提示：按下快捷组合键'),
        fac.AntdText('ctrl+s', keyboard=True),
        fac.AntdText('唤出本示例中的快捷指令面板，在搜索框中输入内容进行远程选项搜索')
    ]
),
fuc.FefferyShortcutPanel(
    id='shortcut-panel-demo',
    openHotkey='cmd+s,ctrl+s',
    data=[]
)

...

import random

...

@app.callback(
    Output('shortcut-panel-demo', 'data'),
    Input('shortcut-panel-demo', 'searchValue'),
    prevent_initial_call=True
)
def shortcut_panel_demo(searchValue):

    return [
        {
            'id': f'{searchValue}搜索结果{i}',
            'title': f'{searchValue}搜索结果{i}',
        }
        for i in range(1, random.randint(3, 6))
    ]
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
                    id='远程搜索',
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
                    {'title': '远程搜索', 'href': '#远程搜索'},
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
            component_name='FefferyShortcutPanel'
        )
    ],
    style={
        'display': 'flex'
    }
)
