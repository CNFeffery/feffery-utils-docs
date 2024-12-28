import uuid
import dash
import random
import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component, Input, Output, State

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdSpace(
            [
                fac.AntdButton(
                    '加载子元素', id='auto-animate-demo-load-children'
                ),
                fac.AntdButton('追加子元素', id='auto-animate-demo-push-child'),
                fac.AntdButton(
                    '随机打乱顺序', id='auto-animate-demo-random-order'
                ),
                fac.AntdButton(
                    '随机删除一项', id='auto-animate-demo-random-delete'
                ),
            ]
        ),
        fuc.FefferyAutoAnimate(id='auto-animate-demo-container'),
    ]

    return demo_contents


@app.callback(
    Output('auto-animate-demo-container', 'children'),
    [
        Input('auto-animate-demo-load-children', 'nClicks'),
        Input('auto-animate-demo-push-child', 'nClicks'),
        Input('auto-animate-demo-random-order', 'nClicks'),
    ],
    Input('auto-animate-demo-random-delete', 'nClicks'),
    State('auto-animate-demo-container', 'children'),
    prevent_initial_call=True,
)
def auto_animate_demo(
    load_children, push_chjild, random_order, random_delete, old_children
):
    if dash.ctx.triggered_id == 'auto-animate-demo-load-children':
        new_children = []
        for i in range(3):
            current_uuid = str(uuid.uuid4())
            new_children.append(
                fuc.FefferyDiv(
                    current_uuid,
                    id=current_uuid,
                    style={
                        'width': '460px',
                        'height': '40px',
                        'marginTop': '5px',
                        'border': '1px solid #e1dfdd',
                        'display': 'flex',
                        'justifyContent': 'center',
                        'alignItems': 'center',
                        'cursor': 'pointer',
                    },
                    shadow='hover-shadow',
                )
            )
        return new_children

    elif dash.ctx.triggered_id == 'auto-animate-demo-push-child':
        current_uuid = str(uuid.uuid4())
        return [
            *old_children,
            fuc.FefferyDiv(
                current_uuid,
                id=current_uuid,
                style={
                    'width': '460px',
                    'height': '40px',
                    'marginTop': '5px',
                    'border': '1px solid #e1dfdd',
                    'display': 'flex',
                    'justifyContent': 'center',
                    'alignItems': 'center',
                    'cursor': 'pointer',
                },
                shadow='hover-shadow',
            ),
        ]

    elif dash.ctx.triggered_id == 'auto-animate-demo-random-order':
        random.shuffle(old_children)
        return old_children

    elif dash.ctx.triggered_id == 'auto-animate-demo-random-delete':
        delete_idx = random.randint(0, len(old_children) - 1)

        return [
            child for i, child in enumerate(old_children) if i != delete_idx
        ]


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
[
    fac.AntdSpace(
        [
            fac.AntdButton(
                '加载子元素', id='auto-animate-demo-load-children'
            ),
            fac.AntdButton('追加子元素', id='auto-animate-demo-push-child'),
            fac.AntdButton(
                '随机打乱顺序', id='auto-animate-demo-random-order'
            ),
            fac.AntdButton(
                '随机删除一项', id='auto-animate-demo-random-delete'
            ),
        ]
    ),
    fuc.FefferyAutoAnimate(id='auto-animate-demo-container'),
]

...

@app.callback(
    Output('auto-animate-demo-container', 'children'),
    [
        Input('auto-animate-demo-load-children', 'nClicks'),
        Input('auto-animate-demo-push-child', 'nClicks'),
        Input('auto-animate-demo-random-order', 'nClicks'),
    ],
    Input('auto-animate-demo-random-delete', 'nClicks'),
    State('auto-animate-demo-container', 'children'),
    prevent_initial_call=True,
)
def auto_animate_demo(
    load_children, push_chjild, random_order, random_delete, old_children
):
    if dash.ctx.triggered_id == 'auto-animate-demo-load-children':
        new_children = []
        for i in range(3):
            current_uuid = str(uuid.uuid4())
            new_children.append(
                fuc.FefferyDiv(
                    current_uuid,
                    id=current_uuid,
                    style={
                        'width': '460px',
                        'height': '40px',
                        'marginTop': '5px',
                        'border': '1px solid #e1dfdd',
                        'display': 'flex',
                        'justifyContent': 'center',
                        'alignItems': 'center',
                        'cursor': 'pointer',
                    },
                    shadow='hover-shadow',
                )
            )
        return new_children

    elif dash.ctx.triggered_id == 'auto-animate-demo-push-child':
        current_uuid = str(uuid.uuid4())
        return [
            *old_children,
            fuc.FefferyDiv(
                current_uuid,
                id=current_uuid,
                style={
                    'width': '460px',
                    'height': '40px',
                    'marginTop': '5px',
                    'border': '1px solid #e1dfdd',
                    'display': 'flex',
                    'justifyContent': 'center',
                    'alignItems': 'center',
                    'cursor': 'pointer',
                },
                shadow='hover-shadow',
            ),
        ]

    elif dash.ctx.triggered_id == 'auto-animate-demo-random-order':
        random.shuffle(old_children)
        return old_children

    elif dash.ctx.triggered_id == 'auto-animate-demo-random-delete':
        delete_idx = random.randint(0, len(old_children) - 1)

        return [
            child for i, child in enumerate(old_children) if i != delete_idx
        ]
"""
        }
    ]
