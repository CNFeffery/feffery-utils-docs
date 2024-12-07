import uuid
import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdButton('触发功能引导', id='guide-show', type='primary'),
        fac.Fragment(id='guide-demo'),
    ]

    return demo_contents


@app.callback(
    Output('guide-demo', 'children'),
    Input('guide-show', 'nClicks'),
    prevent_initial_call=True,
)
def guide_demo(nClicks):
    return fuc.FefferyGuide(
        id='guide-demo-' + str(uuid.uuid4()),
        steps=[
            {
                'selector': '#guide-show',
                'title': '这是一个功能按钮',
                'content': '这里展示了本次功能引导的第一步内容。',
            },
            {
                'selector': '#global-locale-switch',
                'title': '这是国际化切换按钮',
                'content': '这里展示了本次功能引导的第二步内容。',
            },
            {
                'selector': '#open-global-search-panel',
                'title': '这是fuc官网的搜索面板触发区域',
                'content': '这里展示了本次功能引导的第三步内容。',
                'placement': 'bottom-left',
            },
            {
                'targetPos': {
                    'top': 200,
                    'left': 500,
                    'width': 100,
                    'height': 50,
                },
                'title': '这是自定义屏幕绝对位置锚点示例',
                'content': '这里展示了本次功能引导的第四步内容。',
            },
        ],
        localKey='guide-demo-' + str(uuid.uuid4()),
        closable=True,
    )


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
[
    fac.AntdButton('触发功能引导', id='guide-show', type='primary'),
    fac.Fragment(id='guide-demo'),
]

...

@app.callback(
    Output('guide-demo', 'children'),
    Input('guide-show', 'nClicks'),
    prevent_initial_call=True,
)
def guide_demo(nClicks):
    return fuc.FefferyGuide(
        id='guide-demo-' + str(uuid.uuid4()),
        steps=[
            {
                'selector': '#guide-show',
                'title': '这是一个功能按钮',
                'content': '这里展示了本次功能引导的第一步内容。',
            },
            {
                'selector': '#global-locale-switch',
                'title': '这是国际化切换按钮',
                'content': '这里展示了本次功能引导的第二步内容。',
            },
            {
                'selector': '#open-global-search-panel',
                'title': '这是fuc官网的搜索面板触发区域',
                'content': '这里展示了本次功能引导的第三步内容。',
                'placement': 'bottom-left',
            },
            {
                'targetPos': {
                    'top': 200,
                    'left': 500,
                    'width': 100,
                    'height': 50,
                },
                'title': '这是自定义屏幕绝对位置锚点示例',
                'content': '这里展示了本次功能引导的第四步内容。',
            },
        ],
        localKey='guide-demo-' + str(uuid.uuid4()),
        closable=True,
    )
"""
        }
    ]
