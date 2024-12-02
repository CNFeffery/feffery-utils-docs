import dash
from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdSpace(
            [
                fac.AntdButton(
                    '滚动至页面底部', id='scroll-to-bottom-demo', type='primary'
                ),
                fac.AntdButton(
                    '滚动至距离顶部800px处',
                    id='scroll-top-offset-demo',
                    type='primary',
                ),
                fac.AntdButton(
                    '相对当前位置向下滚动300px',
                    id='scroll-relative-offset-demo',
                    type='primary',
                ),
                fac.AntdButton(
                    '滚动至示例元素处', id='scroll-target-demo', type='primary'
                ),
            ],
            wrap=True,
            size='small',
        ),
        html.Div(
            [
                fac.AntdParagraph('示例目标元素', id='scroll-target-element'),
                fac.AntdButton(
                    '滚动至页面顶部', id='scroll-to-top-demo', type='primary'
                ),
            ],
            style={
                'padding': '1400px 0 800px 0',
                'background': 'linear-gradient(180deg,#1890ff80,#fff)',
            },
        ),
        html.Div(id='scroll-demo-output'),
    ]

    return demo_contents


@app.callback(
    Output('scroll-demo-output', 'children'),
    [
        Input('scroll-to-top-demo', 'nClicks'),
        Input('scroll-to-bottom-demo', 'nClicks'),
        Input('scroll-top-offset-demo', 'nClicks'),
        Input('scroll-relative-offset-demo', 'nClicks'),
        Input('scroll-target-demo', 'nClicks'),
    ],
    prevent_initial_call=True,
)
def scroll_demo(*args):
    # 基于dash的上下文功能获知当前回调由谁触发
    trigger_id = dash.ctx.triggered_id

    if trigger_id == 'scroll-to-top-demo':
        return fuc.FefferyScroll(executeScroll=True, scrollMode='to-top')

    elif trigger_id == 'scroll-to-bottom-demo':
        return fuc.FefferyScroll(executeScroll=True, scrollMode='to-bottom')

    elif trigger_id == 'scroll-top-offset-demo':
        return fuc.FefferyScroll(
            executeScroll=True, scrollMode='top-offset', scrollTopOffset=800
        )

    elif trigger_id == 'scroll-relative-offset-demo':
        return fuc.FefferyScroll(
            executeScroll=True,
            scrollMode='relative-offset',
            scrollRelativeOffset=300,
        )

    elif trigger_id == 'scroll-target-demo':
        return fuc.FefferyScroll(
            executeScroll=True,
            scrollMode='target',
            scrollTargetId='scroll-target-element',
        )


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
[
    fac.AntdSpace(
        [
            fac.AntdButton(
                '滚动至页面底部', id='scroll-to-bottom-demo', type='primary'
            ),
            fac.AntdButton(
                '滚动至距离顶部800px处',
                id='scroll-top-offset-demo',
                type='primary',
            ),
            fac.AntdButton(
                '相对当前位置向下滚动300px',
                id='scroll-relative-offset-demo',
                type='primary',
            ),
            fac.AntdButton(
                '滚动至示例元素处', id='scroll-target-demo', type='primary'
            ),
        ],
        wrap=True,
        size='small',
    ),
    html.Div(
        [
            fac.AntdParagraph('示例目标元素', id='scroll-target-element'),
            fac.AntdButton(
                '滚动至页面顶部', id='scroll-to-top-demo', type='primary'
            ),
        ],
        style={
            'padding': '1400px 0 800px 0',
            'background': 'linear-gradient(180deg,#1890ff80,#fff)',
        },
    ),
    html.Div(id='scroll-demo-output'),
]

...

@app.callback(
    Output('scroll-demo-output', 'children'),
    [
        Input('scroll-to-top-demo', 'nClicks'),
        Input('scroll-to-bottom-demo', 'nClicks'),
        Input('scroll-top-offset-demo', 'nClicks'),
        Input('scroll-relative-offset-demo', 'nClicks'),
        Input('scroll-target-demo', 'nClicks'),
    ],
    prevent_initial_call=True,
)
def scroll_demo(*args):
    # 基于dash的上下文功能获知当前回调由谁触发
    trigger_id = dash.ctx.triggered_id

    if trigger_id == 'scroll-to-top-demo':
        return fuc.FefferyScroll(executeScroll=True, scrollMode='to-top')

    elif trigger_id == 'scroll-to-bottom-demo':
        return fuc.FefferyScroll(executeScroll=True, scrollMode='to-bottom')

    elif trigger_id == 'scroll-top-offset-demo':
        return fuc.FefferyScroll(
            executeScroll=True, scrollMode='top-offset', scrollTopOffset=800
        )

    elif trigger_id == 'scroll-relative-offset-demo':
        return fuc.FefferyScroll(
            executeScroll=True,
            scrollMode='relative-offset',
            scrollRelativeOffset=300,
        )

    elif trigger_id == 'scroll-target-demo':
        return fuc.FefferyScroll(
            executeScroll=True,
            scrollMode='target',
            scrollTargetId='scroll-target-element',
        )
"""
        }
    ]
