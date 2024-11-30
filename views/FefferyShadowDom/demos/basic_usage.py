from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdSpace(
            [
                fuc.FefferyShadowDom(
                    [
                        fuc.FefferyStyle(
                            rawStyle="""
.style-demo {
    width: 300px;
    height: 150px;
    background: linear-gradient(135deg,#fce38a,#f38181);
    border-radius: 5px;
    display: flex;
    justify-content: center;
    align-items: center;
}
"""
                        ),
                        html.Div('节点1', className='style-demo'),
                    ]
                ),
                fuc.FefferyShadowDom(
                    [
                        fuc.FefferyStyle(
                            rawStyle="""
.style-demo {
    width: 300px;
    height: 150px;
    background: linear-gradient(135deg,#17ead9,#6078ea);
    border-radius: 5px;
    display: flex;
    justify-content: center;
    align-items: center;
}
"""
                        ),
                        html.Div('节点2', className='style-demo'),
                    ]
                ),
            ],
            direction='vertical',
        )
    ]

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': '''
fuc.FefferyShadowDom(
    [
        fuc.FefferyStyle(
            rawStyle="""
.style-demo {
    width: 300px;
    height: 150px;
    background: linear-gradient(135deg,#fce38a,#f38181);
    border-radius: 5px;
    display: flex;
    justify-content: center;
    align-items: center;
}
"""
        ),
        html.Div('节点1', className='style-demo'),
    ]
),
fuc.FefferyShadowDom(
    [
        fuc.FefferyStyle(
            rawStyle="""
.style-demo {
    width: 300px;
    height: 150px;
    background: linear-gradient(135deg,#17ead9,#6078ea);
    border-radius: 5px;
    display: flex;
    justify-content: center;
    align-items: center;
}
"""
                    ),
                    html.Div('节点2', className='style-demo'),
                ]
            ),
        ],
        direction='vertical',
    )
]
'''
        }
    ]
