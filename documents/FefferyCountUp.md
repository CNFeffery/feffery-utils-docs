**id：** *string*型

　　用于设置*当前组件的唯一id信息*

**style：** *dict*型

　　用于设置*当前组件的css样式*

**className：** *string*型

　　用于设置*当前组件的css类名*

**end：** *int*或*float*型，必填

　　用于*设置数字递增动画的目标数值*

**start：** *int*或*float*型，默认为`0`

　　用于*设置数字递增动画的起点数值*

**duration：** *int*或*float*型，默认为`2`

　　用于*设置数字递增动画过程耗时*，单位：秒

**decimals：** *int*型，默认为`0`

　　用于*设置数值显示所保留的小数位数*

**enableScrollSpy：** *bool*型，默认为`True`

　　用于*设置是否在当前数字递增在视口中出现时才开始动画*

**scrollSpyDelay：** *int*型，默认为`0`

　　当`enableScrollSpy=True`时，用于*设置从数字递增进入视口到播放动画之间的延时时长*，单位：毫秒

**scrollSpyOnce：** *bool*型，默认为`True`

　　设置*是否仅对当前数字递增进行1次视口检测*

**separator：** *string*型，默认为`','`

　　用于*为当前递增数字设置千分符*

