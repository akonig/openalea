# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'preferences.ui'
#
# Created: Tue Dec  4 16:17:13 2007
#      by: PyQt4 UI code generator 4.3.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Preferences(object):
    def setupUi(self, Preferences):
        Preferences.setObjectName("Preferences")
        Preferences.resize(QtCore.QSize(QtCore.QRect(0,0,480,350).size()).expandedTo(Preferences.minimumSizeHint()))

        self.gridlayout = QtGui.QGridLayout(Preferences)
        self.gridlayout.setMargin(9)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName("gridlayout")

        self.tabWidget = QtGui.QTabWidget(Preferences)
        self.tabWidget.setObjectName("tabWidget")

        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")

        self.gridlayout1 = QtGui.QGridLayout(self.tab)
        self.gridlayout1.setMargin(9)
        self.gridlayout1.setSpacing(6)
        self.gridlayout1.setObjectName("gridlayout1")

        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setObjectName("label_2")
        self.gridlayout1.addWidget(self.label_2,0,0,1,1)

        self.pathList = QtGui.QListWidget(self.tab)
        self.pathList.setObjectName("pathList")
        self.gridlayout1.addWidget(self.pathList,0,1,3,1)

        self.addButton = QtGui.QPushButton(self.tab)
        self.addButton.setObjectName("addButton")
        self.gridlayout1.addWidget(self.addButton,1,0,1,1)

        self.removeButton = QtGui.QPushButton(self.tab)
        self.removeButton.setObjectName("removeButton")
        self.gridlayout1.addWidget(self.removeButton,2,0,1,1)

        self.includenmspace = QtGui.QCheckBox(self.tab)
        self.includenmspace.setObjectName("includenmspace")
        self.gridlayout1.addWidget(self.includenmspace,3,1,1,1)
        self.tabWidget.addTab(self.tab,"")

        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName("tab_4")

        self.label_3 = QtGui.QLabel(self.tab_4)
        self.label_3.setGeometry(QtCore.QRect(20,20,56,17))
        self.label_3.setObjectName("label_3")

        self.listAlgo = QtGui.QListWidget(self.tab_4)
        self.listAlgo.setGeometry(QtCore.QRect(20,40,171,211))
        self.listAlgo.setObjectName("listAlgo")
        self.tabWidget.addTab(self.tab_4,"")

        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2,"")

        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName("tab_3")

        self.gridlayout2 = QtGui.QGridLayout(self.tab_3)
        self.gridlayout2.setMargin(9)
        self.gridlayout2.setSpacing(6)
        self.gridlayout2.setObjectName("gridlayout2")

        self.label = QtGui.QLabel(self.tab_3)
        self.label.setObjectName("label")
        self.gridlayout2.addWidget(self.label,0,0,1,1)

        self.dbclickBox = QtGui.QComboBox(self.tab_3)
        self.dbclickBox.setObjectName("dbclickBox")
        self.gridlayout2.addWidget(self.dbclickBox,0,1,1,1)

        self.comboBox = QtGui.QComboBox(self.tab_3)
        self.comboBox.setObjectName("comboBox")
        self.gridlayout2.addWidget(self.comboBox,1,1,1,1)

        self.label_edge_style = QtGui.QLabel(self.tab_3)
        self.label_edge_style.setObjectName("label_edge_style")
        self.gridlayout2.addWidget(self.label_edge_style,1,0,1,1)
        self.tabWidget.addTab(self.tab_3,"")
        self.gridlayout.addWidget(self.tabWidget,0,0,1,1)

        self.buttonBox = QtGui.QDialogButtonBox(Preferences)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.NoButton|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridlayout.addWidget(self.buttonBox,1,0,1,1)

        self.retranslateUi(Preferences)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox,QtCore.SIGNAL("accepted()"),Preferences.accept)
        QtCore.QObject.connect(self.buttonBox,QtCore.SIGNAL("rejected()"),Preferences.reject)
        QtCore.QMetaObject.connectSlotsByName(Preferences)

    def retranslateUi(self, Preferences):
        Preferences.setWindowTitle(QtGui.QApplication.translate("Preferences", "Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Preferences", "Search Path", None, QtGui.QApplication.UnicodeUTF8))
        self.addButton.setText(QtGui.QApplication.translate("Preferences", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.removeButton.setText(QtGui.QApplication.translate("Preferences", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.includenmspace.setText(QtGui.QApplication.translate("Preferences", "Include OpenAlea namespace directories", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("Preferences", "Package Manager", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Preferences", "Algorithm", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QtGui.QApplication.translate("Preferences", "Dataflow", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("Preferences", "Python Editor", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Preferences", "Double click on item", None, QtGui.QApplication.UnicodeUTF8))
        self.dbclickBox.addItem(QtGui.QApplication.translate("Preferences", "Run + Open (Default)", None, QtGui.QApplication.UnicodeUTF8))
        self.dbclickBox.addItem(QtGui.QApplication.translate("Preferences", "Run", None, QtGui.QApplication.UnicodeUTF8))
        self.dbclickBox.addItem(QtGui.QApplication.translate("Preferences", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.addItem(QtGui.QApplication.translate("Preferences", "Line (Default)", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.addItem(QtGui.QApplication.translate("Preferences", "Polyline", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.addItem(QtGui.QApplication.translate("Preferences", "Spline", None, QtGui.QApplication.UnicodeUTF8))
        self.label_edge_style.setText(QtGui.QApplication.translate("Preferences", "Edge Style", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtGui.QApplication.translate("Preferences", "UI", None, QtGui.QApplication.UnicodeUTF8))

