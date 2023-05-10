**id：** *string*型

　　用于设置*当前组件的唯一id信息*

**children：** *组件型*

　　用于传入*嵌套的子元素*

**enabled：** *bool*型，默认为`True`

　　用于*设置是否启用当前组件的粘性布局效果*

**top：** *int*或*string*型

　　用于*设置触发粘性布局效果对应的顶部距离阈值*，当当前元素距离窗口顶部达到此阈值时会触发粘性布局状态，其中：

- 当传入*int*型时，用于*设置窗口顶端到当前元素顶部的像素距离阈值*
- 当传入*string*型时，用于*定义css选择器规则*，被此选择器规则匹配到的元素的高度会被作为阈值所使用

**bottomBoundary：** *int*或*string*型

　　用于*设置解除粘性布局效果对应的底部距离阈值*，其中：

- 当传入*int*型时，用于*设置页面顶端到当前元素顶部的像素距离阈值*
- 当传入*string*型时，用于*定义css选择器规则*，当该规则匹配到的目标元素底部到达粘性布局元素底部时，粘性状态会被解除

**zIndex：** *int*型

　　用于*设置当前粘性布局元素的z-index属性*



