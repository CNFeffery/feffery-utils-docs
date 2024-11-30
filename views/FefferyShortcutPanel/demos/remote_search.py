import random
import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdParagraph(
            [
                fac.AntdText('提示：按下快捷组合键'),
                fac.AntdText('ctrl+s', keyboard=True),
                fac.AntdText(
                    '唤出本示例中的快捷指令面板，在搜索框中输入内容进行远程选项搜索'
                ),
            ]
        ),
        fuc.FefferyShortcutPanel(
            id='shortcut-panel-demo', openHotkey='cmd+s,ctrl+s', data=[]
        ),
    ]

    return demo_contents


@app.callback(
    Output('shortcut-panel-demo', 'data'),
    Input('shortcut-panel-demo', 'searchValue'),
    prevent_initial_call=True,
)
def shortcut_panel_demo(searchValue):
    return [
        {
            'id': f'{searchValue}搜索结果{i}',
            'title': f'{searchValue}搜索结果{i}',
        }
        for i in range(1, random.randint(3, 6))
    ]


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
[
    fac.AntdParagraph(
        [
            fac.AntdText('提示：按下快捷组合键'),
            fac.AntdText('ctrl+s', keyboard=True),
            fac.AntdText(
                '唤出本示例中的快捷指令面板，在搜索框中输入内容进行远程选项搜索'
            ),
        ]
    ),
    fuc.FefferyShortcutPanel(
        id='shortcut-panel-demo', openHotkey='cmd+s,ctrl+s', data=[]
    ),
]

...

@app.callback(
    Output('shortcut-panel-demo', 'data'),
    Input('shortcut-panel-demo', 'searchValue'),
    prevent_initial_call=True,
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
        }
    ]
