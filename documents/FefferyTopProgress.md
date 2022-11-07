**id：** *string*型

　　用于设置*当前组件的唯一id信息*

**children：**

　　用于设置*当前组件的嵌套子元素*，`FefferyTopProgress`会监听其`children`元素作为回调`Output`角色时的回调过程，从而在回调进行中时渲染页面顶部进度条动画

**style：** *dict*型

　　用于设置*当前组件的css样式*

**className：** *string*型

　　用于设置*当前组件的css类名*

**minimum：** *float*型，默认为`0.33`

　　用于设置*进度条开始显示时的起点百分比进度*，取值应在0~1之间

**easing：** *string*型，默认为`'ease'`

　　用于设置*进度条的动画效果css函数*

**speed：** *int*型，默认为`200`

　　用于设置*进度条每次递增一次的耗时时长*，单位毫秒

**showSpinner：** *bool*型，默认为`True`

　　用于设置*在进度条加载中时是否渲染右上角附带的圆圈加载动画*

**debug：** *bool*型，默认为`False`

　　用于设置是否开启*debug模式*，开启后，每当对应`FefferyTopProgress`组件加载动画渲染时，`浏览器开发者工具-console`中会打印触发本次加载动画的子节点**id**信息

**listenPropsMode：** *string*型，默认为`'default'`

　　用于设置特殊的*子节点监听过滤模式*，默认为`'default'`时，`FefferyTopProgress`的所有后代组件作为回调的`Output`进行回调过程时，都会触发加载动画；当设置为`'exclude'`时，会开启*排除过滤模式*，此时传入`includeProps`参数列表中的所有`'id.prop名称'`对应的后代组件处于回调时不会触发加载动画；当设置为`'include'`时，会开启*包含监听模式*，此时与`'exclude'`**恰恰相反**，只有传入到参数`includeProps`列表中的所有`'id.prop名称'`对应的后代组件的回调过程才会被`FefferyTopProgress`监听，具体使用同[fac.AntdSpin](https://fac.feffery.tech/AntdSpin)

**excludeProps：** *list*型

　　配合`listenPropsMode='exclude'`模式使用

**includeProps：** *list*型

　　配合`listenPropsMode='include'`模式使用