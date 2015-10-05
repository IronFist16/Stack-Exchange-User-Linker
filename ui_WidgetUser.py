# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_WidgetUser.ui'
#
# Created: Sat Oct  3 11:06:39 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Frame_Widget_User(object):
    def setupUi(self, Frame_Widget_User):
        Frame_Widget_User.setObjectName(_fromUtf8("Frame_Widget_User"))
        Frame_Widget_User.setWindowModality(QtCore.Qt.ApplicationModal)
        Frame_Widget_User.resize(152, 120)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Frame_Widget_User.sizePolicy().hasHeightForWidth())
        Frame_Widget_User.setSizePolicy(sizePolicy)
        Frame_Widget_User.setMinimumSize(QtCore.QSize(152, 120))
        Frame_Widget_User.setMaximumSize(QtCore.QSize(152, 120))
        Frame_Widget_User.setStyleSheet(_fromUtf8("background-color: rgb(255, 170, 127);"))
        Frame_Widget_User.setFrameShape(QtGui.QFrame.Box)
        Frame_Widget_User.setFrameShadow(QtGui.QFrame.Plain)
        Frame_Widget_User.setLineWidth(3)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Frame_Widget_User)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.Widget_Widget_User = QtGui.QWidget(Frame_Widget_User)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Widget_Widget_User.sizePolicy().hasHeightForWidth())
        self.Widget_Widget_User.setSizePolicy(sizePolicy)
        self.Widget_Widget_User.setMinimumSize(QtCore.QSize(152, 120))
        self.Widget_Widget_User.setMaximumSize(QtCore.QSize(152, 120))
        self.Widget_Widget_User.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.Widget_Widget_User.setObjectName(_fromUtf8("Widget_Widget_User"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.Widget_Widget_User)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setMargin(5)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_Widget_User_Profile = QtGui.QLabel(self.Widget_Widget_User)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_Widget_User_Profile.sizePolicy().hasHeightForWidth())
        self.label_Widget_User_Profile.setSizePolicy(sizePolicy)
        self.label_Widget_User_Profile.setMinimumSize(QtCore.QSize(64, 64))
        self.label_Widget_User_Profile.setMaximumSize(QtCore.QSize(64, 64))
        self.label_Widget_User_Profile.setStyleSheet(_fromUtf8(""))
        self.label_Widget_User_Profile.setFrameShape(QtGui.QFrame.Box)
        self.label_Widget_User_Profile.setText(_fromUtf8(""))
        self.label_Widget_User_Profile.setObjectName(_fromUtf8("label_Widget_User_Profile"))
        self.horizontalLayout_4.addWidget(self.label_Widget_User_Profile)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_Widget_User_Repuation = QtGui.QLabel(self.Widget_Widget_User)
        self.label_Widget_User_Repuation.setStyleSheet(_fromUtf8("color: rgb(0, 0, 127);\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.label_Widget_User_Repuation.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_Widget_User_Repuation.setScaledContents(False)
        self.label_Widget_User_Repuation.setObjectName(_fromUtf8("label_Widget_User_Repuation"))
        self.verticalLayout.addWidget(self.label_Widget_User_Repuation)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.Widget_Widget_User)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(10, 10))
        self.label.setMaximumSize(QtCore.QSize(10, 10))
        self.label.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 255), stop:0.528302 rgba(255, 215, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 215, 0, 255), stop:0.528302 rgba(255, 255, 127, 255), stop:1 rgba(255, 215, 0, 255));"))
        self.label.setFrameShape(QtGui.QFrame.NoFrame)
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.label_Widget_User_Gold = QtGui.QLabel(self.Widget_Widget_User)
        self.label_Widget_User_Gold.setStyleSheet(_fromUtf8("color: rgb(0, 0, 127);\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.label_Widget_User_Gold.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_Widget_User_Gold.setLineWidth(1)
        self.label_Widget_User_Gold.setObjectName(_fromUtf8("label_Widget_User_Gold"))
        self.horizontalLayout.addWidget(self.label_Widget_User_Gold)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.Widget_Widget_User)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(10, 10))
        self.label_2.setMaximumSize(QtCore.QSize(10, 10))
        self.label_2.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 255), stop:0.528302 rgba(192, 192, 192, 255), stop:1 rgba(255, 255, 255, 255));\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(192, 192, 192, 255), stop:0.528302 rgba(236, 236, 236, 255), stop:1 rgba(192, 192, 192, 255));"))
        self.label_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.label_Widget_User_Silver = QtGui.QLabel(self.Widget_Widget_User)
        self.label_Widget_User_Silver.setStyleSheet(_fromUtf8("color: rgb(0, 0, 127);\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.label_Widget_User_Silver.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_Widget_User_Silver.setLineWidth(1)
        self.label_Widget_User_Silver.setObjectName(_fromUtf8("label_Widget_User_Silver"))
        self.horizontalLayout_2.addWidget(self.label_Widget_User_Silver)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_4 = QtGui.QLabel(self.Widget_Widget_User)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(10, 10))
        self.label_4.setMaximumSize(QtCore.QSize(10, 10))
        self.label_4.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 255), stop:0.528302 rgba(205, 127, 50, 255), stop:1 rgba(255, 255, 255, 255));\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(205, 127, 50, 255), stop:0.528302 rgba(255, 155, 62, 255), stop:1 rgba(205, 127, 50, 255));"))
        self.label_4.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_3.addWidget(self.label_4)
        self.label_Widget_User_Bronze = QtGui.QLabel(self.Widget_Widget_User)
        self.label_Widget_User_Bronze.setStyleSheet(_fromUtf8("color: rgb(0, 0, 127);\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.label_Widget_User_Bronze.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_Widget_User_Bronze.setLineWidth(1)
        self.label_Widget_User_Bronze.setObjectName(_fromUtf8("label_Widget_User_Bronze"))
        self.horizontalLayout_3.addWidget(self.label_Widget_User_Bronze)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.label_Widget_User_Name = QLabelCustom(self.Widget_Widget_User)
        self.label_Widget_User_Name.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_Widget_User_Name.setStyleSheet(_fromUtf8("color: rgb(0, 0, 127);\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgba(155, 155, 155);"))
        self.label_Widget_User_Name.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_Widget_User_Name.setScaledContents(False)
        self.label_Widget_User_Name.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Widget_User_Name.setWordWrap(True)
        self.label_Widget_User_Name.setIndent(0)
        self.label_Widget_User_Name.setObjectName(_fromUtf8("label_Widget_User_Name"))
        self.verticalLayout_3.addWidget(self.label_Widget_User_Name)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout_2.addWidget(self.Widget_Widget_User)

        self.retranslateUi(Frame_Widget_User)
        QtCore.QMetaObject.connectSlotsByName(Frame_Widget_User)

    def retranslateUi(self, Frame_Widget_User):
        Frame_Widget_User.setWindowTitle(_translate("Frame_Widget_User", "Frame", None))
        self.label_Widget_User_Repuation.setText(_translate("Frame_Widget_User", "12345678", None))
        self.label_Widget_User_Gold.setText(_translate("Frame_Widget_User", "10", None))
        self.label_Widget_User_Silver.setText(_translate("Frame_Widget_User", "100", None))
        self.label_Widget_User_Bronze.setText(_translate("Frame_Widget_User", "999", None))
        self.label_Widget_User_Name.setText(_translate("Frame_Widget_User", "Khalil Ammour ", None))

from QLabelCustom import QLabelCustom
