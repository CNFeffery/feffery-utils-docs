import uuid
from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc

import callbacks.FefferyGuide
from views.side_props import render_side_props_layout


def docs_content():

    return html.Div(
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
                                'title': 'FefferyGuide 功能引导'
                            }
                        ]
                    ),

                    fac.AntdDivider(isDashed=True),

                    fac.AntdParagraph(
                        [
                            fac.AntdText('　　用于按步骤引导用户认识应用中的不同功能。')
                        ]
                    ),

                    html.Div(
                        [
                            fac.AntdButton(
                                '触发功能引导',
                                id='guide-show',
                                type='primary'
                            ),

                            html.Div(
                                id='guide-demo'
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
import uuid

fac.AntdButton(
    '触发功能引导',
    id='guide-show',
    type='primary'
),

html.Div(
    id='guide-demo'
)

...

@app.callback(
    Output('guide-demo', 'children'),
    Input('guide-show', 'nClicks'),
    prevent_initial_call=True
)
def guide_demo(nClicks):

    return fuc.FefferyGuide(
        id='guide-demo-'+str(uuid.uuid4()),
        steps=[
            {
                'selector': '#guide-show',
                'title': '这是一个功能按钮',
                'content': '这里展示了本次功能引导的第一步内容。'
            },
            {
                'selector': '#github-entry',
                'title': '这是fuc的github仓库地址',
                'content': '这里展示了本次功能引导的第二步内容。'
            },
            {
                'selector': '#fold-side-menu',
                'title': '这是fuc官网的侧边菜单栏折叠按钮',
                'content': '这里展示了本次功能引导的第三步内容。',
                'placement': 'bottom-left'
            },
            {
                'targetPos': {
                    'top': 200,
                    'left': 500,
                    'width': 100,
                    'height': 50
                },
                'title': '这是自定义屏幕绝对位置锚点示例',
                'content': '这里展示了本次功能引导的第四步内容。'
            }
        ],
        localKey='guide-demo-'+str(uuid.uuid4()),
        closable=True
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
                component_name='FefferyGuide'
            )
        ],
        style={
            'display': 'flex'
        }
    )
