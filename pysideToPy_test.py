from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtUiTools import*         # QtUITools 模块提供类去操作由 Qt Designer 创建的窗口
from PySide2 import QtWidgets        # Qt Widgets 模块提供UI元素模块
from PySide2 import QtCore			# QtCore 是Qt的最基础的模块	


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(541, 311)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.tab.setFont(font)
        self.tab.setObjectName("tab")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 40, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 40, 75, 23))
        self.pushButton_3.setToolTip("")
        self.pushButton_3.setToolTipDuration(2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.toolButton_2 = QtWidgets.QToolButton(self.tab_2)
        self.toolButton_2.setGeometry(QtCore.QRect(20, 80, 37, 18))
        self.toolButton_2.setObjectName("toolButton_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.horizontalLayout_3.addWidget(self.tabWidget)
        self.widget = QtWidgets.QWidget(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.toolButton = QtWidgets.QToolButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton.sizePolicy().hasHeightForWidth())
        self.toolButton.setSizePolicy(sizePolicy)
        self.toolButton.setMinimumSize(QtCore.QSize(150, 150))
        self.toolButton.setObjectName("toolButton")
        self.verticalLayout.addWidget(self.toolButton)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setMinimumSize(QtCore.QSize(54, 0))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.lineEdit.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText("")
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setToolTip("")
        self.pushButton.setToolTipDuration(-1)
        self.pushButton.setStatusTip("")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        spacerItem = QtWidgets.QSpacerItem(192, 43, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_3.addWidget(self.widget)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        #定义控件点击连接函数（在类的初始化函数定义）
        self.crea_connections()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(u'星星牌脚本V1.1')
        self.tabWidget.setToolTip("厉害了")
        self.tabWidget.setWhatsThis(_translate("Dialog", "<html><head/><body><p>895</p></body></html>"))
        self.pushButton_2.setText(_translate("Dialog", "Button1"))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Tab 1"))
        self.pushButton_3.setText(_translate("Dialog", "Button2"))

        self.toolButton_2.setText(_translate("Dialog", "..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Tab 2"))
        self.toolButton.setText(_translate("Dialog", "..."))
        self.label.setText(_translate("Dialog", "name"))
        self.label_2.setText(_translate("Dialog", "TextLabel"))
        self.pushButton.setText(_translate("Dialog", "OK"))
        self.pushButton.setToolTip(_translate("Dialog", "工具提示"))
        
        

    #创建控件点击连接函数
    def crea_connections(self):
        self.pushButton_2.clicked.connect(self.testConnect1)
        self.pushButton_3.clicked.connect(self.testConnect2)
        self.pushButton.clicked.connect(self.testConnect)

    #控件点击执行函数
    def testConnect(self):
        print ('HelloWorld')

    def testConnect1(self):
        Name = self.pushButton_2.text()
        print (Name)
        if Name=='Button1':
            self.pushButton_2.setText(u'按钮1')
        else:
            self.pushButton_2.setText('Button1')

    def testConnect2(self):
        print ('按钮2')



class myQt(Ui_Dialog,QtWidgets.QDialog):        #第一个参数填写UI文件转化出来的第一个类的名称（Ui_Dialog）
    def __init__(self):     # 可关联到Maya主窗口，设置为Maya子窗口，parent = none则是独立窗口
        Ui_Dialog.__init__(self)
        QtWidgets.QDialog.__init__(self)
        MaxPlus.AttachQWidgetToMax(self)    #设置以max为父窗口
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)  # 去除窗口上的问号
        

        self.setupUi(self)
        self.retranslateUi(self)

    def wnd_close(self):
        self.close()
        self.deleteLater()
        print (u'工具关闭。')

if __name__ == '__main__':        
    try:
        myUI.wnd_close()
    except:
        pass
    
    myUI = myQt()        # 类对象化 myUl
    myUI.show()        # 显示窗口