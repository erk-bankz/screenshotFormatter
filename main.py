from ui_merckSSformatter import Ui_Dialog
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import QtWidgets
import modules
import docx
import win32com.client as win32


class Dialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)
        self.setupUi(self)
        self.buttonBox.clicked.connect(self.buttonClicked)  # alternative way to call your method
    # @pyqtSlot()

    def buttonClicked(self):
        list_of_excels = []
        tup_one = (self.first_excel.text(), self.first_image_start.text(), self.first_image_end.text())
        tup_two = (self.second_excel.text(), self.second_image_start.text(), self.second_image_end.text())
        tup_three = (self.third_excel.text(), self.third_image_start.text(), self.third_image_end.text())
        tup_four = (self.fourth_excel.text(), self.fourth_image_start.text(), self.fourth_image_end.text())
        tup_five = (self.fifth_excel.text(), self.fifth_image_start.text(), self.fifth_image_end.text())
        tup_six = (self.sixth_excel.text(), self.sixth_image_start.text(), self.sixth_image_end.text())
        list_of_excels.append(tup_one)
        list_of_excels.append(tup_two)
        list_of_excels.append(tup_three)
        list_of_excels.append(tup_four)
        list_of_excels.append(tup_five)
        list_of_excels.append(tup_six)
        docu = docx.Document(self.word_template.text())
        modules.change_orientation(docu)
        modules.extract_img_to_word_doc(list_of_excels, docu, self.word_template.text())
        modules.wrapping_pictures(self.word_template.text())



if __name__ == "__main__":
    import sys
    application = QApplication(sys.argv)
    macro_dialog = Dialog() # create object of dialog, **use the name of your class (ie class Dialog)**
    macro_dialog.show()
    sys.exit(application.exec_())