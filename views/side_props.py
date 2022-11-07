import uuid
from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_markdown_components as fmc


def render_side_props_layout(component_name: str):

    return html.Div(
        fac.AntdAffix(
            html.Div(
                [
                    fuc.FefferyScrollbars(
                        fac.AntdRibbon(
                            fmc.FefferyMarkdown(
                                markdownStr=(
                                    open(
                                        f'./documents/{component_name}.md',
                                        encoding='utf-8'
                                    )
                                    .read()
                                ),
                                style={
                                    'padding': '60px 25px 25px 25px'
                                }
                            ),
                            text=f'{component_name} API参数说明',
                            placement='start',
                            style={
                                'padding': '5px 8px 5px 15px',
                                'fontSize': '18px',
                                'height': '32px'
                            }
                        ),
                        style={
                            'height': '100%',
                            'background': 'white',
                            'boxShadow': '0px 0px 12px rgba(0, 0, 0, .12)'
                        }
                    ),
                    fac.AntdButton(
                        fac.AntdIcon(
                            id='fold-side-props-icon',
                            icon='antd-arrow-right'
                        ),
                        id='fold-side-props',
                        type='text',
                        shape='circle',
                        style={
                            'position': 'absolute',
                            'zIndex': 999,
                            'top': '10px',
                            'left': '-15px',
                            'boxShadow': '0 4px 10px 0 rgba(0, 0, 0, .1)',
                            'background': 'white'
                        }
                    )
                ],
                id='side-props',
                style={
                    'width': '600px',
                    'height': '100vh',
                    'borderLeft': '1px solid #f0f0f0',
                    'padding': '0 20px',
                    'position': 'relative',
                    'background': '#f2f3f5'
                }
            ),
            offsetTop=0
        ),
        # 强制重绘
        id=str(uuid.uuid4()),
        style={
            'flex': 'none'
        }
    )
