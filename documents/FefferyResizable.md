**id：** *string*型

　　用于设置*当前组件的唯一id信息*

**style：** *dict*型

　　用于设置*当前组件的css样式*

**className：** *string*型

　　用于设置*当前组件的css类名*

**children：** *组件型*

　　用于传入*嵌套的子元素*

**defaultSize：** *dict*型

　　用于*设置当前尺寸调整组件初始化时的宽度、高度*，可用的键值对参数有：

- **width：** *int*或*string*型，用于*设置初始化宽度*，可传入如`300`、`'300px'`、`'50%'`、`'50vw'`等形式的输入
- **height：** *int*或*string*型，用于*设置初始化高度*，可传入如`300`、`'300px'`、`'50%'`、`'50vh'`等形式的输入

**minWidth：** *int*或*string*型，默认为`10`

　　用于*设置当前尺寸调整组件的最小宽度*

**minHeight：** *int*或*string*型，默认为`10`

　　用于*设置当前尺寸调整组件的最小高度*

**maxWidth：** *int*或*string*型，默认为`10`

　　用于*设置当前尺寸调整组件的最大宽度*

**maxHeight：** *int*或*string*型，默认为`10`

　　用于*设置当前尺寸调整组件的最大高度*

**direction：** `list[string]`型

　　用于*设置允许进行尺寸调整的方向*，可选的有`'top'`、`'right'`、`'bottom'`、`'left'`、`'topRight'`、`'bottomRight'`、`'bottomLeft'`、`'topLeft'`，默认允许所有方向

**grid：** `list[int]`型，默认为`[1, 1]`

　　用于*分别设置尺寸调整在水平、竖直方向上的最小调整像素步长*

**bounds：** *string*型，默认为`'window'`

　　用于*设置当前尺寸调整组件的限制范围*，可选的有`'parent'`（父元素内）、`'window'`（整体页面内）

**handleStyles：** *dict*型

　　用于*分别设置各个方向上尺寸调整拖拽控件的css样式*

**handleClassNames：** *dict*型

　　用于*分别设置各个方向上尺寸调整拖拽控件的css类*