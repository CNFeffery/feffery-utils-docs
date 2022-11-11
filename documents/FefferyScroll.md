**id：** *string*型

　　用于设置*当前组件的唯一id信息*

**scrollMode：** *string*型，默认为`'to-top'`

　　必填，用于设置*滚动动作的模式*，可选的有`'to-top'`（滚至顶部）、`'to-bottom'`（滚至底部）、`'top-offset'`（滚至距离顶端若干像素位置）、`'relative-offset'`（相对当前位置滚动若干像素）、`'target'`（滚动至目标元素位置）

**executeScroll：** *bool*型，默认为`False`

　　用于*触发新的滚动动作*，每次更新为`True`后都会基于其他参数进行新的滚动动作，且在滚动动作完成后自动重置为`false`

**scrollTopOffset：** *int*型

　　当`scrollMode='top-offset'`时，用于设置*滚动终点距离页面顶端的像素距离*

**scrollRelativeOffset：** *int*型

　　当`scrollMode='relative-offset'`时，用于设置*相对当前位置向下进行滚动的距离*，当设置为负数时则会向上滚动

**scrollTargetId：** *string*型

　　当`scrollMode='target'`时，用于设置*滚动目标元素的id*

**duration：** *int*型，默认为`500`

　　用于设置*滚动过程动画耗时*，单位：毫秒

**smooth：** *bool*或*string*型，默认为`True`

　	用于配置*滚动过程动画平滑模式*，亦可设置为特定的动画函数，可选的有`'linear'`、`'easeInQuad'`、`'easeOutQuad'`、`'easeInOutQuad'`、`'easeInCubic'`、`'easeOutCubic'`、`'easeInOutCubic'`、`'easeInQuart'`、`'easeOutQuart'`、`'easeInOutQuart'`、`'easeInQuint'`、`'easeOutQuint'`、`'easeInOutQuint'`

**delay：** *int*型，默认为`0`

　　用于设置*滚动动作执行前的延时时长*，单位：毫秒

**containerId：** *string*型

　　当需要在局部容器内执行滚动动作时，需要将对应局部容器的`id`传递给此参数

**offset：** *int*型

　　用于设置*滚动过程的额外偏移像素距离*