# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'merckSSFormatter.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(439, 472)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(180, 410, 221, 41))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.first_excel = QtWidgets.QLineEdit(Dialog)
        self.first_excel.setGeometry(QtCore.QRect(20, 70, 151, 20))
        self.first_excel.setObjectName("first_excel")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 0, 411, 31))
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 47, 13))
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(183, 50, 20, 301))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 100, 47, 13))
        self.label_3.setObjectName("label_3")
        self.second_excel = QtWidgets.QLineEdit(Dialog)
        self.second_excel.setGeometry(QtCore.QRect(20, 120, 151, 20))
        self.second_excel.setObjectName("second_excel")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 150, 47, 13))
        self.label_4.setObjectName("label_4")
        self.third_excel = QtWidgets.QLineEdit(Dialog)
        self.third_excel.setGeometry(QtCore.QRect(20, 170, 151, 20))
        self.third_excel.setObjectName("third_excel")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 200, 47, 13))
        self.label_5.setObjectName("label_5")
        self.fourth_excel = QtWidgets.QLineEdit(Dialog)
        self.fourth_excel.setGeometry(QtCore.QRect(20, 220, 151, 20))
        self.fourth_excel.setObjectName("fourth_excel")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(20, 250, 47, 13))
        self.label_6.setObjectName("label_6")
        self.fifth_excel = QtWidgets.QLineEdit(Dialog)
        self.fifth_excel.setGeometry(QtCore.QRect(20, 270, 151, 20))
        self.fifth_excel.setObjectName("fifth_excel")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(20, 300, 47, 13))
        self.label_7.setObjectName("label_7")
        self.sixth_excel = QtWidgets.QLineEdit(Dialog)
        self.sixth_excel.setGeometry(QtCore.QRect(20, 320, 151, 20))
        self.sixth_excel.setObjectName("sixth_excel")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(210, 30, 91, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(330, 30, 81, 16))
        self.label_9.setObjectName("label_9")
        self.first_image_start = QtWidgets.QLineEdit(Dialog)
        self.first_image_start.setGeometry(QtCore.QRect(230, 70, 51, 20))
        self.first_image_start.setMaxLength(3)
        self.first_image_start.setAlignment(QtCore.Qt.AlignCenter)
        self.first_image_start.setObjectName("first_image_start")
        self.first_image_end = QtWidgets.QLineEdit(Dialog)
        self.first_image_end.setGeometry(QtCore.QRect(340, 70, 51, 20))
        self.first_image_end.setObjectName("first_image_end")
        self.first_image_end.setMaxLength(3)
        self.first_image_end.setAlignment(QtCore.Qt.AlignCenter)
        self.second_image_start = QtWidgets.QLineEdit(Dialog)
        self.second_image_start.setGeometry(QtCore.QRect(230, 120, 51, 20))
        self.second_image_start.setMaxLength(3)
        self.second_image_start.setAlignment(QtCore.Qt.AlignCenter)
        self.second_image_start.setObjectName("second_image_start")
        self.second_image_end = QtWidgets.QLineEdit(Dialog)
        self.second_image_end.setGeometry(QtCore.QRect(340, 120, 51, 20))
        self.second_image_end.setMaxLength(3)
        self.second_image_end.setAlignment(QtCore.Qt.AlignCenter)
        self.second_image_end.setObjectName("second_image_end")
        self.third_image_start = QtWidgets.QLineEdit(Dialog)
        self.third_image_start.setGeometry(QtCore.QRect(230, 170, 51, 20))
        self.third_image_start.setMaxLength(3)
        self.third_image_start.setAlignment(QtCore.Qt.AlignCenter)
        self.third_image_start.setObjectName("third_image_start")
        self.third_image_end = QtWidgets.QLineEdit(Dialog)
        self.third_image_end.setGeometry(QtCore.QRect(340, 170, 51, 20))
        self.third_image_end.setMaxLength(3)
        self.third_image_end.setAlignment(QtCore.Qt.AlignCenter)
        self.third_image_end.setObjectName("third_image_end")
        self.fourth_image_start = QtWidgets.QLineEdit(Dialog)
        self.fourth_image_start.setGeometry(QtCore.QRect(230, 220, 51, 20))
        self.fourth_image_start.setMaxLength(3)
        self.fourth_image_start.setAlignment(QtCore.Qt.AlignCenter)
        self.fourth_image_start.setObjectName("fourth_image_start")
        self.fourth_image_end = QtWidgets.QLineEdit(Dialog)
        self.fourth_image_end.setGeometry(QtCore.QRect(340, 220, 51, 20))
        self.fourth_image_end.setMaxLength(3)
        self.fourth_image_end.setAlignment(QtCore.Qt.AlignCenter)
        self.fourth_image_end.setObjectName("fourth_image_end")
        self.fifth_image_start = QtWidgets.QLineEdit(Dialog)
        self.fifth_image_start.setGeometry(QtCore.QRect(230, 270, 51, 20))
        self.fifth_image_start.setMaxLength(3)
        self.fifth_image_start.setAlignment(QtCore.Qt.AlignCenter)
        self.fifth_image_start.setObjectName("fifth_image_start")
        self.fifth_image_end = QtWidgets.QLineEdit(Dialog)
        self.fifth_image_end.setGeometry(QtCore.QRect(340, 270, 51, 20))
        self.fifth_image_end.setMaxLength(3)
        self.fifth_image_end.setAlignment(QtCore.Qt.AlignCenter)
        self.fifth_image_end.setObjectName("fifth_image_end")
        self.sixth_image_start = QtWidgets.QLineEdit(Dialog)
        self.sixth_image_start.setGeometry(QtCore.QRect(230, 320, 51, 20))
        self.sixth_image_start.setMaxLength(3)
        self.sixth_image_start.setAlignment(QtCore.Qt.AlignCenter)
        self.sixth_image_start.setObjectName("sixth_image_start")
        self.sixth_image_end = QtWidgets.QLineEdit(Dialog)
        self.sixth_image_end.setGeometry(QtCore.QRect(340, 320, 51, 20))
        self.sixth_image_end.setMaxLength(3)
        self.sixth_image_end.setAlignment(QtCore.Qt.AlignCenter)
        self.sixth_image_end.setObjectName("sixth_image_end")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(30, 360, 161, 16))
        self.label_10.setObjectName("label_10")
        self.word_template = QtWidgets.QLineEdit(Dialog)
        self.word_template.setGeometry(QtCore.QRect(30, 380, 361, 20))
        self.word_template.setObjectName("word_doc_template")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "MerckSSFormatter"))
        self.label.setText(_translate("Dialog", "Please provide direct paths to xlsx in the order you want it to appear in the Word doc"))
        self.label_2.setText(_translate("Dialog", "Excel 1"))
        self.label_3.setText(_translate("Dialog", "Excel 2"))
        self.label_4.setText(_translate("Dialog", "Excel 3"))
        self.label_5.setText(_translate("Dialog", "Excel 4"))
        self.label_6.setText(_translate("Dialog", "Excel 5"))
        self.label_7.setText(_translate("Dialog", "Excel 6"))
        self.label_8.setText(_translate("Dialog", "First Image Row"))
        self.label_9.setText(_translate("Dialog", "Last Image Row"))
        self.label_10.setText(_translate("Dialog", "Path to Word Doc Template"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())