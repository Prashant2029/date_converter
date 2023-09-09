from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.uic import loadUi
from nepali_date_converter import english_to_nepali_converter, nepali_to_english_converter
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        loadUi('calendar.ui', self)
        self.convert.clicked.connect(self.convert_date)

    def convert_date(self):
        selected_choice = self.choice.currentText()

        if selected_choice == "BS to AD":
            try:
                bs_year = int(self.year.text())
                bs_month = int(self.month.text())
                bs_day = int(self.day.text())

                converted_date = nepali_to_english_converter(bs_year, bs_month, bs_day)
                self.label.setText(converted_date)

            except Exception as e:
                error_message = "An error occurred: " + str(e)
                QMessageBox.warning(self, "Error", error_message)

        elif selected_choice == "AD to BS":
            try:
                ad_year = int(self.year.text())
                ad_month = int(self.month.text())
                ad_day = int(self.day.text())

                converted_date = english_to_nepali_converter(ad_year, ad_month, ad_day)
                self.label.setText(converted_date)
            except Exception as e:
                error_message = "An error occurred: " + str(e)
                QMessageBox.warning(self, "Error", error_message)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
