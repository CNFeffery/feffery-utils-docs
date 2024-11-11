import json
import feffery_utils_components as fuc

# 国际化
from i18n import translator


class DeployConfig:
    """
    应用部署相关参数
    """

    # CDN模块名列表
    cdn_modules = [
        'DashRenderer',
        'dash_html_components',
        'dash_core_components',
        'feffery_antd_components',
        'feffery_utils_components',
        'feffery_markdown_components',
    ]


class AppConfig:
    """
    应用常规参数配置
    """

    # 应用默认标签页标题
    title = 'feffery-utils-components在线文档'

    # 应用logo地址
    logo_path = 'imgs/fuc-logo.svg'

    # 页首标题
    page_header_title = 'feffery-utils-components'

    # 当前组件版本
    library_version = fuc.__version__

    # 组件仓库地址
    library_repo = 'https://github.com/CNFeffery/feffery-utils-components'

    # 文档仓库地址
    doc_library_repo = 'https://github.com/CNFeffery/feffery-utils-docs'

    # 文档Gitee仓库地址
    doc_gitee_library_repo = 'https://gitee.com/cnfeffery/feffery-utils-docs'

    # 文档仓库分支名称
    doc_library_branch = 'main'

    # 当前应用是否为正式发布模式
    is_release = True

    # 文档贡献者信息
    doc_contributors = json.load(open('./public/contributors.json'))

    # 项目国际化指南地址
    i18n_guide_link = (
        'https://github.com/CNFeffery/feffery-utils-docs/issues/166'
    )

    @staticmethod
    def side_menu_items() -> list:
        # 侧边菜单栏数据结构
        return [
            {
                'component': 'ItemGroup',
                'props': {'key': '快速入门', 'title': translator.t('快速入门')},
                'children': [
                    {
                        'component': 'Item',
                        'props': {
                            'key': '/what-is-fuc',
                            'name': '/what-is-fuc',
                            'href': '/what-is-fuc',
                            'title': translator.t('fuc是什么'),
                        },
                    }
                ],
            },
            {'component': 'Divider', 'props': {'dashed': True}},
            {
                'component': 'ItemGroup',
                'props': {'key': '组件介绍', 'title': translator.t('组件介绍')},
                'children': [
                    {
                        'component': 'SubMenu',
                        'props': {'key': '通用', 'title': translator.t('通用')},
                        'children': [
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyBurger',
                                    'name': '/FefferyBurger',
                                    'title': translator.t(
                                        'FefferyBurger 动态菜单图标'
                                    ),
                                    'href': '/FefferyBurger',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyDownload',
                                    'name': '/FefferyDownload',
                                    'title': translator.t(
                                        'FefferyDownload 文件下载'
                                    ),
                                    'href': '/FefferyDownload',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyFancyButton',
                                    'name': '/FefferyFancyButton',
                                    'title': translator.t(
                                        'FefferyFancyButton 美观按钮'
                                    ),
                                    'href': '/FefferyFancyButton',
                                },
                            },
                        ],
                    },
                    {
                        'component': 'SubMenu',
                        'props': {
                            'key': '颜色选择',
                            'title': translator.t('颜色选择'),
                        },
                        'children': [
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyBlockColorPicker',
                                    'name': '/FefferyBlockColorPicker',
                                    'title': translator.t(
                                        'FefferyBlockColorPicker Block风格色彩选择器'
                                    ),
                                    'href': '/FefferyBlockColorPicker',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyCircleColorPicker',
                                    'name': '/FefferyCircleColorPicker',
                                    'title': translator.t(
                                        'FefferyCircleColorPicker Circle风格色彩选择器'
                                    ),
                                    'href': '/FefferyCircleColorPicker',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyEyeDropper',
                                    'name': '/FefferyEyeDropper',
                                    'title': translator.t(
                                        'FefferyEyeDropper 色彩拾取'
                                    ),
                                    'href': '/FefferyEyeDropper',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyGithubColorPicker',
                                    'name': '/FefferyGithubColorPicker',
                                    'title': translator.t(
                                        'FefferyGithubColorPicker Github风格色彩选择器'
                                    ),
                                    'href': '/FefferyGithubColorPicker',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyHexColorPicker',
                                    'name': '/FefferyHexColorPicker',
                                    'title': translator.t(
                                        'FefferyHexColorPicker 16进制色彩选择器'
                                    ),
                                    'href': '/FefferyHexColorPicker',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyRgbColorPicker',
                                    'name': '/FefferyRgbColorPicker',
                                    'title': translator.t(
                                        'FefferyRgbColorPicker rgb色彩选择器'
                                    ),
                                    'href': '/FefferyRgbColorPicker',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyTwitterColorPicker',
                                    'name': '/FefferyTwitterColorPicker',
                                    'title': translator.t(
                                        'FefferyTwitterColorPicker Twitter风格色彩选择器'
                                    ),
                                    'href': '/FefferyTwitterColorPicker',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyWheelColorPicker',
                                    'name': '/FefferyWheelColorPicker',
                                    'title': translator.t(
                                        'FefferyWheelColorPicker Wheel风格色彩选择器'
                                    ),
                                    'href': '/FefferyWheelColorPicker',
                                },
                            },
                        ],
                    },
                    {
                        'component': 'SubMenu',
                        'props': {
                            'key': '动效',
                            'title': translator.t('动效'),
                        },
                        'children': [
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyAutoAnimate',
                                    'name': '/FefferyAutoAnimate',
                                    'title': translator.t(
                                        'FefferyAutoAnimate 自动动画'
                                    ),
                                    'href': '/FefferyAutoAnimate',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyMotion',
                                    'name': '/FefferyMotion',
                                    'title': translator.t(
                                        'FefferyMotion 动画编排'
                                    ),
                                    'href': '/FefferyMotion',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyBirdsBackground',
                                    'name': '/FefferyBirdsBackground',
                                    'title': translator.t(
                                        'FefferyBirdsBackground 3D-Birds背景'
                                    ),
                                    'href': '/FefferyBirdsBackground',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyCellsBackground',
                                    'name': '/FefferyCellsBackground',
                                    'title': translator.t(
                                        'FefferyCellsBackground 3D-Cells背景'
                                    ),
                                    'href': '/FefferyCellsBackground',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyCloudsBackground',
                                    'name': '/FefferyCloudsBackground',
                                    'title': translator.t(
                                        'FefferyCloudsBackground 3D-Clouds背景'
                                    ),
                                    'href': '/FefferyCloudsBackground',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyCloudsTwoBackground',
                                    'name': '/FefferyCloudsTwoBackground',
                                    'title': translator.t(
                                        'FefferyCloudsTwoBackground 3D-CloudsTwo背景'
                                    ),
                                    'href': '/FefferyCloudsTwoBackground',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyFogBackground',
                                    'name': '/FefferyFogBackground',
                                    'title': translator.t(
                                        'FefferyFogBackground 3D-Fog背景'
                                    ),
                                    'href': '/FefferyFogBackground',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyGlobeBackground',
                                    'name': '/FefferyGlobeBackground',
                                    'title': translator.t(
                                        'FefferyGlobeBackground 3D-Globe背景'
                                    ),
                                    'href': '/FefferyGlobeBackground',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyHaloBackground',
                                    'name': '/FefferyHaloBackground',
                                    'title': translator.t(
                                        'FefferyHaloBackground 3D-Halo背景'
                                    ),
                                    'href': '/FefferyHaloBackground',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyNetBackground',
                                    'name': '/FefferyNetBackground',
                                    'title': translator.t(
                                        'FefferyNetBackground 3D-Net背景'
                                    ),
                                    'href': '/FefferyNetBackground',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyRingsBackground',
                                    'name': '/FefferyRingsBackground',
                                    'title': translator.t(
                                        'FefferyRingsBackground 3D-Rings背景'
                                    ),
                                    'href': '/FefferyRingsBackground',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyTopologyBackground',
                                    'name': '/FefferyTopologyBackground',
                                    'title': translator.t(
                                        'FefferyTopologyBackground 3D-Topology背景'
                                    ),
                                    'href': '/FefferyTopologyBackground',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyTrunkBackground',
                                    'name': '/FefferyTrunkBackground',
                                    'title': translator.t(
                                        'FefferyTrunkBackground 3D-Trunk背景'
                                    ),
                                    'href': '/FefferyTrunkBackground',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyWavesBackground',
                                    'name': '/FefferyWavesBackground',
                                    'title': translator.t(
                                        'FefferyWavesBackground 3D-Waves背景'
                                    ),
                                    'href': '/FefferyWavesBackground',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/FefferyTiltHover',
                                    'name': '/FefferyTiltHover',
                                    'title': translator.t(
                                        'FefferyTiltHover 倾斜悬浮'
                                    ),
                                    'href': '/FefferyTiltHover',
                                },
                            },
                        ],
                    },
                ],
            },
            # {
            #     'component': 'ItemGroup',
            #     'props': {'key': '更新日志', 'title': translator.t('更新日志')},
            #     'children': [
            #         {
            #             'component': 'SubMenu',
            #             'props': {
            #                 'key': '0.2.x版本',
            #                 'title': '0.2.x',
            #             },
            #             'children': [
            #                 {
            #                     'component': 'Item',
            #                     'props': {
            #                         'key': '/changelog-' + version,
            #                         'name': '/changelog-' + version,
            #                         'title': version,
            #                         'href': '/changelog-' + version,
            #                     },
            #                 }
            #                 for version in []
            #             ],
            #         }
            #     ],
            # },
        ]

    # 侧边菜单栏key值 -> 展开项节点key值数组
    side_menu_expand_keys = {
        '/FefferyBurger': ['通用'],
        '/FefferyDownload': ['通用'],
        '/FefferyFancyButton': ['通用'],
        '/FefferyBlockColorPicker': ['颜色选择'],
        '/FefferyCircleColorPicker': ['颜色选择'],
        '/FefferyEyeDropper': ['颜色选择'],
        '/FefferyGithubColorPicker': ['颜色选择'],
        '/FefferyHexColorPicker': ['颜色选择'],
        '/FefferyRgbColorPicker': ['颜色选择'],
        '/FefferyTwitterColorPicker': ['颜色选择'],
        '/FefferyWheelColorPicker': ['颜色选择'],
        '/FefferyAutoAnimate': ['动效'],
        '/FefferyMotion': ['动效'],
        '/FefferyBirdsBackground': ['动效'],
        '/FefferyCellsBackground': ['动效'],
        '/FefferyCloudsBackground': ['动效'],
        '/FefferyCloudsTwoBackground': ['动效'],
        '/FefferyFogBackground': ['动效'],
        '/FefferyGlobeBackground': ['动效'],
        '/FefferyHaloBackground': ['动效'],
        '/FefferyNetBackground': ['动效'],
        '/FefferyRingsBackground': ['动效'],
        '/FefferyTopologyBackground': ['动效'],
        '/FefferyTrunkBackground': ['动效'],
        '/FefferyWavesBackground': ['动效'],
        '/FefferyTiltHover': ['动效'],
    }
