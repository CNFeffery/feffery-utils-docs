import dash

# 导入Dash Hooks
from dash_change_cdn_plugin import setup_change_cdn_plugin
from dash_console_filter_plugin import setup_console_filter_plugin

from config import AppConfig

# 启用相关Dash Hooks插件

# 更换默认CDN到npmmirror
setup_change_cdn_plugin()
# 屏蔽浏览器控制台无关报错信息
setup_console_filter_plugin(keywords=['Warning:'])

app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    update_title=None,
    serve_locally=False,
    extra_hot_reload_paths=['./changelogs', './public'],
    compress=True,
    meta_tags=[
        # 移动端显示优化
        {
            'name': 'viewport',
            'content': 'width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0',
        }
    ],
)

app.title = AppConfig.title

server = app.server
