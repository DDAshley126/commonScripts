import dash_bootstrap_components as dbc
from dash import html
from typing import Union
from dash.development.base_component import Component

_Component = Union[Component, str, list, int, float]


def simple_card_plot(
        title: _Component = None,
        titleStyle: dict = None,
        titleClassName: str = None,
        title_id: Union[str, dict] = None,
        content: _Component = None,
        contentStyle: dict = None,
        contentClassName: str = None,
        content_id: Union[str, dict] = None,
        tooltip: _Component = None,
        tooltipStyle: dict = None,
        tooltip_id: Union[str, dict] = None,
        footer: _Component = None,
        footerStyle: dict = None,
        footerClassName: str = None,
        footer_id: Union[str, dict] = None,
        frameStyle: dict = None,
        frameClassName: str = None,
        frame_id: str = None,
) -> Component:
    """
    简易卡片模板，包含标题、中间内容和脚注（环比）
    :param title: 卡片标题，默认为None
    :param titleStyle: 卡片标题样式，默认为None
    :param titleClassName: 卡片标题类名，默认为None
    :param title_id: 卡片标题id，默认为None
    :param content: 卡片中间内容，默认为None
    :param contentStyle: 卡片中间内容样式，默认为None
    :param contentClassName: 卡片中间内容类名，默认为None
    :param content_id: 卡片中间内容id，默认为None
    :param tooltip: 提示框内容，默认为None
    :param tooltipStyle: 提示框内容样式，默认为None
    :param tooltip_id: 提示框内容id，默认为None
    :param footer: 脚注内容，默认为None
    :param footerStyle: 脚注内容样式，默认为None
    :param footerClassName: 脚注内容类名，默认为None
    :param footer_id: 脚注内容id，默认为None
    :param frameStyle: 外框样式，默认为None
    :param frameClassName: 外框类名，默认为None
    :param frame_id: 外框id，默认为None
    :return: 返回卡片模板
    """
    return dbc.Col(
        children=[
            html.Div(
                [
                    dbc.Row([
                        dbc.Col([
                            html.Div(
                                children=title,
                                style={**{'font-size': '18px', 'font-weight': 'bold', 'family': 'sans ser-if', 'color': 'black'}, **(titleStyle or {})},
                                className=titleClassName,
                                **{'id': title_id if title_id is not None else {}}
                            ),
                            html.I(className='bi bi-info-circle', id='info-circle'),
                            dbc.Tooltip(
                                children=tooltip,
                                target='info-circle',
                                style=(tooltipStyle or {}),
                                **{'id': tooltip_id if tooltip_id is not None else {}}
                            ),
                        ], style={'display': 'flex', 'justify-content': 'space-between'}),
                    ]),
                    html.Div(
                        children=content,
                        style={**{'text-align': 'left', 'font-size': '20px', 'font-weight': 'bold', 'color': '#4B63AD'}, **(contentStyle or {})},
                        className=contentClassName,
                        **{'id': content_id if content_id is not None else {}}
                    ),
                    html.Hr(style={'margin-top': 0, 'margin-bottom': 0}),
                    html.Div(
                        children=footer,
                        style={
                            **{
                                'height': 32,
                                'paddingTop': 9,
                            },
                            **(footerStyle or {})
                        },
                        **{'id': footer_id if footer_id is not None else {}},
                        className=footerClassName
                    ),
                ]
            )
        ],
        style={
            **{
                'padding': '20px 20px 8px',
                'box-shadow': '2px 2px 5px #dbdbdb',
                'border-style': 'solid',
                'border-width': '1px',
                'border-color': 'lightgrey',
                'border-radius': '10px',
                'text-align': 'left',
                'background-color': 'white',
            },
            **(frameStyle or {})
        },
        className=frameClassName,
        **{'id': frame_id if frame_id is not None else {}}
    )
