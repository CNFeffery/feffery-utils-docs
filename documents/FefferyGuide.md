**id：** *string*型

　　用于设置*当前组件的唯一id信息*

**style：** *dict*型

　　用于设置*当前组件的css样式*

**className：** *string*型

　　用于设置*当前组件的css类名*

**locale：** *string*型，默认为`'zh'`

　　用于设置*文案语言*，可选的有`'zh'`（中文）、`'en'`（英文）

**steps：** `list[dict]`型

　　用于*定义功能引导各步骤参数*，可用的键值对参数有：

- **selector：** *string*型，用于设置*可以用来定位当前步骤对应元素的css选择器*
- **targetPos：** *dict*型，当`selector`参数缺失时，用于*基于屏幕像素距离进行定位*，可用的键值对参数有：
  - **top：** *int*型，用于设置*锚点距离屏幕顶端的像素距离*
  - **left：** *int*型，用于设置*锚点距离屏幕左侧的像素距离*
  - **width：** *int*型，用于设置*锚点区域的像素宽度*
  - **height：** *int*型，用于设置*锚点区域的像素高度*
- **title：** *组件型*，用于设置*当前步骤弹窗的标题内容*
- **content：** *组件型*，用于设置*当前步骤弹窗的描述内容*
- **placement：** *string型*，默认为`'bottom'`，用于设置*当前步骤弹窗相对锚点的方位*，可选的有`'top'`、`'bottom'`、`'left'`、`'right'`、`'top-left'`、`'top-right'`、`'bottom-left'`、`'bottom-right'`、`'left-top'`、`'left-bottom'`、`'right-top'`、`'right-bottom'`
- **offset：** *dict*型，用于设置*当前步骤弹窗的像素偏移量*，可用的键值对参数有：
  - **x：** *int*型，用于设置*水平方向像素偏移量*
  - **y：** *int*型，用于设置*竖直方向像素偏移量*

**localKey：** *string*型

　　用于设置*本地缓存唯一标识key*，用于辅助浏览器端自动判断是否已完成过功能引导的展示，当应用中存在多个功能引导时，需保持`localKey`各自唯一

**closable：** *bool*型，默认为`True`

　　用于设置*是否允许用户选择跳过引导*

**modalClassName：** *string*型

　　用于设置*弹窗的css类*

**maskClassName：** *string*型

　　用于设置*蒙版层的css类*

**mask：** *bool*型，默认为`True`

　　用于设置*是否展示蒙版层*

**arrow：** *bool*型，默认为`True`

　　用于设置*步骤弹窗是否添加箭头*

**hotspot：** *bool*型，默认为`False`

　　用于设置*步骤弹窗是否添加额外的热点标识*

**stepText：** *string*型

　　用于设置*自定义步骤辅助信息展示内容对应的字符格式javascript函数*，默认为`"(stepIndex, stepCount) => { return '第${stepIndex}步，共${stepCount}步'; }"`

**nextText：** *string*型

　　用于设置*“下一步”按钮的文案信息*

**prevText：** *string*型

　　用于设置*“上一步”按钮的文案信息*

**showPreviousBtn：** *bool*型，默认为`True`

　　用于设置*是否显示“上一步”按钮*

**okText：** *string*型

　　用于设置*“确认”按钮的文案信息*

**step：** *int*型，默认为`0`

　　用于设置*初始化时展示的起始步骤*，设置为`-1`时则不显示