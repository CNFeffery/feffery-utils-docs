import re
import dash


class CustomDash(dash.Dash):

    def interpolate_index(self, **kwargs):
        # scripts = (
        #     kwargs.pop('scripts').replace(
        #         'https://unpkg.com/', 'https://npm.elemecdn.com/'
        #     )
        # )
        scripts = kwargs.pop('scripts')

        # 提取scripts部分符合条件的外部js资源
        external_scripts = re.findall(
            '(<script src="http.*?"></script>)',
            scripts
        )

        # 将原有的script标签内容替换为带备用地址错误切换的版本
        for external_script in external_scripts:
            # 排除fmc被onmicrosoft封禁的情况
            if 'markdown' not in external_script:
                scripts = scripts.replace(
                    external_script,
                    '''<script src="{}" onerror='this.remove(); let fallbackScript = document.createElement("script"); fallbackScript.src = "{}"; document.querySelector("head").prepend(fallbackScript);'></script>'''.format(
                        re.findall('"(.*?)"', external_script)[0]
                        .replace('https://unpkg.com/', 'https://npm.onmicrosoft.cn/'),
                        re.findall('"(.*?)"', external_script)[0]
                    )
                )

        scripts = '''<script>
window.onerror = async function(message, source, lineno, colno, error) {
    if (message.includes('is not defined') !== -1) {
        await waitForModules();
    }
}

async function waitForModules() {
    const requiredModules = [
        'DashRenderer',
        'dash_html_components',
        'dash_core_components',
        'feffery_antd_components',
        'feffery_utils_components',
        'feffery_markdown_components'
    ];

    while (!areModulesDefined(requiredModules)) {
        await delay(100); // 延迟100毫秒
    }

    // 变量已定义，触发事件
    var renderer = new DashRenderer();
}

function areModulesDefined(modules) {
    return modules.every(module => window[module]);
}

function delay(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}
</script>
''' + scripts

        return super(CustomDash, self).interpolate_index(scripts=scripts, **kwargs)


app = CustomDash(
    __name__,
    suppress_callback_exceptions=True,
    update_title=None,
    serve_locally=False,
    extra_hot_reload_paths=[
        './documents'
    ],
    compress=True,
    assets_ignore='dark.css'
)

app.title = 'feffery-utils-components在线文档'

server = app.server
