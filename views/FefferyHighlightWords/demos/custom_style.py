from dash import html
import feffery_utils_components as fuc
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fuc.FefferyHighlightWords(
            textToHighlight="""　　从来就没有什么救世主，
也不靠神仙皇帝。
要创造人类的幸福，
全靠我们自己。
我们要夺回劳动果实，
让思想冲破牢笼。
快把那炉火烧得通红，
趁热打铁才能成功！
这是最后的斗争，
团结起来，到明天，
英特纳雄耐尔就一定要实现。""",
            searchWords=['我们', '团结'],
            highlightStyle={
                'background': 'linear-gradient(90deg,#ff75c3,#ffa647,#ffe83f,#9fff5b,#70e2ff,#cd93ff)',
                'padding': 0,
                'color': 'white',
            },
        ),
        html.Br(),
        fuc.FefferyHighlightWords(
            textToHighlight="""　　从来就没有什么救世主，
也不靠神仙皇帝。
要创造人类的幸福，
全靠我们自己。
我们要夺回劳动果实，
让思想冲破牢笼。
快把那炉火烧得通红，
趁热打铁才能成功！
这是最后的斗争，
团结起来，到明天，
英特纳雄耐尔就一定要实现。""",
            searchWords=['我们', '团结'],
            highlightStyle={
                'fontWeight': 'bold',
                'backgroundColor': 'transparent',
                'padding': 0,
                'color': 'red',
            },
            unhighlightStyle={'color': '#bfbfbf'},
        ),
    ]

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': '''
[
    fuc.FefferyHighlightWords(
        textToHighlight="""　　从来就没有什么救世主，
也不靠神仙皇帝。
要创造人类的幸福，
全靠我们自己。
我们要夺回劳动果实，
让思想冲破牢笼。
快把那炉火烧得通红，
趁热打铁才能成功！
这是最后的斗争，
团结起来，到明天，
英特纳雄耐尔就一定要实现。""",
        searchWords=['我们', '团结'],
        highlightStyle={
            'background': 'linear-gradient(90deg,#ff75c3,#ffa647,#ffe83f,#9fff5b,#70e2ff,#cd93ff)',
            'padding': 0,
            'color': 'white',
        },
    ),
    html.Br(),
    fuc.FefferyHighlightWords(
        textToHighlight="""　　从来就没有什么救世主，
也不靠神仙皇帝。
要创造人类的幸福，
全靠我们自己。
我们要夺回劳动果实，
让思想冲破牢笼。
快把那炉火烧得通红，
趁热打铁才能成功！
这是最后的斗争，
团结起来，到明天，
英特纳雄耐尔就一定要实现。""",
        searchWords=['我们', '团结'],
        highlightStyle={
            'fontWeight': 'bold',
            'backgroundColor': 'transparent',
            'padding': 0,
            'color': 'red',
        },
        unhighlightStyle={'color': '#bfbfbf'},
    ),
]
'''
        }
    ]
