**id：** *string*型

　　用于设置*当前组件的唯一id信息*

**style：** *dict*型

　　用于设置*当前组件的css样式*

**className：** *string*型

　　用于设置*当前组件的css类名*

**data：** *dict*型，必填

　　用于*设置要展示的json数据*

**theme：** *string*型，默认为`'summerfruit:inverted'`

　　用于*设置样式风格*，可选的有`'apathy'`、`'apathy:inverted'`、`'ashes'`、`'bespin'`、`'brewer'`、`'bright:inverted'`、`'bright'`、`'chalk'`、`'codeschool'`、`'colors'`、`'eighties'`、`'embers'`、`'flat'`、`'google'`、`'grayscale'`、`'grayscale:inverted'`、`'greenscreen'`、`'harmonic'`、`'hopscotch'`、`'isotope'`、`'marrakesh'`、`'mocha'`、`'monokai'`、`'ocean'`、`'paraiso'`、`'pop'`、`'railscasts'`、`'shapeshifter'`、`'shapeshifter:inverted'`、`'solarized'`、`'summerfruit'`、`'summerfruit:inverted'`、`'threezerotwofour'`、`'tomorrow'`、`'tube'`、`'twilight'`、`'rjv-default'`

**indent：** *int*型，默认为`4`

　　用于*设置标准缩进空格数量*

**iconStyle：** *string*型，默认为`'circle'`

　　用于*设置各个操作按钮的形状风格*，可选的有`'circle'`、`'triangle'`、`'square'`

**collapsed：** *bool*或*int*型，默认为`False`

　　用于*设置节点的折叠情况*，当传入*bool*型时用于决定是否折叠全部节点，当传入*int*型输入时，用于设置折叠节点深度范围，深度超过此范围的节点会被自动折叠

**collapseStringsAfterLength：** *bool*或*int*型，默认为`False`

　　用于*设置针对超长字符串的省略展示*，当传入`False`时不省略，当传入*int*型输入时，用于设置字符串省略长度范围，字符长度超过此范围的部分字符串内容将会被省略展示

**groupArraysAfterLength：** *int*型，默认为`100`

　　用于*针对数组元素进行分组省略展示时*，每个组内的最大元素数量

**enableClipboard：** *bool*型，默认为`True`

　　用于*设置是否开启节点复制功能*

**displayObjectSize：** *bool*型，默认为`True`

　　用于*设置是否额外展示节点元素大小信息*

**displayDataTypes：** *bool*型，默认为`True`

　　用于*设置是否展示节点数据类型*

**editable：** *bool*型，默认为`False`

　　用于*设置是否开启数据编辑功能*

**addible：** *bool*型，默认为`False`

　　用于*设置是否开启数据追加功能*

**deletable：** *bool*型，默认为`False`

　　用于*设置是否开启数据删除功能*

**sortKeys：** *bool*型，默认为`False`

　　用于*设置是否根据键对节点进行排序*

**quotesOnKeys：** *bool*型，默认为`True`

　　用于*设置是否为键添加引号*

**displayArrayKey：** *bool*型，默认为`True`

　　用于*设置是否为数组元素展示下标*