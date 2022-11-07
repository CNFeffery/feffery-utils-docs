**id：** *string*型

　　用于设置*当前组件的唯一id信息*

**style：** *dict*型

　　用于设置*当前组件的css样式*

**className：** *string*型

　　用于设置*当前组件的css类名*

**caseSensitive：** *bool*型，默认为`False`

　　用于设置*匹配规则是否大小写敏感*

**highlightClassName：** *string*型，默认为`'feffery-highlight-words-highlight'`

　　用于设置*高亮内容的css样式类*

**highlightStyle：** *dict*型

　　用于设置*高亮内容的css样式*

**unhighlightClassName：** *string*型

　　用于设置*非高亮内容的css样式类*

**unhighlightStyle：** *dict*型

　　用于设置*非高亮内容的css样式*

**useRegex：** *bool*型，默认为`False`

　　用于设置*是否开启正则表达式匹配模式*

**searchWords：** `list[string]`型

　　用于设置*高亮内容匹配规则*，当`useRegex=True`时，`searchWords`中的每个元素都将被视作正则表达式

**textToHighlight：** *string*型

　　用于设置*原始文本内容*