from dash import html, dcc
import feffery_antd_components as fac

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
                            'title': 'FefferyGridItem 可拖拽网格项'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText(
                            '　　用于定义FefferyGrid内每一个可拖拽的网格项子元素，具体使用请移步'),
                        dcc.Link(
                            'FefferyGrid文档页',
                            href='/FefferyGrid'
                        ),
                        fac.AntdText('。')
                    ]
                ),

                html.Div(style={'height': '100px'})
            ],
            style={
                'flex': 'auto',
                'padding': '25px'
            }
        ),
        # 侧边参数栏
        render_side_props_layout(
            component_name='FefferyGridItem'
        )
    ],
    style={
        'display': 'flex'
    }
)
