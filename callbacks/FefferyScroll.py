import dash
import feffery_utils_components as fuc
from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('scroll-demo-output', 'children'),
    [Input('scroll-to-top-demo', 'nClicks'),
     Input('scroll-to-bottom-demo', 'nClicks'),
     Input('scroll-top-offset-demo', 'nClicks'),
     Input('scroll-relative-offset-demo', 'nClicks'),
     Input('scroll-target-demo', 'nClicks')],
    prevent_initial_call=True
)
def scroll_demo(*args):

    # 基于dash的上下文功能获知当前回调由谁触发
    trigger_id = dash.ctx.triggered_id

    if trigger_id == 'scroll-to-top-demo':
        return fuc.FefferyScroll(
            executeScroll=True,
            scrollMode='to-top'
        )

    elif trigger_id == 'scroll-to-bottom-demo':
        return fuc.FefferyScroll(
            executeScroll=True,
            scrollMode='to-bottom'
        )

    elif trigger_id == 'scroll-top-offset-demo':
        return fuc.FefferyScroll(
            executeScroll=True,
            scrollMode='top-offset',
            scrollTopOffset=800
        )

    elif trigger_id == 'scroll-relative-offset-demo':
        return fuc.FefferyScroll(
            executeScroll=True,
            scrollMode='relative-offset',
            scrollRelativeOffset=300
        )

    elif trigger_id == 'scroll-target-demo':
        return fuc.FefferyScroll(
            executeScroll=True,
            scrollMode='target',
            scrollTargetId='scroll-target-element'
        )
