from PyQt5 import QtGui, QtCore, QtWidgets, Qt
import sys
import qtawesome


class MainUi(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # 初始化折叠参数
        self.getFold = False
        self.__init_ui()

    def __init_ui(self):
        self.setFixedSize(960, 500)
        self.main_widget = QtWidgets.QWidget()  # 创建窗口主部件
        self.main_layout = QtWidgets.QGridLayout()  # 创建主部件的网络布局层
        self.main_widget.setLayout(self.main_layout)  # 将布局设置为网格布局

        # 创建基础布局
        self.top_widget = QtWidgets.QWidget()  # 创建右侧部件
        self.top_widget.setObjectName("top_widget")

        self.left_widget = QtWidgets.QWidget()  # 创建右侧部件
        self.left_widget.setObjectName("left_widget")

        # 顶部布局设计
        self.top_little = QtWidgets.QLabel(self.top_widget)
        self.top_little.setText("寒烟云")
        self.top_little.setGeometry(QtCore.QRect(10, 0, 60, 30))
        self.top_mini_button = QtWidgets.QPushButton(self.top_widget)
        self.top_mini_button.setIcon(QtGui.QIcon('./resource/img/mini.png'))
        self.top_mini_button.setObjectName("top_mini")
        self.top_mini_button.setGeometry(QtCore.QRect(820, 0, 40, 30))
        self.top_mini_button.setIconSize(QtCore.QSize(30, 30))
        self.top_max_button = QtWidgets.QPushButton(self.top_widget)
        self.top_max_button.setIcon(QtGui.QIcon('./resource/img/max.png'))
        self.top_max_button.setObjectName("top_max")
        self.top_max_button.setGeometry(QtCore.QRect(860, 0, 40, 30))
        self.top_max_button.setIconSize(QtCore.QSize(30, 30))
        self.top_close_button = QtWidgets.QPushButton(self.top_widget)
        self.top_close_button.setIcon(QtGui.QIcon('./resource/img/close.png'))
        self.top_close_button.setObjectName("top_close")
        self.top_close_button.setGeometry(QtCore.QRect(900, 0, 40, 30))
        self.top_close_button.setIconSize(QtCore.QSize(40, 40))

        # 左侧布局设计
        self.left_fold = QtWidgets.QPushButton(self.left_widget)      # 折叠按钮
        self.left_fold.setIcon(qtawesome.icon('fa.bars', color='gray'))
        self.left_fold.setIconSize(QtCore.QSize(25, 25))
        self.left_button_1 = QtWidgets.QPushButton(self.left_widget)
        self.left_button_1.setIcon(qtawesome.icon('fa.home', color='gray'))
        self.left_button_1.setText("首页")
        self.left_button_1.setIconSize(QtCore.QSize(25, 25))
        self.left_button_1.setObjectName("left_button")
        self.left_button_2 = QtWidgets.QPushButton(self.left_widget)
        self.left_button_2.setIcon(qtawesome.icon('fa.folder', color='gray'))
        self.left_button_2.setText("资源管理器")
        self.left_button_2.setIconSize(QtCore.QSize(25, 25))
        self.left_button_2.setObjectName("left_button")
        self.left_button_3 = QtWidgets.QPushButton(self.left_widget)
        self.left_button_3.setIcon(qtawesome.icon('fa.desktop', color='gray'))
        self.left_button_3.setText("屏幕捕获")
        self.left_button_3.setIconSize(QtCore.QSize(25, 25))
        self.left_button_3.setObjectName("left_button")
        self.left_button_4 = QtWidgets.QPushButton(self.left_widget)
        self.left_button_4.setIcon(qtawesome.icon('fa.camera', color='gray'))
        self.left_button_4.setText("视频语音")
        self.left_button_4.setIconSize(QtCore.QSize(25, 25))
        self.left_button_4.setObjectName("left_button")
        self.left_button_5 = QtWidgets.QPushButton(self.left_widget)
        self.left_button_5.setIcon(qtawesome.icon('fa.window-maximize', color='gray'))
        self.left_button_5.setText("控制台")
        self.left_button_5.setIconSize(QtCore.QSize(25, 25))
        self.left_button_5.setObjectName("left_button")
        self.left_button_6 = QtWidgets.QPushButton(self.left_widget)
        self.left_button_6.setIcon(qtawesome.icon('fa.cubes', color='gray'))
        self.left_button_6.setText("扩展功能")
        self.left_button_6.setIconSize(QtCore.QSize(25, 25))
        self.left_button_6.setObjectName("left_button")
        self.left_button_7 = QtWidgets.QPushButton(self.left_widget)
        self.left_button_7.setIcon(qtawesome.icon('fa.mobile-phone', color='gray'))
        self.left_button_7.setText("手机")
        self.left_button_7.setIconSize(QtCore.QSize(25, 25))
        self.left_button_7.setObjectName("left_button")

        self.left_fold.setGeometry(QtCore.QRect(5, 0, 40, 40))
        self.left_button_1.setGeometry(QtCore.QRect(5, 40, 150, 40))
        self.left_button_2.setGeometry(QtCore.QRect(5, 80, 150, 40))
        self.left_button_3.setGeometry(QtCore.QRect(5, 120, 150, 40))
        self.left_button_4.setGeometry(QtCore.QRect(5, 160, 150, 40))
        self.left_button_5.setGeometry(QtCore.QRect(5, 200, 150, 40))
        self.left_button_6.setGeometry(QtCore.QRect(5, 240, 150, 40))
        self.left_button_7.setGeometry(QtCore.QRect(5, 280, 150, 40))

        # 将左侧和上侧部件加入主窗口
        self.main_layout.addWidget(self.top_widget, 0, 0, 1, 40)
        self.main_layout.addWidget(self.left_widget, 1, 0, 15, 6)

        # 左侧和顶部的QSS样式设计
        self.top_widget.setStyleSheet(
            '''
             QWidget#top_widget{
                background:white;
                border-top:1px solid rgba(255, 255, 255, 40);
                border-bottom:lpx solid  rgba(255, 255, 255, 40);
                border-left:1px solid  rgba(255, 255, 255, 40);
            }
            QPushButton{
                border:none;
                color:white;
            }
            QPushButton#top_mini::hover{
                background: #CCCCCC;
            }
            QPushButton#top_max::hover{
                background: #CCCCCC;
            }
            QPushButton#top_close::hover{
                background: #EE3B3B;
            }
            QLabel{
                font-size: 12px;
                font-weight:50;
                font-family:'微软雅黑'
            }
            '''
        )
        self.left_widget.setStyleSheet(
            '''
            QPushButton{
                border:none;
                color:white;
                text-align: left;
                font-size:16px;
                font-weight:100;
                font-family:"楷体";
                }
            QWidget#left_widget{
                background:rgb(50, 50, 50);
                border-bottom:lpx solid  rgba(255, 255, 255, 40);
                border-left:1px solid  rgba(255, 255, 255, 40);
            }
            QPushButton#left_button::hover{
                border-left:2px solid #CD0000;
                background: rgba(255, 255, 255, 40);
                font-weight:700;
            }
            '''
        )

        # 加载右侧布局
        self.__loading_home()
        self.__loading_explorer()

        # 初始化右侧部件
        self.right_widget = self.right_home_widget
        self.right_widget.show()

        # 设置窗口主部件
        self.setCentralWidget(self.main_widget)

        # 边框隐藏，透明
        self.setWindowOpacity(0.95)  # 设置窗口透明
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        self.main_layout.setSpacing(0)

        # 触发事件
        self.top_close_button.clicked.connect(QtCore.QCoreApplication.quit)
        self.left_fold.clicked.connect(self.fold)
        self.left_button_1.clicked.connect(self.__switch_home)
        self.left_button_2.clicked.connect(self.__switch_explorer)

    def __loading_home(self):
        self.right_home_widget = QtWidgets.QWidget()  # 创建右侧部件
        self.right_home_widget.setObjectName("right_widget")
        self.right_home_layout = QtWidgets.QGridLayout()  # 创建左部件的网络布局层
        self.right_home_widget.setLayout(self.right_home_layout)  # 将左侧布局设置为网格布局
        # 状态布局
        self.right_state_label = QtWidgets.QLabel("连接状态")
        self.right_state_label.setObjectName("right_label")
        self.right_table_label = QtWidgets.QLabel("主机信息")
        self.right_table_label.setObjectName("right_label")

        self.right_state_widget = QtWidgets.QWidget()  # 右侧连接状态主部件
        self.right_state_layout = QtWidgets.QGridLayout()  # 右侧连接状态主部件网格
        self.right_state_widget.setLayout(self.right_state_layout)

        self.right_control_label = QtWidgets.QLabel()
        self.right_control_label.setPixmap(QtGui.QPixmap('./resource/img/tv.png'))
        self.right_control_label.setScaledContents(True)
        self.right_control_label.setFixedSize(QtCore.QSize(50, 50))
        self.right_link1_label = QtWidgets.QLabel()
        self.right_link1_label.setPixmap(QtGui.QPixmap('./resource/img/link.png'))
        self.right_link1_label.setScaledContents(True)
        self.right_link1_label.setFixedSize(QtCore.QSize(100, 10))
        self.right_server_label = QtWidgets.QLabel()
        self.right_server_label.setPixmap(QtGui.QPixmap('./resource/img/load.png'))
        self.right_server_label.setScaledContents(True)
        self.right_server_label.setFixedSize(QtCore.QSize(50, 50))
        self.right_link2_label = QtWidgets.QLabel()
        self.right_link2_label.setPixmap(QtGui.QPixmap('./resource/img/link.png'))
        self.right_link2_label.setScaledContents(True)
        self.right_link2_label.setFixedSize(QtCore.QSize(100, 10))
        self.right_controlled_label = QtWidgets.QLabel()
        self.right_controlled_label.setPixmap(QtGui.QPixmap('./resource/img/server.png'))
        self.right_controlled_label.setScaledContents(True)
        self.right_controlled_label.setFixedSize(QtCore.QSize(50, 50))

        self.right_state_layout.addWidget(self.right_control_label, 0, 3, 1, 1)
        self.right_state_layout.addWidget(self.right_link1_label, 0, 4, 1, 1)
        self.right_state_layout.addWidget(self.right_server_label, 0, 5, 1, 1)
        self.right_state_layout.addWidget(self.right_link2_label, 0, 6, 1, 1)
        self.right_state_layout.addWidget(self.right_controlled_label, 0, 7, 1, 1)
        self.right_state_layout.setAlignment(QtCore.Qt.AlignCenter)

        self.right_state_text_widget = QtWidgets.QWidget()  # 状态信息主部件
        self.right_state_text_layout = QtWidgets.QGridLayout()  # 状态信息主部件网格
        self.right_state_text_widget.setLayout(self.right_state_text_layout)
        self.right_state_report_text = QtWidgets.QLabel()
        self.right_state_report_text.setObjectName("state_report")
        self.right_state_report_text.setText("正在尝试连接服务器....")
        self.right_state_information_text = QtWidgets.QLabel()
        self.right_state_information_text.setObjectName("information_report")
        self.right_state_information_text.setText("服务器IP:  127. 0. 0. 1\n"
                                                  "本机IP:  127. 0. 0. 1\n终端IP:  127. 0. 0. 1")

        self.right_state_text_layout.addWidget(self.right_state_report_text, 1, 1, 1, 3)
        self.right_state_text_layout.addWidget(self.right_state_information_text, 2, 1, 1, 3)
        self.right_state_text_layout.setAlignment(QtCore.Qt.AlignCenter)

        # 信息表格布局
        self.right_information_widget = QtWidgets.QWidget()  # 信息表主部件
        self.right_information_layout = QtWidgets.QGridLayout()  # 信息表主部件网格
        self.right_information_widget.setLayout(self.right_information_layout)

        self.right_information_table = QtWidgets.QTableWidget()
        self.right_information_table.setRowCount(10)
        self.right_information_table.setColumnCount(13)
        information_table_label = ['序号', '国家', '地理位置', 'IP地址', 'isp运营商', '在线状态', '上次登录时间', '用户名',
                                   '主机名称', '系统', '硬盘', '内存', '处理器']
        self.right_information_table.setHorizontalHeaderLabels(information_table_label)
        self.right_information_table.verticalHeader().setVisible(False)
        self.right_information_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)  # 将表格设置为行选中
        self.right_information_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)  # 将表格设置为不可编辑

        self.right_information_layout.addWidget(self.right_information_table)

        # 右侧子布局加入总布局
        self.right_home_layout.addWidget(self.right_state_label, 0, 0, 1, 1)
        self.right_home_layout.addWidget(self.right_state_widget, 1, 0, 2, 9)
        self.right_home_layout.addWidget(self.right_state_text_widget, 3, 0, 1, 9)
        self.right_home_layout.addWidget(self.right_table_label, 4, 0, 1, 1)
        self.right_home_layout.addWidget(self.right_information_widget, 7, 0, 8, 9)

        self.right_home_widget.setStyleSheet(
            '''
            QLabel#state_report{
                font-size:20px;
                font-weight:100;
                font-family:"微软雅黑";
            }
            QLabel#state_information{
                font-size:10px;
                font-weight:100;
                font-family:"微软雅黑";
            }

            QWidget#right_widget{
                background:white;
                border-bottom:lpx solid  rgba(255, 255, 255, 40);
                border-right:1px solid  rgba(255, 255, 255, 40);
            }
             QLabel#right_label{
                border:none;
                font-size:18px;
                font-weight:300;
                font-family: "仿宋";
            }
            /**********表格**********/
            QTableView {
                    border: 1px solid rgb(45, 45, 45);
                    background: rgb(57, 58, 60);
                    gridline-color: rgb(60, 60, 60);
            }
            QTableView::item {
                    padding-left: 5px;
                    padding-right: 5px;
                    border: none;
                    background: rgb(72, 72, 74);
                    border-right: 1px solid rgb(45, 45, 45);
                    border-bottom: 1px solid rgb(45, 45, 45);
            }
            QTableView::item:selected {
                    background: rgba(255, 255, 255, 40);
            }
            QTableView::item:selected:!active {
                    color: white;
            }
            QTableView::indicator {
                    width: 20px;
                    height: 20px;
            }
            QTableView::indicator:enabled:unchecked {
                    image: url(:/Black/checkBox);
            }
            QTableView::indicator:enabled:unchecked:hover {
                    image: url(:/Black/checkBoxHover);
            }
            QTableView::indicator:enabled:unchecked:pressed {
                    image: url(:/Black/checkBoxPressed);
            }
            QTableView::indicator:enabled:checked {
                    image: url(:/Black/checkBoxChecked);
            }
            QTableView::indicator:enabled:checked:hover {
                    image: url(:/Black/checkBoxCheckedHover);
            }
            QTableView::indicator:enabled:checked:pressed {
                    image: url(:/Black/checkBoxCheckedPressed);
            }
            QTableView::indicator:enabled:indeterminate {
                    image: url(:/Black/checkBoxIndeterminate);
            }
            QTableView::indicator:enabled:indeterminate:hover {
                    image: url(:/Black/checkBoxIndeterminateHover);
            }
            QTableView::indicator:enabled:indeterminate:pressed {
                    image: url(:/Black/checkBoxIndeterminatePressed);
            }

            QHeaderView{
                border: none;
                border-bottom: 3px solid rgb(0, 160, 230);
                background: rgb(57, 58, 60);
                min-height: 30px;
            }
            QHeaderView::section:horizontal {
                    border: none;
                    color: white;
                    background: transparent;
                    padding-left: 5px;
            }
            QHeaderView::section:horizontal:hover {
                    background: rgb(0, 160, 230);
            }
            QHeaderView::section:horizontal:pressed {
                    background: rgb(0, 180, 255);
            }
            QHeaderView::up-arrow {
                    width: 13px;
                    height: 11px;
                    padding-right: 5px;
                    image: url(:/Black/topArrow);
                    subcontrol-position: center right;
            }
            QHeaderView::up-arrow:hover, QHeaderView::up-arrow:pressed {
                    image: url(:/Black/topArrowHover);
            }
            QHeaderView::down-arrow {
                    width: 13px;
                    height: 11px;
                    padding-right: 5px;
                    image: url(:/Black/bottomArrow);
                    subcontrol-position: center right;
            }
            QHeaderView::down-arrow:hover, QHeaderView::down-arrow:pressed {
                    image: url(:/Black/bottomArrowHover);
            }

            /**********滚动条-水平**********/QScrollBar:horizontal {
                    height: 20px;
                    background: transparent;
                    margin-top: 3px;
                    margin-bottom: 3px;
            }
            QScrollBar::handle:horizontal {
                    height: 20px;
                    min-width: 30px;
                    background: rgb(68, 69, 73);
                    margin-left: 15px;
                    margin-right: 15px;
            }
            QScrollBar::handle:horizontal:hover {
                    background: rgb(80, 80, 80);
            }
            QScrollBar::sub-line:horizontal {
                    width: 15px;
                    background: transparent;
                    image: url(:/Black/arrowLeft);
                    subcontrol-position: left;
            }
            QScrollBar::add-line:horizontal {
                    width: 15px;
                    background: transparent;
                    image: url(:/Black/arrowRight);
                    subcontrol-position: right;
            }
            QScrollBar::sub-line:horizontal:hover {
                    background: rgb(68, 69, 73);
            }
            QScrollBar::add-line:horizontal:hover {
                    background: rgb(68, 69, 73);
            }
            QScrollBar::add-page:horizontal,QScrollBar::sub-page:horizontal {
                    background: transparent;
            }

            /**********滚动条-垂直**********/
            QScrollBar:vertical {
                    width: 20px;
                    background: transparent;
                    margin-left: 3px;
                    margin-right: 3px;
            }
            QScrollBar::handle:vertical {
                    width: 20px;
                    min-height: 30px;
                    background: rgb(68, 69, 73);
                    margin-top: 15px;
                    margin-bottom: 15px;
            }
            QScrollBar::handle:vertical:hover {
                    background: rgb(80, 80, 80);
            }
            QScrollBar::sub-line:vertical {
                    height: 15px;
                    background: transparent;
                    image: url(:/Black/arrowTop);
                    subcontrol-position: top;
            }
            QScrollBar::add-line:vertical {
                    height: 15px;
                    background: transparent;
                    image: url(:/Black/arrowBottom);
                    subcontrol-position: bottom;
            }
            QScrollBar::sub-line:vertical:hover {
                    background: rgb(68, 69, 73);
            }
            QScrollBar::add-line:vertical:hover {
                    background: rgb(68, 69, 73);
            }
            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                    background: transparent;
            }

            QScrollBar#verticalScrollBar:vertical {
                    margin-top: 30px;
            }

            '''
        )

        self.main_layout.addWidget(self.right_home_widget, 1, 6, 15, 34)
        self.right_home_widget.hide()

    def __loading_explorer(self):
        self.right_explorer_widget = QtWidgets.QWidget()  # 创建右侧部件
        self.right_explorer_widget.setObjectName("right_widget")
        self.right_explorer_layout = QtWidgets.QGridLayout()  # 创建左部件的网络布局层
        self.right_explorer_widget.setLayout(self.right_explorer_layout)  # 将左侧布局设置为网格布局

        # 资源信息工具部件
        self.right_tool_widget = QtWidgets.QWidget()    # 创建资源工具部件
        self.right_tool_layout = QtWidgets.QGridLayout()    # 创建资源工具部件网格
        self.right_tool_widget.setLayout(self.right_tool_layout)

        self.right_back_button = QtWidgets.QPushButton(qtawesome.icon('fa.arrow-left', color='black'), "")
        self.right_ahead_button = QtWidgets.QPushButton(qtawesome.icon('fa.arrow-right', color='black'), "")
        self.right_file_path = QtWidgets.QLineEdit()
        self.right_refresh = QtWidgets.QPushButton(qtawesome.icon('fa.refresh', color='black'), "")
        self.right_search_content = QtWidgets.QLineEdit()
        self.right_search_button = QtWidgets.QPushButton(qtawesome.icon('fa.search', color='black'), "")

        self.right_tool_layout.addWidget(self.right_back_button, 0, 0, 1, 1)
        self.right_tool_layout.addWidget(self.right_ahead_button, 0, 1, 1, 1)
        self.right_tool_layout.addWidget(self.right_file_path, 0, 2, 1, 10)
        self.right_tool_layout.addWidget(self.right_refresh, 0, 12, 1, 1)
        self.right_tool_layout.addWidget(self.right_search_content, 0, 13, 1, 2)
        self.right_tool_layout.addWidget(self.right_search_button, 0, 15, 1, 1)

        self.right_table_widget = QtWidgets.QWidget()   # 右边资源表格部件
        self.right_table_layout = QtWidgets.QHBoxLayout()   # 右边资源表格部件网格
        self.right_table_widget.setLayout(self.right_table_layout)

        self.resource_tree_table = QtWidgets.QTreeView()
        self.resource_table = QtWidgets.QTableView()
        self.right_table_layout.addWidget(self.resource_tree_table, 1)
        self.right_table_layout.addWidget(self.resource_table, 3)

        self.right_explorer_layout.addWidget(self.right_tool_widget, 0, 0, 1, 10)
        self.right_explorer_layout.addWidget(self.right_table_widget, 1, 0, 9, 10)
        self.right_explorer_layout.setSpacing(0)

        self.main_layout.addWidget(self.right_explorer_widget, 1, 6, 15, 34)
        self.right_explorer_widget.hide()

        self.right_explorer_widget.setStyleSheet(
            '''
            QLabel#state_report{
                font-size:20px;
                font-weight:100;
                font-family:"微软雅黑";
            }
            QLabel#state_information{
                font-size:10px;
                font-weight:100;
                font-family:"微软雅黑";
            }
            QPushButton{
                border:none;
                width: 30px;
                height: 30px;
            }
            QPushButton::hover{
                background: #CCCCCC;
            }
            QWidget#right_widget{
                background:white;
                border-bottom:lpx solid  rgba(255, 255, 255, 40);
                border-right:1px solid  rgba(255, 255, 255, 40);
            }
             QLabel#right_label{
                border:none;
                font-size:18px;
                font-weight:300;
                font-family: "仿宋";
            }
            /**********表格**********/
            QTableView {
                    border: 1px solid rgb(45, 45, 45);
                    background: rgb(57, 58, 60);
                    gridline-color: rgb(60, 60, 60);
            }
            QTableView::item {
                    padding-left: 5px;
                    padding-right: 5px;
                    border: none;
                    background: rgb(72, 72, 74);
                    border-right: 1px solid rgb(45, 45, 45);
                    border-bottom: 1px solid rgb(45, 45, 45);
            }
            QTableView::item:selected {
                    background: rgba(255, 255, 255, 40);
            }
            QTableView::item:selected:!active {
                    color: white;
            }
            QTableView::indicator {
                    width: 20px;
                    height: 20px;
            }
            


            /**********滚动条-水平**********/
            QScrollBar:horizontal {
                    height: 20px;
                    background: transparent;
                    margin-top: 3px;
                    margin-bottom: 3px;
            }
            QScrollBar::handle:horizontal {
                    height: 20px;
                    min-width: 30px;
                    background: rgb(68, 69, 73);
                    margin-left: 15px;
                    margin-right: 15px;
            }
            QScrollBar::handle:horizontal:hover {
                    background: rgb(80, 80, 80);
            }
            QScrollBar::sub-line:horizontal {
                    width: 15px;
                    background: transparent;
                    image: url(:/Black/arrowLeft);
                    subcontrol-position: left;
            }
            QScrollBar::add-line:horizontal {
                    width: 15px;
                    background: transparent;
                    image: url(:/Black/arrowRight);
                    subcontrol-position: right;
            }
            QScrollBar::sub-line:horizontal:hover {
                    background: rgb(68, 69, 73);
            }
            QScrollBar::add-line:horizontal:hover {
                    background: rgb(68, 69, 73);
            }
            QScrollBar::add-page:horizontal,QScrollBar::sub-page:horizontal {
                    background: transparent;
            }

            /**********滚动条-垂直**********/
            QScrollBar:vertical {
                    width: 20px;
                    background: transparent;
                    margin-left: 3px;
                    margin-right: 3px;
            }
            QScrollBar::handle:vertical {
                    width: 20px;
                    min-height: 30px;
                    background: rgb(68, 69, 73);
                    margin-top: 15px;
                    margin-bottom: 15px;
            }
            QScrollBar::handle:vertical:hover {
                    background: rgb(80, 80, 80);
            }
            QScrollBar::sub-line:vertical {
                    height: 15px;
                    background: transparent;
                    image: url(:/Black/arrowTop);
                    subcontrol-position: top;
            }
            QScrollBar::add-line:vertical {
                    height: 15px;
                    background: transparent;
                    image: url(:/Black/arrowBottom);
                    subcontrol-position: bottom;
            }
            QScrollBar::sub-line:vertical:hover {
                    background: rgb(68, 69, 73);
            }
            QScrollBar::add-line:vertical:hover {
                    background: rgb(68, 69, 73);
            }
            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                    background: transparent;
            }

            QScrollBar#verticalScrollBar:vertical {
                    margin-top: 30px;
            }

            '''
        )

    def __switch_home(self):
        self.right_widget.hide()
        self.right_widget = self.right_home_widget
        self.right_widget.show()

    def __switch_explorer(self):
        self.right_widget.hide()
        self.right_widget = self.right_explorer_widget
        self.right_widget.show()

    # 鼠标拖动方法重写
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            QtWidgets.QApplication.postEvent(self, Qt.QEvent(174))
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()

    # 标签折叠方法
    def fold(self):
        if self.left_button_1.text() != "":
            self.left_button_1.setText("")
            self.left_button_1.setGeometry(QtCore.QRect(5, 40, 40, 40))
            self.left_button_2.setText("")
            self.left_button_2.setGeometry(QtCore.QRect(5, 80, 40, 40))
            self.left_button_3.setText("")
            self.left_button_3.setGeometry(QtCore.QRect(5, 120, 40, 40))
            self.left_button_4.setText("")
            self.left_button_4.setGeometry(QtCore.QRect(5, 160, 40, 40))
            self.left_button_5.setText("")
            self.left_button_5.setGeometry(QtCore.QRect(5, 200, 40, 40))
            self.left_button_6.setText("")
            self.left_button_6.setGeometry(QtCore.QRect(5, 240, 40, 40))
            self.left_button_7.setText("")
            self.left_button_7.setGeometry(QtCore.QRect(5, 280, 40, 40))
            # 重置布局
            self.main_layout.addWidget(self.top_widget, 0, 0, 1, 40)
            self.main_layout.addWidget(self.left_widget, 1, 0, 15, 2)
            self.main_layout.addWidget(self.right_home_widget, 1, 2, 15, 38)
            self.main_layout.addWidget(self.right_explorer_widget, 1, 2, 15, 38)
            # 重置状态
            self.getFold = True
        else:
            self.left_button_1.setText("首页")
            self.left_button_1.setGeometry(QtCore.QRect(5, 40, 150, 40))
            self.left_button_2.setText("资源管理器")
            self.left_button_2.setGeometry(QtCore.QRect(5, 80, 150, 40))
            self.left_button_3.setText("屏幕捕获")
            self.left_button_3.setGeometry(QtCore.QRect(5, 120, 150, 40))
            self.left_button_4.setText("视频语音")
            self.left_button_4.setGeometry(QtCore.QRect(5, 160, 150, 40))
            self.left_button_5.setText("控制台")
            self.left_button_5.setGeometry(QtCore.QRect(5, 200, 150, 40))
            self.left_button_6.setText("扩展功能")
            self.left_button_6.setGeometry(QtCore.QRect(5, 240, 150, 40))
            self.left_button_7.setText("手机")
            self.left_button_7.setGeometry(QtCore.QRect(5, 280, 150, 40))
            # 恢复布局
            self.main_layout.addWidget(self.top_widget, 0, 0, 1, 40)
            self.main_layout.addWidget(self.left_widget, 1, 0, 15, 6)
            self.main_layout.addWidget(self.right_home_widget, 1, 6, 15, 34)
            self.main_layout.addWidget(self.right_explorer_widget, 1, 6, 15, 34)
            # 重置状态
            self.getFold = False

    def addTable(self, row, row_data):
        for _ in range(len(row_data)):
            newItem = QtWidgets.QTableWidgetItem(row_data[_])
            newItem.setForeground(Qt.QBrush(Qt.QColor(190, 190, 190)))
            self.right_information_table.setItem(row-1, _, newItem)


def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = MainUi()
    gui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
