组合框(下拉选择输入) QComboBox

描述
	是一个组合控件
	默认展示最小的空间给用户操作
	可通过下拉选择界面, 选取更多的预置选项
继承
	QWidget
功能作用
	构造函数
		API
			QComboBox(parent: QWidget = None)
		应用场景
			构造出一个空白的下拉列表控件
			后续通过操作数据的方法设置数据列表
		案例
			测试以上API
	数据操作
		API
		添加条目项
			addItem(str, userData: Any = None)
			addItem(QIcon, str, userData: Any = None)
			addItems(Iterable[str])
		插入条目项
			insertItem(int, str, userData: Any = None)
			insertItem(int, QIcon, str, userData: Any = None)
			insertItems(int, Iterable[str])
		设置条目项
			setItemIcon(int, QIcon)
			setItemText(int, str)
			setItemData(int, Any, role: int = Qt.UserRole)
		删除条目项
			removeItem(int index)
		插分割线
			insertSeparator(int index)
		设置当前编辑文本
			setCurrentIndex(int index)
			setCurrentText(QString text)
			setEditText(QString text) 
                必须先将对象设置为可编辑，则可以添加条目
				结合设置可被编辑
		了解MVC
            用不同的view来展示相应的数据model，达到自定义下拉选择框的目的。
            比如展示多级项目列表model,就可以用树形view。 
			模型操作
				setModel(QAbstractItemModel model)
				setModelColumn(int visibleColumn)
				setRootModelIndex(QModelIndex index)
				model() 
				modelColumn()
				rootModelIndex()
			视图操作
				setView(QAbstractItemView *itemView)
				view() 
			代理设置
				setItemDelegate(QAbstractItemDelegate *delegate)
		应用场景
			增删改条目内容
		案例
			测试以上API
	常用数据获取
		API
			count() -> int
			itemIcon(int index) -> QIcon
			itemText(int index) -> str
			itemData(int index) -> Any
			currentIndex() -> int
			currentText() -> str
		应用场景
			获取相关数据
		案例
			测试以上API
	数据限制
		API
			setMaxCount(int max)
			maxCount() 
			setMaxVisibleItems(int maxItems) 最多可见条目个数 超过会有滚动条
			maxVisibleItems()
		应用场景
			限制数据内容显示等限制
		案例
			测试以上API
	尝龟操作
		API
		可编辑
			setEditable(bool editable) 设为True 则 光标在文本框 可编辑 回车就增加条目
			isEditable() 默认是False
		可重复
			setDuplicatesEnabled(bool enable)
			duplicatesEnabled() 默认是False 不可重复
		有框架
			setFrame(bool)
			hasFrame() 默认是True
		图标尺寸
			setIconSize(QSize)
			iconSize()
		尺寸调整策略
			setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy policy)
				QComboBox.AdjustToContents	
					组合框将始终根据内容进行调整
				QComboBox.AdjustToContentsOnFirstShow
					组合框将在第一次显示时调整其内容。默认值
				QComboBox.AdjustToMinimumContentsLength
					请改用AdjustToContents或AdjustToContentsOnFirstShow。
				QComboBox.AdjustToMinimumContentsLengthWithIcon
					组合框将调整为minimumContentsLength加上图标的空间。出于性能原因，请在大型模型上使用此策略。
			sizeAdjustPolicy() -> QComboBox.SizeAdjustPolicy
			setMinimumContentsLength(int characters)
			minimumContentsLength() -> int
		清空
			clear()
				移除所有项目
			clearEditText()
				# 清除组合框中用于编辑的行编辑内容 ，条目并没有减少。只是清空了文本框而已。
		弹出
			showPopup()
		完成器
			setCompleter(QCompleter completer)
			completer() -> QCompleter
		验证器
			setValidator(QValidator validator)
			validator()
		场景
			看着用吧
		案例
			测试一下, 以后按需求来用即可!
信号
	activated(int index)
    activated(QString text)
		某个条目被选中时
			必须是用户交互, 造成的值改变才会发射这个信号
            代码设置的不会发射信号。
	
	currentIndexChanged(int index)
    currentIndexChanged(QString text)
		当前索引发生改变时
			用户交互
			代码控制
	
	currentTextChanged(QString text)
		当前的文本内容发生改变时

	editTextChanged(QString text)
		编辑的文本发生改变时

	highlighted(int index)
    highlighted(QString text)
		高亮

案例
	给定城市数据
	实现两级联动效果

相关子类
	QFontComboBox
		描述
			组合框中填充了按字母顺序排列的字体系列名称列表
			让用户选择字体家族
		继承
			QComboBox
		功能作用
			设置和获取当前字体
				setCurrentFont(QFont f)
				currentFont() -> QFont
			设置和获取过滤器
				setFontFilters(QFontComboBox.FontFilters)
				fontFilters() -> QFontComboBox.FontFilters
		信号
			继承
				currentIndexChanged(QString text)
			currentFontChanged(QFont font)
		补充
			QFontComboBox.FontFilters
				QFontComboBox.AllFonts
					显示所有字体
				QFontComboBox.ScalableFonts
					显示可缩放字体
				QFontComboBox.NonScalableFonts
					显示不可缩放的字体
				QFontComboBox.MonospacedFonts
					显示等宽字体
				QFontComboBox.ProportionalFonts
					显示比例字体