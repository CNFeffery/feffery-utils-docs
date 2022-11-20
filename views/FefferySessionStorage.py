from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc

import callbacks.FefferySessionStorage
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
                            'title': 'FefferySessionStorage 状态同步'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText(
                            '　　既可直接设置data参数进行状态设置，又可监听其他位置发生的sessionStorage.setItem()事件并同步回data。')
                    ]
                ),

                html.Div(
                    [

                        fac.AntdButton(
                            '执行示例js代码',
                            id='session-storage-demo-input'
                        ),

                        fuc.FefferyExecuteJs(
                            id='session-storage-demo-trigger'
                        ),

                        fuc.FefferySessionStorage(id='session-storage-demo'),

                        html.Pre(id='session-storage-demo-output'),

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
                                codeString="""
fac.AntdButton(
    '执行示例js代码',
    id='session-storage-demo-input'
),

fuc.FefferyExecuteJs(
    id='session-storage-demo-trigger'
),

fuc.FefferySessionStorage(id='session-storage-demo'),

html.Pre(id='session-storage-demo-output')

...

@app.callback(
    Output('session-storage-demo-trigger', 'jsString'),
    Input('session-storage-demo-input', 'nClicks'),
    prevent_initial_call=True
)
def trigger_session_storage_set(nClicks):

    return '''sessionStorage.setItem('session-storage-demo', JSON.stringify({'点击次数': % s, '当前时间': new Date(Date.now())}))''' % str(nClicks)


@app.callback(
    Output('session-storage-demo-output', 'children'),
    Input('session-storage-demo', 'data'),
    prevent_initial_call=True
)
def session_storage_demo(data):

    return json.dumps(
        data,
        ensure_ascii=False,
        indent=4
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
            component_name='FefferySessionStorage'
        )
    ],
    style={
        'display': 'flex'
    }
)
