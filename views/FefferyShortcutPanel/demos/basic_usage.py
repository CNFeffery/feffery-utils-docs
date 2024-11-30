import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdParagraph(
            [
                fac.AntdText('提示：按下快捷组合键'),
                fac.AntdText('ctrl+h', keyboard=True),
                fac.AntdText('唤出本示例中的快捷指令面板'),
            ]
        ),
        fuc.FefferyShortcutPanel(
            openHotkey='cmd+h,ctrl+h',
            data=[
                {
                    'id': '指令1',
                    'title': '指令1',
                    'handler': '() => alert("指令1触发")',
                    'section': '模拟js指令',
                },
                {
                    'id': '指令2',
                    'title': '指令2',
                    'handler': '() => alert("指令2触发")',
                    'section': '模拟js指令',
                },
                {
                    'id': '跳转到首页',
                    'title': '跳转到首页',
                    'handler': """() => {
                window.location = "/"
            }""",
                    'section': '模拟js指令',
                },
                {
                    'id': '指令3',
                    'title': '指令3',
                    'children': ['指令3-1', '指令3-2'],
                    'section': '多层指令菜单项',
                },
                {'id': '指令3-1', 'title': '指令3-1', 'parent': '指令3'},
                {'id': '指令3-2', 'title': '指令3-2', 'parent': '指令3'},
            ],
        ),
    ]

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': '''
[
    fac.AntdParagraph(
        [
            fac.AntdText('提示：按下快捷组合键'),
            fac.AntdText('ctrl+h', keyboard=True),
            fac.AntdText('唤出本示例中的快捷指令面板'),
        ]
    ),
    fuc.FefferyShortcutPanel(
        openHotkey='cmd+h,ctrl+h',
        data=[
            {
                'id': '指令1',
                'title': '指令1',
                'handler': '() => alert("指令1触发")',
                'section': '模拟js指令',
            },
            {
                'id': '指令2',
                'title': '指令2',
                'handler': '() => alert("指令2触发")',
                'section': '模拟js指令',
            },
            {
                'id': '跳转到首页',
                'title': '跳转到首页',
                'handler': """() => {
            window.location = "/"
        }""",
                'section': '模拟js指令',
            },
            {
                'id': '指令3',
                'title': '指令3',
                'children': ['指令3-1', '指令3-2'],
                'section': '多层指令菜单项',
            },
            {'id': '指令3-1', 'title': '指令3-1', 'parent': '指令3'},
            {'id': '指令3-2', 'title': '指令3-2', 'parent': '指令3'},
        ],
    ),
]
'''
        }
    ]
