import uuid
import feffery_utils_components as fuc
from dash.dependencies import Input, Output

from server import app


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
