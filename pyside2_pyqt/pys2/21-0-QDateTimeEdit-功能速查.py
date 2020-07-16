QDateTimeEdit
描述
	编辑日期和时间的单行文本框
	既可以用箭头调节, 也可以用键盘编辑输入
	可以单独调节某个部分
继承
	QAbstractSpinBox
功能作用
	构造函数
		API
			QDateTimeEdit(parent: QWidget = None)
			QDateTimeEdit(Union[QDateTime, datetime.datetime], parent: QWidget = None)
			QDateTimeEdit(Union[QDate, datetime.date], parent: QWidget = None)
			QDateTimeEdit(Union[QTime, datetime.time], parent: QWidget = None)
		应用场景
			根据指定日期或时间, 创建出日期时间编辑器控件
			并会初始化该控件展示的section
		案例
			测试以上API
	显示格式
		API
			setDisplayFormat(format_str)
				设置日期时间显示格式
			displayFormat() -> str
				获取日期时间显示格式
		应用场景
			设置展示的section格式
		案例
			测试以上API
	section控制
		API
			sectionCount() -> int
				获取section个数
			setCurrentSectionIndex(int)
				设置当前的section索引
			currentSectionIndex() -> int
				获取section索引
			setCurrentSection(QDateTimeEdit.Section)
				设置当前操作的日期时间section
			currentSection() -> QDateTimeEdit.Section
				获取当前的section部分
			sectionAt(index_int) -> QDateTimeEdit.Section
				获取指定索引位置的section
			sectionText(QDateTimeEdit.Section) -> str
				获取指定section的文本内容
			00-01-01 $ 0: 01: 000
		应用场景
			控制section部分
		案例
			测试以上API
		补充
			QDateTimeEdit.Section
				QDateTimeEdit.NoSection
				QDateTimeEdit.AmPmSection
				QDateTimeEdit.MSecSection
				QDateTimeEdit.SecondSection
				QDateTimeEdit.MinuteSection
				QDateTimeEdit.HourSection
				QDateTimeEdit.DaySection
				QDateTimeEdit.MonthSection
				QDateTimeEdit.YearSection
	最大和最小日期时间
		API
			日期时间
				最大
					setMaximumDateTime(QDateTime)
						默认
							9999年12月31日 23:59:59 999毫秒
					maximumDateTime() -> QDateTime
					clearMaximumDateTime()
				最小
					setMinimumDateTime(QDateTime)
					minimumDateTime() -> QDateTime
					clearMinimumDateTime()
				范围
					setDateTimeRange(min_datetime, max_datetime)
			日期
				最大
					setMaximumDate(QDate)
						设置最大日期
						默认包含9999年12月31日
					maximumDate() -> QDate
						获取最大日期
					clearMaximumDate()
						清除自定义最大日期, 恢复默认
				最小
					setMinimumDate(QDate)
						设置最小日期
						默认1752年9月14日
					minimumDate() -> QDate
						获取最小日期
					clearMinimumDate()
						清除自定义最小日期, 恢复默认
				范围
					setDateRange(min_date, max_date)
			时间
				最大
					setMaximumTime(QTime)
					maximumTime() -> QTime
					clearMaximumTime()
				最小
					setMinimumTime(QTime)
					minimumTime() -> QTime
					clearMinimumTime()
				范围
					setTimeRange(min_time, max_time)
		应用场景
			控制日期范围
		案例
			测试以上API
	日历选择控件
		API
			是否弹出日历选择控件
				setCalendarPopup(bool)
				calendarPopup()
			自定义日历选择控件
				setCalendarWidget(QCalendarWidget)
				calendarWidget() -> QCalendarWidget
		应用场景
			通过日历选择控件, 快速的让用户输入日期
		案例
			测试以上API
	获取日期和时间
		API
			dateTime() -> QDateTime
			date() -> QDate
			time() -> QTime
		应用场景
			获取用户所输入的日期时间
		案例
			测试以上API
信号
	dateTimeChanged(QDateTime datetime)
	dateChanged(QDate date)
	timeChanged(QTime time)
补充
	QDateTime
		描述
			日期时间对象
			它是QDate和QTime类的组合
			包括年月日 时分秒毫秒
		功能作用
			日期时间对象构造
				    QDateTime()
				    QDateTime(QDateTime)
				    QDateTime(QDate)
				    QDateTime(QDate,  QTime, Qt.TimeSpec = Qt.LocalTime)
				    QDateTime(int, int, int, int, int, second: int = 0, msec: int = 0, timeSpec: int = 0)
				    QDateTime(QDate, QTime, Qt.TimeSpec, int)
				    QDateTime(QDate, QTime, QTimeZone)
				静态方法
					currentDateTime()
						当前时间
					currentDateTimeUtc()
						世界标准时间
			调整日期时间
				addYears(int)
				addMonths(int)
				addDays(int)
				addSecs(int)
				addMSecs(int)
				setDate(const QDate &date)
				setTime(const QTime &time)
			计算时间差
				offsetFromUtc()
				secsTo(QDateTime)
				msecsTo(QDateTime)
	QDate
		描述
			日期对象
			包括年月日
		功能作用
			日期对象的构造
				QDate()
				QDate(int y, int m, int d)
				currentDate()
			调整日期
				setDate(int year, int month, int day)
				addYears(int nyears)
				addMonths(int nmonths)
				addDays(qint64 ndays)
			计算时间差
				daysTo(const QDate &d)
			获取时间
				day()
					这一个月的第几日
				month()
					第几月
				year() 
					第几年
				dayOfWeek()
					这一周 第几日
				dayOfYear()
					这一年 第几日
				daysInMonth()
					这一月总共多少天
				daysInYear()
					这一年总共多少天
	QTime
		描述
			时间对象
			包括时分秒毫秒
		功能作用
			时间对象构造
				QTime()
				QTime(int h, int m, int s = 0, int ms = 0)
				currentTime()
			调整时间
				addSecs(int s)
				addMSecs(int ms)
			计算时间差
				secsTo(QTime t) 
			计时
				 start()
				restart()
				elapsed()
					以上两个方法启动后, 至此方法调用时, 经历的毫秒数
			获取时间
				hour()
				minute()
				second() 
				msec()
	时间日期格式符
		日期
			d
				没有前导零的数字的日期（1到31）
			dd
				有前导零的数字的日期（01到31）
			ddd
				缩写的本地化日期名称（例如'Mon'到'Sun'
			dddd
				完整本地化的日期名称（例如“星期一”到“星期日”）
			M
				没有前导零的数字的月份（1-12）
			MM
				月份为前导零的数字（01-12）
			MMM
				缩写的本地化月份名称（例如'Jan'到'Dec'）
			MMMM
				完整的本地化月份名称（例如“1月”到“12月”）
			yy
				年份为两位数字（00-99）
			yyyy
				年份为四位数字
		时间
			h
				没有前导零的小时（如果显示AM / PM，则为0到23或1到12）
			hh
				前导零的小时（如果AM / PM显示，则为00到23或01到12）
			H
				没有前导零的小时（0到23，即使有AM / PM显示）
			HH
				前导零的小时（00到23，即使有AM / PM显示）
			m
				没有前导零的分钟（0到59）
			mm
				前导零（00到59）的分钟
			s
				整个秒没有前导零（0到59）
			ss
				带有前导零（00到59）
			z
				第二个小数部分, 没有尾随零的毫秒（0到999）
			zzz
				第二个小数部分, 有尾随零的毫秒（000到999）
			AP / A
				使用AM / PM显示
			ap / a
				使用am / pm显示
			t
				时区
相关子类
	QDateEdit
		描述
			基于QDateTimeEdit控件的小控件
			主要操作日期部分
		继承
			QDateTimeEdit
		功能作用
			构造函数
				QDateEdit(QWidget *parent = nullptr)
				QDateEdit(const QDate &date, QWidget *parent = nullptr)
			显示格式
				API
					setDisplayFormat(format_str)
						设置日期时间显示格式
					displayFormat() -> str
						获取日期时间显示格式
				应用场景
					设置展示的section格式
				案例
					测试以上API
			最大和最小日期
				最大
					setMaximumDate(QDate)
						设置最大日期
						默认包含9999年12月31日
					maximumDate() -> QDate
						获取最大日期
					clearMaximumDate()
						清除自定义最大日期, 恢复默认
				最小
					setMinimumDate(QDate)
						设置最小日期
						默认1752年9月14日
					minimumDate() -> QDate
						获取最小日期
					clearMinimumDate()
						清除自定义最小日期, 恢复默认
				范围
					setDateRange(min_date, max_date)
			获取日期
				date() -> QDate
			...
		信号
			继承父类
	QTimeEdit
		描述
			基于QDateTimeEdit控件的小控件
			主要操作时间部分
		继承
			QDateTimeEdit
		功能作用
			构造函数
				QTimeEdit(QWidget *parent = nullptr)
				QTimeEdit(const QTime &time, QWidget *parent = nullptr)
			显示格式
				API
					setDisplayFormat(format_str)
						设置日期时间显示格式
					displayFormat() -> str
						获取日期时间显示格式
				应用场景
					设置展示的section格式
				案例
					测试以上API
			时间
				最大
					setMaximumTime(QTime)
					maximumTime() -> QTime
					clearMaximumTime()
				最小
					setMinimumTime(QTime)
					minimumTime() -> QTime
					clearMinimumTime()
				范围
					setTimeRange(min_time, max_time)
			获取时间
				time() -> QTime
			...
		信号
			继承父类