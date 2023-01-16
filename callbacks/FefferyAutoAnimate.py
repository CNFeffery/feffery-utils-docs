import dash
import uuid
import random
import feffery_utils_components as fuc
from dash.dependencies import Input, Output, State

from server import app


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
