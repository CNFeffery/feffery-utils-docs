from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_markdown_components as fmc

import callbacks.FefferyAutoAnimate
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
                            'title': 'FefferyAutoAnimate 自动动画'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　用于自动为子元素添加通用的动画过渡效果。')
                    ]
                ),

                html.Div(
                    [
                        fac.AntdSpace(
                            [
                                fac.AntdButton(
                                    '加载子元素',
                                    id='auto-animate-demo-load-children'
                                ),
                                fac.AntdButton(
                                    '追加子元素',
                                    id='auto-animate-demo-push-child'
                                ),
                                fac.AntdButton(
                                    '随机打乱顺序',
                                    id='auto-animate-demo-random-order'
                                ),
                                fac.AntdButton(
                                    '随机删除一项',
                                    id='auto-animate-demo-random-delete'
                                )
                            ]
                        ),

                        fuc.FefferyAutoAnimate(
                            id='auto-animate-demo-container'
                        ),

                        fac.AntdDivider(
                            '基础使用',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                fac.AntdText(
                                    'FefferyAutoAnimate',
                                    strong=True
                                ),
                                fac.AntdText(
                                    '可视作常规的div容器使用，其内部的有唯一id或key定义的子元素，在发生新增、删除、顺序变化等操作时会自动渲染动画效果'
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
fac.AntdSpace(
    [
        fac.AntdButton(
            '加载子元素',
            id='auto-animate-demo-load-children'
        ),
        fac.AntdButton(
            '追加子元素',
            id='auto-animate-demo-push-child'
        ),
        fac.AntdButton(
            '随机打乱顺序',
            id='auto-animate-demo-random-order'
        ),
        fac.AntdButton(
            '随机删除一项',
            id='auto-animate-demo-random-delete'
        )
    ]
),

fuc.FefferyAutoAnimate(
    id='auto-animate-demo-container'
)

...

@app.callback(
    Output('auto-animate-demo-container', 'children'),
    [Input('auto-animate-demo-load-children', 'nClicks'),
     Input('auto-animate-demo-push-child', 'nClicks'),
     Input('auto-animate-demo-random-order', 'nClicks')],
    Input('auto-animate-demo-random-delete', 'nClicks'),
    State('auto-animate-demo-container', 'children'),
    prevent_initial_call=True
)
def auto_animate_demo(load_children,
                      push_chjild,
                      random_order,
                      random_delete,
                      old_children):

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
                        'cursor': 'pointer'
                    },
                    shadow='hover-shadow'
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
                    'cursor': 'pointer'
                },
                shadow='hover-shadow'
            )
        ]

    elif dash.ctx.triggered_id == 'auto-animate-demo-random-order':
        random.shuffle(old_children)
        return old_children

    elif dash.ctx.triggered_id == 'auto-animate-demo-random-delete':
        delete_idx = random.randint(0, len(old_children)-1)

        return [
            child for i, child in enumerate(old_children)
            if i != delete_idx
        ]
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
            component_name='FefferyAutoAnimate'
        )
    ],
    style={
        'display': 'flex'
    }
)
