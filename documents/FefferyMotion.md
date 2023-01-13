> 注意：
>
> 　　针对`FefferyMotion`中的可用于定义css样式的参数`style`、`initial`、`animate`、`exit`、`whileHover`、`whileTap`、`whileInView`，除了标准的css属性可用外，还可设置以下**快捷**属性：
>
> - **位置移动类：** *x、y、z、translateX、translateY、translateZ*
> - **缩放类：** *scale、scaleX、scaleY*
> - **旋转类：** *rotate、rotateX、rotateY、rotateZ*
> - **倾斜类：** *skew、skewX、skewY*
> - **透视类：** *transformPerspective*
> - **元素变形原点：** *originX、originY、originZ*

**id：** *string*型

　　用于设置*当前组件的唯一id信息*

**style：** *dict*型

　　用于设置*当前组件的css样式*

**className：** *string*型

　　用于设置*当前组件的css类名*

**children：** *组件型*

　　用于传入*嵌套的子元素*

**initial：** *dict*、*bool*或*string*型

　　用于*为当前组件设置初始化时额外施加的样式*，其中：

- 当传入*dict*型时，用于*设置样式字典*
- 当传入`False`时，会*禁止当前组件初始化时的动画变换*
- 当传入*string*型时，可套用`variants`参数中定义的具有别名的样式组

**animate：** *dict*或*string*型

　　用于*为当前组件设置初始化完成后进行动画过渡的目标样式*，其中：

- 当传入*dict*型时，用于*设置样式字典*
- 当传入*string*型时，可套用`variants`参数中定义的具有别名的样式组

**exit：** *dict*或*string*型

　　用于*为当前组件设置从页面卸载时进行动画过渡的目标样式*，其中：

- 当传入*dict*型时，用于*设置样式字典*
- 当传入*string*型时，可套用`variants`参数中定义的具有别名的样式组

**whileHover：** *dict*或*string*型

　　用于*为当前组件设置鼠标悬停时进行动画过渡的目标样式*，其中：

- 当传入*dict*型时，用于*设置样式字典*
- 当传入*string*型时，可套用`variants`参数中定义的具有别名的样式组

**whileTap：** *dict*或*string*型

　　用于*为当前组件设置鼠标点按时进行动画过渡的目标样式*，其中：

- 当传入*dict*型时，用于*设置样式字典*
- 当传入*string*型时，可套用`variants`参数中定义的具有别名的样式组

**transition：** *dict*型

　　用于*配置过渡动画相关参数*，可用的键值对参数有：

- **delay：** *int*或*float*型，默认为`0`，用于*设置过渡动画开始前的延时*，单位：秒
- **repeat：** *int*或*string*型，用于*设置过渡动画的重复次数*，特殊的，传入`'infinity'`代表无限循环
- **repeatType：** *string*型，用于*设置过渡动画的重复方式*，可选的有`'loop'`、`'reverse'`、`'mirror'`
- **repeatDelay：** *int*或*float*型，用于*设置每次过渡动画重复前的延时*，单位：秒
- **type：** *string*型，默认为`'tween'`，用于*设置动画计算算法*，可选的有`'tween'`（常规补间算法）、`'spring'`（弹簧物理算法）
- **duration：** *int*或*float*型，用于*设置动化过渡周期时长*，单位：秒
- **ease：** *string*型，当`transition.type='tween'`时，用于*设置过渡动画函数*，可选的有`'linear'`、`'easeIn'`、`'easeOut'`、`'easeInOut'`、`'circIn'`、`'circOut'`、`'circInOut'`、`'backIn'`、`'backOut'`、`'backInOut'`、`'anticipate'`
- **times：** `list[int]`或`list[float]`型，用于以`duration`为1单位，一一对应设置分段动画中每段的耗时累积分布，单位：秒

**whileInView：** *dict*或*string*型

　　用于*为当前组件设置进入视口后进行动画过渡的目标样式*，其中：

- 当传入*dict*型时，用于*设置样式字典*
- 当传入*string*型时，可套用`variants`参数中定义的具有别名的样式组

**viewport：** *dict*型

　　用于*配置视口检测相关参数*，可用的键值对参数有：

- **once：** *bool*型，默认为`False`，用于*设置是否针对当前元素只进行一次视口检测*
- **margin：** *string*型，默认为`'0px'`，用于*为当前元素设置辅助视口检测的外边界大小*，可设置例如`200px`统一为上右下左添加外边界，也可设置例如`'0px -20px 0px 100px'`分别控制不同方向
- **amount：** *string*型，默认为`'some'`，用于*视口检测策略*，可选的有`'some'`、`'all'`

**variants：** *dict*型

　　用于*编排具有别名的样式组*